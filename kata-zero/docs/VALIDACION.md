# Validación de la introducción narrativa

31 de octubre de 2026, macOS aarch64. JDK SDKMAN `25.0.5.0+8-zulu`, Azul 25.0.5+8-LTS. Maven 3.10.0 y JUnit Jupiter 6.1.3. No se cambió el JDK global.

## Resultado

`python3 scripts/verify-kata-zero.py` construye el reactor completo y ejecuta 27 recorridos de consola. La versión final pasa tres pruebas sin errores ni omisiones.

También se comprueban objetivos alternativos 50/50 y 30/70, y se rechazan valores no numéricos o que no suman 100. Se comprobaron los cuatro recorridos habituales —consulta/plan sin mutación, plan repetido, opción inválida y fin de entrada— en tres etapas. Tres copias adicionales usan META a 150 USD: before vende 4, la adaptación double vende 4.0 y la versión corregida vende 3.333333333333333.

En una copia temporal del calculador defectuoso:

- OriginalExamplesTest: 2 pruebas, 0 fallas; BUILD SUCCESS.
- Suite completa: 3 pruebas, 1 falla; esperado -3.333333, obtenido -4.0; BUILD FAILURE.
- Calculador corregido, mismas expectativas: 3 pruebas, 0 fallas; BUILD SUCCESS.

La falla detectada es división entera previa a la asignación double. No se atribuye a IEEE 754. Los datos están preparados y no se afirma corrección para todo dominio financiero.

## Capturas

El mismo script con `--captures` genera cinco PNG y SVG desde extractos reales, junto con .txt y manifest.json. Se requiere PyMuPDF de scripts/requirements-captures.txt. Los encabezados y colores son de presentación; los resultados, cantidades y conteos proceden de las ejecuciones verificadas. No se fotografió una ventana de terminal.

No se verificó Windows ni ejecución desde el IDE. Los conteos y fotografías de versiones anteriores se conservan en Git como antecedentes y no describen esta introducción.
