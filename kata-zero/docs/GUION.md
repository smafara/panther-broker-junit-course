# Guion de Kata Zero — Una suposición que dejó de cumplirse

Duración orientativa: 15 minutos. Narración en español de México. No se requiere experiencia como inversionista. Dar el cálculo esperado en pantalla; no convertir la primera clase en un acertijo financiero.

## Preparación

Ejecutar `sdk env`, comprobar Zulu 25.0.5+8 y ejecutar `./mvnw clean verify`. Abrir before, after/01 y after/02 en pestañas diferenciadas. El menú actual solo tiene consulta, rebalanceo y salida.

Tener preparada una copia temporal de before con solo el primer precio cambiado de 100.00 a 150.00. No editar ambos precios. El script de validación demuestra esa reproducción sin tocar los originales.

## 0:00–2:00 — Una tarea familiar

«Tenemos una cuenta y queremos proponer qué vender y qué comprar para llegar a 40% META y 60% AAPL. Este programa comenzó pensando en acciones completas; ahora el requisito permite fracciones».

Presentar las 10 acciones de cada instrumento, inicialmente a 100 USD. Explicar que porcentajes se aplican al valor monetario, no al número de acciones. Total 2000 USD, objetivos 800 y 1200 USD: vender 2 META y comprar 2 AAPL.

## 2:00–4:00 — Parece funcionar

Ejecutar before y teclear 1, 2, 1, 0. Comparar con lo calculado a mano. El plan no modifica la cuenta. Mostrar el main de 52 líneas y ubicar lectura, arreglos y fórmula sin explicar cada detalle de BigDecimal.

«Si este es el único ejemplo que revisamos, parece que ya terminamos».

## 4:00–6:00 — Un precio distinto revela el supuesto

«¿Qué pasa si cambia solo el precio de META a 150 USD?» Mostrar la tabla: total 2500 USD, objetivo META 1000 USD, cantidad objetivo 6.6666..., venta de 3.3333 a cuatro decimales.

Ejecutar la copia con el nuevo precio y observar VENDER META 4.0000. No existe un menú para cambiar el precio: el instructor cambia un literal y recompila.

«No desapareció una diezmilésima. Estamos proponiendo vender aproximadamente 100 USD de más».

No señalar todavía la conversión exacta como si el estudiante debiera descubrirla solo; ya hay una diferencia observable que vale la pena comprobar.

## 6:00–8:00 — Hacer una pregunta sin navegar el menú

Extraer las operaciones a RebalanceCalculator.quantityToTrade, conservando el int. Mostrar after/01. Repetir el ejemplo habitual: misma salida. Explicar las cuatro entradas y el significado del signo.

«Extraer el cálculo no corrige automáticamente el comportamiento. Ahora podemos preguntarle directamente cuánto vendería».

## 8:00–11:00 — Primera prueba, primera falla útil

Mostrar la dependencia JUnit con alcance test y src/test/java. Escribir la prueba existente con Preparar–Ejecutar–Comprobar y un solo assertEquals. El esperado -3.3333 proviene de la tabla, no del método.

Con el calculador de after/01, la prueba debe fallar: expected -3.3333, actual -4.0000. Ese estado está en `kata-zero-v3-first-test-red`. Para una grabación continua se puede copiar temporalmente el calculador defectuoso a after/02 y restaurarlo tras el siguiente paso; evitar cambios de revisión con archivos sin guardar.

## 11:00–13:00 — Corregir el supuesto

Señalar intValue: «Se preparó un cálculo decimal, pero esta conversión conservó solo la parte entera. Era una suposición de acciones completas que quedó aquí».

Mostrar el cálculo corregido: conservar decimales, restar el valor actual del objetivo, dividir por el precio y redondear la orden final a cuatro decimales. Ejecutar la misma prueba sin cambiar el esperado: verde.

El nuevo plan propone vender 3.3333 META; quedan 6.6667 a la precisión elegida. Las diferencias mínimas de representar fracciones son un tema posterior, distinto del int.

## 13:00–15:00 — Qué demuestra y qué falta

La prueba permite repetir una pregunta importante sin teclado ni comparación visual. No demuestra que todo el programa sea correcto. No llamar TDD al recorrido: el programa ya existía.

Reto opcional: con el nuevo precio, AAPL requiere 1500 USD, equivalentes a 15 acciones; ya hay 10. Agregar una prueba que espere +5.0000. No requiere entrega ni calificación.

## Diapositivas sugeridas

| Diapositiva | Contenido |
|---|---|
| 1 | Requisito nuevo: permitir fracciones |
| 2 | Ejemplo entero que parece funcionar |
| 3 | Cambio de precio y resultado esperado a mano |
| 4 | Resultado incorrecto: vende cuatro |
| 5 | Extraer sin corregir |
| 6 | Primera prueba: expected y actual |
| 7 | El int heredado y la prueba en verde |
| 8 | Alcance y reto opcional |

La historia y los precios son ficticios. No atribuir el defecto a una plataforma real ni afirmar que se ejecutaron operaciones.
