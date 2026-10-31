# Validación de la versión simplificada de Kata Zero

Fecha: 31 de octubre de 2026. Plataforma: macOS aarch64. No se verificó ejecución desde el IDE ni en Windows.

## Entorno

SDKMAN `25.0.5.0+8-zulu`, proveedor Azul Systems, Inc., runtime 25.0.5+8-LTS. Maven 3.10.0 mediante Wrapper 3.3.4; Compiler 3.16.0; Surefire 3.6.1; JUnit Jupiter 6.1.3 en after/02. No se cambió el JDK global.

Comando reproducible desde la raíz: `python3 scripts/verify-kata-zero.py`. El script comprueba el build exacto y ejecuta Maven con su JAVA_HOME y PATH.

## Construcción final

`./mvnw -B -ntp clean verify`: BUILD SUCCESS en las tres etapas y el agregador. after/02 ejecutó **1 prueba, 0 fallas, 0 errores, 0 omitidas**. Las primeras dos etapas compilan y empaquetan sin pruebas JUnit; conservan el defecto docente intencional.

## Primera prueba y corrección

El estado `kata-zero-v3-first-test-red` usa la conversión a int y falla con `expected: <-3.3333> but was: <-4.0000>`. Después se corrige el calculador sin cambiar la prueba. La versión final pasa.

El script reproduce la falla copiando after/02 a una carpeta temporal y sustituyendo solamente su calculador por el de after/01. No modifica los originales ni deja fallando la versión entregada.

## Verificación de consola

Cuatro recorridos por las tres fotografías, con salida idéntica y resultados esperados:

1. Consultar, calcular y consultar de nuevo: vender 2 META, comprar 2 AAPL, posiciones intactas.
2. Calcular dos veces: el plan no muta la cuenta.
3. Opción desconocida: mensaje de opción inválida y salida normal.
4. Fin de entrada: salida normal.

Tres ejecuciones adicionales usan copias compiladas con Maven cambiando solo el primer precio de 100.00 a 150.00. before y after/01 coinciden en el defecto: vender 4.0000 META. after/02 propone 3.3333; las demás líneas coinciden, incluida la compra de 5.0000 AAPL. El total mostrado es 2500.00 USD.

Resultado: **15 ejecuciones de consola** más la reproducción de la prueba roja y la prueba verde del reactor. Main es idéntico byte a byte entre las carpetas after; el calculador cambia explícitamente para corregir el defecto.

La validación anterior de 36 ejecuciones corresponde a la versión extensa y se conserva en Git. No describe este menú simplificado. Esta evidencia tampoco demuestra corrección para toda entrada posible ni funcionamiento de una plataforma real de inversión.
