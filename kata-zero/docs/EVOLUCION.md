# Evolución vigente: int → double no basta

## Qué cambia en esta introducción

El usuario redujo el alcance a una historia para motivar el curso. Los primeros diseños —140 líneas, extracción guiada, precisión BigDecimal e intValue— permanecen en Git y en DECISIONS.md. No describen el video actual.

## 1. El programa original

Datos iniciales fijos: diez META, diez AAPL, ambas a 100 USD. La persona ingresa los objetivos; el ejemplo usa 40/60. Arreglos y resultados int, menú con println y BufferedReader. Calcula un plan; no ejecuta operaciones. El caso manual da vender 2 y comprar 2.

## 2. El cambio ingenuo

El nuevo requisito permite fracciones. La persona cambia solo targetShares y difference a double. Antes y después, `targetValue / price` divide dos int. En el ejemplo habitual 800/100 y 1200/100 son divisiones exactas, así que el resultado parece correcto.

## 3. Los datos que distinguen comportamientos

| Concepto | Caso habitual | META a 150 USD |
|---|---:|---:|
| Valor total | 2000 USD | 2500 USD |
| Objetivo META, 40% | 800 USD | 1000 USD |
| Cantidad objetivo exacta | 8 | 6.666666… |
| Cantidad obtenida por división entera | 8 | 6 |
| Venta correcta | 2 | 3.333333… |
| Venta del programa adaptado | 2.0 | 4.0 |

El fallo sucede antes de la asignación a double. No es una pequeña discrepancia binaria ni el residuo normal de representar una fracción periódica.

## 4. La suite

Dos pruebas automatizan los ejemplos originales y pasan incluso con el defecto. Una tercera expresa el nuevo caso y falla. Conservar solo las primeras no habría encontrado el problema.

Se usa una tolerancia explícita para comparar double, sin enseñar toda la API de assertions. Se proporciona el esperado calculado a mano. No se presenta este recorrido como TDD: el código existía antes de la prueba.

## 5. Corrección y alcance

Promover un operando mediante `(double) price` permite la división fraccionaria. La suite mantiene sus tres expectativas y pasa. El cálculo está en un método desde la versión original; se prueba directamente.

El ejemplo usa precios enteros y valores preparados. No resuelve toda la precisión monetaria ni cualquier entrada de un sistema financiero. La elección de casos, BigDecimal, estructura de pruebas y metodologías se estudian en el curso.

Las capturas son extractos reales ejecutados con Zulu 25.0.5+8, renderizados para legibilidad. El texto y manifiesto permiten comprobar su procedencia.
