# Validación de Kata Zero

Fecha: 31 de octubre de 2026. Plataforma de verificación: macOS aarch64. No se comprobó la ejecución en Windows ni desde el IDE.

## Entorno usado

- SDKMAN: `25.0.5.0+8-zulu`.
- `java -version`: OpenJDK 25.0.5, Zulu25.38+107-CA, build 25.0.5+8-LTS.
- Proveedor: Azul Systems, Inc.
- Maven 3.10.0 mediante Maven Wrapper 3.3.4.
- Compiler 3.16.0; Surefire 3.6.1; JUnit Jupiter 6.1.3 en la tercera etapa.

No se cambió el JDK predeterminado del equipo. Se usaron JAVA_HOME y PATH del JDK solicitado.

## Construcción y primera prueba

Comando reproducible desde la raíz: `python3 scripts/verify-kata-zero.py`. El script selecciona y comprueba el JDK exacto, ejecuta `./mvnw -B -ntp clean verify` y verifica los recorridos de consola.

Resultado: BUILD SUCCESS en los tres proyectos y en el agregador. La tercera etapa ejecutó **1 prueba, 0 fallas, 0 errores, 0 omitidas**. Las dos primeras no tienen pruebas JUnit y se compilaron y empaquetaron.

## Demostración de falla

Se cambió temporalmente `subtract(currentQuantity.multiply(price))` por `add(currentQuantity.multiply(price))` en la tercera etapa. Maven terminó con error de prueba y JUnit reportó `expected: <-5.2000> but was: <14.8000>`.

Se restauró el archivo original y se ejecutó la validación completa con éxito. El código entregado conserva la resta correcta. La modificación defectuosa no se conserva en un commit ni se necesita para ejecutar el material.

## Comparación de etapas

Se ejecutaron los siguientes escenarios en before, after/01 y after/02. Se comprobaron fragmentos esperados calculados del contrato y coincidencia de toda la salida entre etapas:

1. Cuenta inicial, plan y consulta posterior sin mutación.
2. Cambio de precio de META a 400 USD.
3. Cuenta ya balanceada.
4. Distribución nueva hacia una posición inicialmente vacía.
5. Distribución cuya suma es inválida, conservando la anterior.
6. Precios cero y negativos rechazados.
7. Cantidad negativa rechazada sin cambiar posición.
8. Números y opciones inválidos.
9. Símbolo desconocido y normalización de espacios y mayúsculas.
10. Cuenta vacía.
11. Redondeo y límite de venta para no exceder lo disponible.
12. Fin de entrada durante la captura de distribución.

Resultado: **12 escenarios × 3 etapas = 36 ejecuciones**, todas con las mismas salidas y los resultados esperados. También se comprobó identidad byte a byte de Main.java y RebalanceCalculator.java entre las dos carpetas after.

Esto no demuestra corrección para toda entrada posible ni cubre un sistema real de inversión. La evidencia respalda el recorrido didáctico y la conservación de los comportamientos comprobados durante la extracción.
