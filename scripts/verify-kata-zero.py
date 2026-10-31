#!/usr/bin/env python3
"""Comprobación de producción del material, separada de la primera prueba docente."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
JDK = "25.0.5.0+8-zulu"
java_home = Path(os.environ.get("SDKMAN_DIR", str(Path.home() / ".sdkman"))) / "candidates/java" / JDK
java = java_home / "bin/java"
if not java.is_file():
    sys.exit(f"Instala el JDK del curso con SDKMAN: sdk install java {JDK}")

env = os.environ.copy()
env["JAVA_HOME"] = str(java_home)
env["PATH"] = str(java_home / "bin") + os.pathsep + env.get("PATH", "")
version = subprocess.run([str(java), "-XshowSettings:properties", "-version"],
                         capture_output=True, text=True, check=True, env=env)
if "java.runtime.version = 25.0.5+8-LTS" not in version.stderr or "java.vendor = Azul Systems, Inc." not in version.stderr:
    sys.exit("La instalación no corresponde al build Zulu 25.0.5+8 del curso.")

print(f"JDK: {java_home}", flush=True)
subprocess.run([str(ROOT / "mvnw"), "-B", "-ntp", "clean", "verify"],
               cwd=ROOT, env=env, check=True)

stages = ["before", "after/01-small-refactor", "after/02-first-test"]
main_path = Path("src/main/java/mx/serviciosocial/katazero")
for name in ["Main.java", "RebalanceCalculator.java"]:
    if (ROOT / "kata-zero" / stages[1] / main_path / name).read_bytes() != (ROOT / "kata-zero" / stages[2] / main_path / name).read_bytes():
        sys.exit(f"La etapa de la primera prueba cambió producción: {name}")

# Valores esperados independientes, obtenidos a mano del contrato de la kata.
cases = [
    ("cuenta inicial y plan sin mutación", "1\n4\n1\n0\n",
     ["VENDER META 5.2000 acciones", "COMPRAR AAPL 13.0000 acciones", "Valor total USD: 6000.00"],
     ["Posición actualizada."]),
    ("precio actualizado", "2\nMETA\n400\n4\n0\n",
     ["Valor total USD: 5000.00", "VENDER META 5.0000 acciones", "COMPRAR AAPL 10.0000 acciones"], []),
    ("cuenta ya balanceada", "5\nMETA\n4.8\n5\nAAPL\n18\n4\n0\n",
     ["Sin operaciones: la cuenta ya está balanceada a esta precisión."], ["VENDER ", "COMPRAR "]),
    ("entrada a una posición nueva", "3\n0\n0\n1\n4\n0\n",
     ["VENDER META 10.0000 acciones", "VENDER AAPL 5.0000 acciones", "COMPRAR NVDA 60.0000 acciones"], []),
    ("distribución inválida conserva objetivo", "3\n0.5\n0.6\n0\n4\n0\n",
     ["No se cambió el objetivo.", "VENDER META 5.2000 acciones", "COMPRAR AAPL 13.0000 acciones"], []),
    ("precios inválidos conservan valor", "2\nMETA\n0\n2\nMETA\n-1\n4\n0\n",
     ["El precio debe ser positivo.", "Valor total USD: 6000.00"], ["Precio actualizado."]),
    ("cantidad negativa conserva posición", "5\nMETA\n-1\n4\n0\n",
     ["La cantidad no puede ser negativa.", "VENDER META 5.2000 acciones"], ["Posición actualizada."]),
    ("números y opciones inválidos", "texto\n99\n2\nMETA\ntexto\n4\n0\n",
     ["Escribe un número válido", "Opción no válida.", "VENDER META 5.2000 acciones"], []),
    ("símbolo desconocido y normalización", "2\nOTRO\n2\n meta \n400\n4\n0\n",
     ["Símbolo no admitido.", "VENDER META 5.0000 acciones"], []),
    ("cuenta vacía", "5\nMETA\n0\n5\nAAPL\n0\n4\n0\n",
     ["Valor total USD: 0.00", "Sin operaciones:"], ["VENDER ", "COMPRAR "]),
    ("redondeo y venta limitada a lo disponible", "5\nMETA\n0.00007\n3\n0\n1\n0\n4\n0\n",
     ["VENDER META 0.00007 acciones", "COMPRAR AAPL 0.0002 acciones"], []),
    ("fin de entrada dentro de un menú", "3\n0.4\n", ["Hasta luego."], []),
]

for label, input_text, required, forbidden in cases:
    outputs = []
    for stage in stages:
        classes = ROOT / "kata-zero" / stage / "target/classes"
        result = subprocess.run([str(java), "-cp", str(classes), "mx.serviciosocial.katazero.Main"],
                                input=input_text, capture_output=True, text=True, timeout=10,
                                check=True, env=env)
        for fragment in required:
            if fragment not in result.stdout:
                sys.exit(f"{label} ({stage}): falta {fragment!r}")
        for fragment in forbidden:
            if fragment in result.stdout:
                sys.exit(f"{label} ({stage}): apareció {fragment!r}")
        if label == "cuenta inicial y plan sin mutación":
            if result.stdout.count("META | acciones: 10") != 2 or result.stdout.count("AAPL | acciones: 5") != 2:
                sys.exit(f"{stage}: el plan modificó la cuenta")
        if result.stderr:
            sys.exit(f"{label} ({stage}): stderr inesperado: {result.stderr}")
        outputs.append(result.stdout)
    if not all(output == outputs[0] for output in outputs):
        sys.exit(f"La salida cambió entre etapas: {label}")
    print(f"OK · {label}", flush=True)

print(f"{len(cases)} escenarios × {len(stages)} etapas: mismas salidas y resultados esperados.")
