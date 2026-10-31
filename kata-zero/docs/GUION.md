# Guion de Kata Zero y material para presentación

Duración orientativa: 20 minutos. Idioma: español de México. Audiencia: estudiantes que ya hicieron programas de consola en Java y todavía no trabajan habitualmente con pruebas automatizadas.

## Mensaje central

«Si para comprobar una fórmula tengo que abrir el programa, navegar un menú y revisar varios números, verificar un cambio se vuelve tardado. Podemos separar un cálculo pequeño y pedirle a una prueba que compruebe el resultado por nosotros».

No presentar el código inicial como motivo de burla: el menú resuelve una necesidad y es una experiencia familiar. El problema aparece cuando hay que verificarlo muchas veces.

## Preparación antes de grabar

1. Ejecutar `sdk env` en la raíz y mostrar Zulu 25.0.5+8 en `java -version` y el mismo JDK en `./mvnw -version`.
2. Ejecutar `./mvnw clean verify` para descargar dependencias antes de grabar.
3. Abrir las tres carpetas en pestañas diferenciadas. No ejecutar las tres Main simultáneamente.
4. Tener a mano el ejemplo calculado en EVOLUCION.md y los archivos samples.
5. Aumentar tamaño de letra y ocultar paneles que no se usarán. Mantener visibles el método y el resultado de la prueba.

## 0:00–2:00 — El problema

Mostrar una tabla: META 10 acciones a 500 USD; AAPL 5 acciones a 200 USD. Aclarar que se permiten fracciones: 0.5 representa media acción. El valor total es 6000 USD. Queremos 40% META y 60% AAPL.

Preguntar para que el espectador lo piense: «¿Qué venderías y qué comprarías?». Pausar unos segundos. Mostrar el resultado a mano: META debe bajar a 4.8, AAPL debe subir a 18. Vender 5.2 y comprar 13.

## 2:00–6:00 — Resolverlo como programa de consola

Abrir before/Main.java. Mostrar BufferedReader, los arreglos y el ciclo del menú. Ejecutar `./mvnw -q -f kata-zero/before/pom.xml compile exec:java`.

Teclear `1`, luego `4`, luego `1`. Comparar el plan con la tabla y confirmar que consultar el plan no ejecutó operaciones. Cambiar precio de META a 400 mediante la opción 2 y volver a 4: vender 5 META y comprar 10 AAPL.

Narración: «Funciona con los ejemplos que acabamos de revisar. Si cambio una fórmula, tengo que repetir estas entradas y volver a comparar los números».

## 6:00–9:00 — Dónde está la dificultad

Señalar las dos copias de la fórmula: ventas y compras. Mostrar cómo el cálculo está rodeado de lectura, formato y ramas del menú. Explicar por qué capturar toda la consola sería un inicio incómodo para probar una operación matemática.

No aprovechar este momento para renombrar todo o diseñar Stock y Portfolio. Esa sería otra clase. La meta es un cambio que pueda verse y entenderse completo.

## 9:00–12:00 — Una extracción pequeña

Pasar a after/01-small-refactor. Extraer o reproducir en vivo `RebalanceCalculator.quantityToTrade`, conservando exactamente la fórmula y el límite de venta. Reemplazar las dos copias en main por llamadas al método.

Explicar sus cuatro entradas: valor total, proporción objetivo, precio y cantidad actual. Salida: cantidad con signo; negativo vende, positivo compra. La consola sigue siendo imperfecta, pero el cálculo ya no necesita teclado ni pantalla.

Ejecutar de nuevo el ejemplo inicial y comprobar la misma salida. Esto es una comparación manual; no afirmar que ya existe una suite de regresión.

## 12:00–16:00 — La primera prueba

Pasar a after/02-first-test. Mostrar solo la dependencia JUnit con alcance test y la carpeta src/test/java. Dejar la arquitectura de Platform/Jupiter y el detalle del BOM para la siguiente lección.

Escribir @Test y @DisplayName. Separar Preparar, Ejecutar y Comprobar con los comentarios existentes. Usar literales calculados a mano: -5.2000 y 13.0000. Ejecutar `./mvnw -f kata-zero/after/02-first-test/pom.xml test`.

Narración: «La prueba repite la pregunta sin abrir el menú. Una comprobación compara lo que esperábamos con lo que realmente devolvió el método».

Explicar brevemente que BigDecimal.equals comprueba también decimales representados: aquí la escala cuatro es parte del resultado. No convertir esta explicación en una clase completa de precisión financiera.

## 16:00–18:00 — Verla fallar y leer el resultado

Cambiar temporalmente subtract por add en el método extraído. Ejecutar la prueba. Leer expected -5.2000 y actual 14.8000, y abrir la línea señalada. Relacionar el signo incorrecto con una venta que terminó convertida en compra.

Restaurar subtract y volver a ejecutar. El repositorio entregado debe terminar en verde. No cambiar el valor esperado para acomodarlo al defecto.

No presentar este recorrido como TDD: primero existía el programa y después se agregó una prueba. El TDD se estudiará más adelante.

## 18:00–20:00 — Qué ganamos y qué falta

Mostrar las responsabilidades que permanecen en main. La prueba todavía no comprueba el total de la cuenta, todos los datos inválidos ni todos los redondeos. Es un comienzo que permite comprobar una regla importante de forma repetible.

Presentar el reto opcional de la cuenta ya balanceada. El criterio de éxito es cero en ambas órdenes, con cuatro decimales; no se pide entregar evidencia ni obtener una calificación.

## Propuesta de diapositivas

| Diapositiva | Contenido | Evidencia o demostración |
|---|---|---|
| 1 | Problema: rebalancear una cuenta | Datos y objetivo 40/60 |
| 2 | Resultado esperado a mano | Tabla de EVOLUCION.md |
| 3 | Verificar desde el menú | Captura del plan en before |
| 4 | Cálculo mezclado con consola | Dos copias de la fórmula |
| 5 | Una entrada y una salida controlables | Método extraído y sus parámetros |
| 6 | Primera prueba | Preparar–Ejecutar–Comprobar |
| 7 | Una falla útil | Expected y actual del defecto temporal |
| 8 | Reto y siguiente paso | Cuenta ya balanceada y estructura de JUnit |

Usar capturas obtenidas de la versión validada; no inventar una interfaz gráfica ni sugerir que se operó dinero real.
