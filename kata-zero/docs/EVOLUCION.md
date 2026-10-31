# Qué cambió y por qué

## Punto de partida

La persona estudiante recibe una cuenta con posiciones, precios conocidos y porcentajes objetivo. Debe producir un plan para acercar el valor de cada posición a su porcentaje. Primero resuelve el problema como suele hacerlo en ejercicios de consola: menú, BufferedReader y comprobación visual.

La primera versión funciona para el alcance definido. El problema docente es el esfuerzo de comprobarla repetidamente y la dificultad de separar entrada, cálculo y salida.

## Antes: el programa manual

`before/src/main/java/mx/serviciosocial/katazero/Main.java` contiene toda la lógica en `public static void main(String[] args)`. Arreglos paralelos representan símbolos, precios, cantidades y pesos. El total se repite en consulta y rebalanceo. La fórmula de orden se repite para imprimir primero ventas y luego compras. Los nombres breves y las ramas del menú dificultan seguir el cálculo.

Se mantiene una validación básica de precio positivo, cantidad no negativa y proporciones que suman 1. El desorden no consiste en inventar errores aritméticos ocultos ni provocar fallas evitables al introducir datos.

La opción 4 solo imprime un plan. Volver a la opción 1 permite comprobar que no cambió la cuenta.

## Resultado esperado calculado a mano

| Concepto | META | AAPL |
|---|---:|---:|
| Precio USD | 500 | 200 |
| Cantidad actual | 10 | 5 |
| Valor actual USD | 5000 | 1000 |
| Porcentaje objetivo | 40% | 60% |
| Valor objetivo USD, sobre 6000 | 2400 | 3600 |
| Cantidad objetivo | 4.8 | 18 |
| Cambio de cantidad | -5.2 | +13 |

Un valor negativo significa vender; uno positivo, comprar. NVDA está en el catálogo con cantidad y objetivo cero, por lo que no produce orden. Vender libera 2600 USD y comprar requiere 2600 USD en este ejemplo exacto; no generalizar esa igualdad a casos con redondeo.

## Alcance y limitaciones

Una cuenta, tres instrumentos fijos y una moneda (USD). Sin efectivo, comisiones, impuestos, red de mercado ni ejecución. Las proporciones deben sumar exactamente 1. Cero permite retirar un instrumento de la distribución. Las órdenes se redondean a cuatro decimales con HALF_EVEN; una venta se limita a las acciones disponibles. El redondeo puede dejar una diferencia entre valor de compras y ventas.

El programa conserva la estructura imperfecta para mostrar un cambio pequeño. No representa la arquitectura final del curso ni una plataforma de inversión real.

## Después 1: extraer sin rediseñar

En `after/01-small-refactor` se extrae la fórmula repetida a `RebalanceCalculator.quantityToTrade`. La fórmula calcula `(total × peso - cantidadActual × precio) / precio`, redondea una vez y limita una venta a lo disponible. Las dos ramas de impresión llaman al mismo método. No se agregan validaciones nuevas ni se cambian tipos numéricos.

El resto de main sigue igual: nombres breves, arreglos paralelos, lectura y presentación mezcladas. Este paso no pretende terminar la refactorización. Solo permite preguntar por un resultado sin simular teclas.

Para comparar: `git diff --no-index kata-zero/before/src/main/java kata-zero/after/01-small-refactor/src/main/java`. Un código de salida 1 en ese comando significa que encontró diferencias.
