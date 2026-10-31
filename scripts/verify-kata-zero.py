#!/usr/bin/env python3
"""Validación del material: ejemplo habitual, defecto reproducible y corrección."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
JDK = "25.0.5.0+8-zulu"
java_home = Path(os.environ.get("SDKMAN_DIR", str(Path.home() / ".sdkman"))) / "candidates/java" / JDK
java = java_home / "bin/java"
if not java.is_file():
    sys.exit(f"Instala el JDK del curso: sdk install java {JDK}")
env = os.environ.copy()
env["JAVA_HOME"] = str(java_home)
env["PATH"] = str(java_home / "bin") + os.pathsep + env.get("PATH", "")
version = subprocess.run([str(java), "-XshowSettings:properties", "-version"],
                         capture_output=True, text=True, check=True, env=env)
if "java.runtime.version = 25.0.5+8-LTS" not in version.stderr or "java.vendor = Azul Systems, Inc." not in version.stderr:
    sys.exit("Se requiere exactamente Zulu 25.0.5+8.")

wrapper = str(ROOT / "mvnw")
stages = [ROOT / "kata-zero" / path for path in
          ["before", "after/01-small-refactor", "after/02-first-test"]]
source = Path("src/main/java/mx/serviciosocial/katazero")
print(f"JDK: {java_home}", flush=True)
subprocess.run([wrapper, "-B", "-ntp", "clean", "verify"], cwd=ROOT, env=env, check=True)
assert (stages[1] / source / "Main.java").read_bytes() == (stages[2] / source / "Main.java").read_bytes()


def run_console(project, input_text):
    result = subprocess.run([str(java), "-cp", str(project / "target/classes"),
                             "mx.serviciosocial.katazero.Main"], input=input_text,
                            capture_output=True, text=True, timeout=10, check=True, env=env)
    assert not result.stderr, result.stderr
    return result.stdout


cases = [
    ("cuenta inicial y plan sin mutación", "1\n2\n1\n0\n"),
    ("plan repetido", "2\n2\n0\n"),
    ("opción no válida", "99\n0\n"),
    ("fin de entrada", ""),
]
for label, input_text in cases:
    outputs = [run_console(stage, input_text) for stage in stages]
    assert all(output == outputs[0] for output in outputs), label
    if label == "cuenta inicial y plan sin mutación":
        for output in outputs:
            assert "VENDER META 2.0000 acciones" in output
            assert "COMPRAR AAPL 2.0000 acciones" in output
            assert output.count("META: 10 acciones a 100.00 USD") == 2
            assert output.count("AAPL: 10 acciones a 100.00 USD") == 2
    elif label == "plan repetido":
        assert outputs[0].count("VENDER META 2.0000 acciones") == 2
    elif label == "opción no válida":
        assert "Opción no válida." in outputs[0]
    assert "Hasta luego." in outputs[0]
    print(f"OK · {label}: salida idéntica en tres etapas", flush=True)

# Crear copias temporales: el menú ya no edita precios y no se toca el material original.
with tempfile.TemporaryDirectory(prefix="kata-zero-") as temporary:
    altered_outputs = []
    for index, stage in enumerate(stages):
        copy = Path(temporary) / str(index)
        shutil.copytree(stage, copy, ignore=shutil.ignore_patterns("target"))
        main = copy / source / "Main.java"
        original = main.read_text()
        assert original.count('"100.00"') == 2
        main.write_text(original.replace('"100.00"', '"150.00"', 1))
        subprocess.run([wrapper, "-B", "-ntp", "-q", "-f", str(copy / "pom.xml"), "compile"],
                       cwd=ROOT, env=env, check=True)
        altered_outputs.append(run_console(copy, "1\n2\n0\n"))
    assert altered_outputs[0] == altered_outputs[1], "La extracción cambió el defecto"
    assert "VENDER META 4.0000 acciones" in altered_outputs[0]
    assert "VENDER META 3.3333 acciones" in altered_outputs[2]
    assert "Valor total: 2500.00 USD" in altered_outputs[2]
    assert altered_outputs[2] == altered_outputs[0].replace("META 4.0000", "META 3.3333")
    print("OK · precio 150: before y refactor venden 4.0000; corregido vende 3.3333", flush=True)

    red = Path(temporary) / "red-test"
    shutil.copytree(stages[2], red, ignore=shutil.ignore_patterns("target"))
    shutil.copyfile(stages[1] / source / "RebalanceCalculator.java",
                    red / source / "RebalanceCalculator.java")
    result = subprocess.run([wrapper, "-B", "-ntp", "-f", str(red / "pom.xml"), "test"],
                            cwd=ROOT, env=env, capture_output=True, text=True)
    assert result.returncode != 0, "La primera prueba no detectó el defecto"
    assert "expected: <-3.3333> but was: <-4.0000>" in result.stdout, result.stdout + result.stderr
    print("OK · la misma prueba falla con la fórmula original y pasa con la corregida", flush=True)

print("15 ejecuciones de consola verificadas; rojo/verde reproducido sin modificar los originales.")
