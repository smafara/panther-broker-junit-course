# Registro de cambios

## 2026-10-31 — Preparación de Kata Zero

- Se conserva el temario previo en español y su investigación en inglés.
- Se inicializa Git en la raíz y se excluye el repositorio independiente de referencia.
- Se registra el nuevo requisito: comenzar por rebalanceo manual en consola, extraer un cálculo y escribir la primera prueba.
- Se fija Zulu `25.0.5.0+8-zulu` de SDKMAN por instrucción expresa del usuario, sin cambiar su JDK global.
- Se implementan tres proyectos Maven independientes: before, after/01-small-refactor y after/02-first-test.
- Se agrega Maven Wrapper 3.3.4 con Maven 3.10.0 y un agregador raíz.
- Se verifica una prueba JUnit 6.1.3, su falla ante una suma incorrecta y su éxito tras restaurar la resta.
- Se comparan 12 escenarios de consola en las tres etapas: 36 ejecuciones con resultados esperados y salidas coincidentes.
- Se agregan guion de 20 minutos, propuesta de diapositivas, explicación de cambios, referencia, comandos y validación.
- Se etiquetan los avances y se integra Kata Zero como introducción al temario.
