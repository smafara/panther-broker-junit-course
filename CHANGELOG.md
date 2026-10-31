# Registro de cambios

## 2026-10-31 — Panther Broker y títulos limpios

- Se agrega el código original y su propósito inmediatamente después de la portada.
- El deck pasa a 13 diapositivas y se titula «Introducción a JUnit».
- Se eliminan subtítulo, etiquetas complementarias, antetítulos y duraciones del deck y de sus notas.
- Se registra esa regla para presentaciones futuras en presentation/AGENTS.md.
- El proyecto adopta Panther Broker, referencia elegida por el usuario a la UAM Azcapotzalco; se actualizan programa, temario y material vigente.

## 2026-10-31 — Introducción reducida a una historia

- Se adopta la secuencia de siete momentos solicitada y se reduce el deck a 12 diapositivas, 7–8 minutos.
- Se sustituye BigDecimal/intValue por el programa entero y su cambio ingenuo a double que conserva división entera.
- Se conserva un ejemplo original que pasa y otro fraccionario que descubre la falla.
- Se verifican dos pruebas verdes con defecto, tres con una falla y las tres verdes tras corregir.
- Se generan cinco imágenes de salidas reales con extractos y procedencia, y se actualizan guion, temario y decisiones.

## 2026-10-31 — Presentación del video introductorio

- Se delega la creación del deck a un subagente por solicitud del usuario.
- Se acota la propuesta inicial del módulo 1 a «Introducción a JUnit con Kata Zero».
- Se crean 19 diapositivas Slidev en español con notas, tema oscuro, Shiki, focos de código, Mermaid y magic-move.
- Se agregan instalación reproducible con npm, exportación PDF y comprobación en navegador.
- Se enlaza el deck desde el curso y Kata Zero y se registra la decisión de usar Node para la presentación, conservando Maven para Java.

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

## 2026-10-31 — Simplificación revisada en consejo

- Se reduce main de 140 a 52 líneas, con dos instrumentos y opciones de ver, calcular y salir.
- Se eliminan edición de datos, búsqueda de símbolos y validación financiera interactiva.
- Se registra y descarta como versión vigente el experimento de precisión de dos decimales por resultar demasiado sutil.
- Se adopta el supuesto heredado de acciones enteras: un int pierde la fracción de la cantidad objetivo.
- El ejemplo inicial vende 2 META y compra 2 AAPL; el cambio de META a 150 USD exige vender 3.3333, pero el defecto vende 4.
- Se preserva el estado rojo en `kata-zero-v3-first-test-red` y la corrección en un commit separado con la misma prueba.
- Se actualizan guion, evolución, revisión colegiada y validación con 15 ejecuciones de consola y reproducción rojo/verde en copias temporales.
- Se conserva Zulu `25.0.5.0+8-zulu` para toda compilación y ejecución.
