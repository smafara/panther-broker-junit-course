# Referencia de Kata Zero

Referencia principal: repositorio local `fintual-kata`, revisión `8e9dc92` (Final transcript), consultado el 31 de octubre de 2026. Es una solución C# 14/.NET 10 a una kata de rebalanceo. La carpeta no forma parte del repositorio del curso y permanece sin cambios.

Archivos consultados: `README.md`, `DECISIONS.md`, `src/PortfolioRebalancing/Portfolio.cs` y `CLAUDE.md`. El acuerdo de trabajo de ese repositorio corresponde a aquella entrega; aquí se aplica la instrucción actual de implementar material Java.

Se toma como referencia el problema, no se copia una implementación Java preexistente: valorar posiciones, comparar con una distribución objetivo y proponer compras/ventas fraccionadas. La referencia usa 10 META a 500 USD y 5 AAPL a 200 USD. La versión docente vigente simplifica sus datos a 10 de cada una a 100 USD y cambia META a 150 USD para revelar un supuesto de acciones completas.

| Aspecto | Referencia C# | Kata Zero |
|---|---|---|
| Entrada | Biblioteca y CLI JSON | Menú println y BufferedReader |
| Diseño | Stock, Portfolio y Order | Menú en main y cálculo separado desde la versión original |
| Números | decimal | BigDecimal construido con cadenas |
| Cantidad de orden | Cuatro decimales, ToEven | Cuatro decimales, HALF_EVEN |
| Distribución | Pesos positivos de instrumentos objetivo | Arreglo fijo con pesos de 0 a 1; cero excluye el instrumento |
| Ejecución | Apply separado | Solo plan; no ejecuta |
| Cobertura | Suite completa | Primera prueba deliberadamente pequeña |

Los precios y la cuenta son ficticios y no se consultan cotizaciones reales. No se atribuyen las reglas del ejercicio a Fintual o GBM.

## Revisión narrativa vigente

La introducción actual usa precios y resultados enteros y un cambio ingenuo a double. El uso anterior de BigDecimal, cuatro decimales e intValue en esta kata es un antecedente en Git. Se conserva de la referencia el problema de rebalanceo; no se trasladan todos sus contratos numéricos a este programa introductorio.
