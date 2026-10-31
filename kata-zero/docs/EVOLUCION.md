# Qué cambió y por qué

## Problema y contrato

Una cuenta contiene 10 META y 10 AAPL. El objetivo es 40% del valor en META y 60% en AAPL. Los precios son datos ficticios en USD. El programa propone compras y ventas sin modificar las posiciones.

Solo se usan los datos válidos preparados: cantidades de hasta cuatro decimales, precios positivos y proporciones que suman 1. No hay edición interactiva, efectivo, comisiones, impuestos, ejecución ni cotizaciones reales. Las órdenes finales se redondean a cuatro decimales con HALF_EVEN; puede quedar un residuo pequeño por redondeo. No modelamos su liquidación.

## Dos ejemplos que explican el defecto

| Concepto | Ejemplo habitual | Nuevo precio |
|---|---:|---:|
| Precio META | 100 USD | 150 USD |
| Precio AAPL | 100 USD | 100 USD |
| Cantidad de cada una | 10 | 10 |
| Valor de la cuenta | 2000 USD | 2500 USD |
| Valor objetivo META, 40% | 800 USD | 1000 USD |
| Cantidad objetivo META | 8 | 6.666666... |
| Orden correcta META | -2.0000 | -3.3333 |
| Orden con el defecto | -2.0000 | -4.0000 |
| Orden correcta AAPL | +2.0000 | +5.0000 |

En el nuevo escenario, truncar el objetivo a seis acciones propone vender cuatro. El error principal equivale a aproximadamente 100 USD vendidos de más, no a una diezmilésima perdida. No confundirlo con el residuo normal de redondeo al representar una fracción periódica.

## Antes: todo en main

El main original de esta revisión tiene 52 líneas, dos instrumentos y tres opciones. Mezcla menú, BufferedReader, arreglos paralelos, cálculo e impresión. El total aparece en dos ramas. El desorden es pequeño y deliberado.

La historia del ejercicio es una adaptación de acciones completas a fraccionadas: quedó una variable `int target`. La operación decimal se convierte con intValue, perdiendo la parte fraccionaria. El primer ejemplo no lo revela porque sus cantidades objetivo ya son enteras.

## Después 1: extraer sin corregir

RebalanceCalculator.quantityToTrade recibe total, peso objetivo, precio y posición actual. Devuelve una cantidad firmada: negativa para vender, positiva para comprar. Se extraen las mismas operaciones, incluida la conversión defectuosa. Repetir ambos escenarios conserva la salida de before.

No se introducen modelos, mocks, validaciones generales ni una arquitectura de producción. La extracción solo permite hacer una pregunta al cálculo sin navegar por el menú.

## Primera prueba: rojo

La prueba de after/02 usa el nuevo precio y comprueba únicamente META. Preparar: cuenta de 2500 USD. Ejecutar: objetivo .40, precio 150, posición 10. Comprobar: -3.3333, calculado a mano.

En la etiqueta `kata-zero-v3-first-test-red` obtiene -4.0000 y falla. La prueba no copia la fórmula de producción ni falla solamente por escala de BigDecimal. Introduce @Test, @DisplayName y assertEquals con una sola comprobación.

## Corrección: verde

Se calcula el valor objetivo menos el valor actual y se divide por el precio, conservando decimales y redondeando una vez la orden final. La prueba no cambia. Main sigue idéntico entre las carpetas after; el calculador cambia expresamente para corregir el defecto.

El ejemplo habitual mantiene vender 2 META y comprar 2 AAPL; el nuevo escenario ahora vende 3.3333 META. Esto es una prueba de regresión añadida a código existente, no un recorrido de TDD.

## Límites de la evidencia

La primera prueba no cubre el total calculado en main, la consola ni todos los redondeos. El script de preparación agrega comparaciones del material, pero no se presenta como parte de la primera prueba del estudiante.

Los antecedentes de 140 líneas y del defecto de dos decimales se conservan en Git y DECISIONS.md. Esta revisión sustituye sus ejemplos y comandos de menú.
