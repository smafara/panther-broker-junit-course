# Referencia de Kata Zero

Referencia principal: repositorio local `fintual-kata`, revisión `8e9dc92` (Final transcript), consultado el 31 de octubre de 2026. Es una solución C# 14/.NET 10 a una kata de rebalanceo. La carpeta no forma parte del repositorio del curso y permanece sin cambios.

Archivos consultados: `README.md`, `DECISIONS.md`, `src/PortfolioRebalancing/Portfolio.cs` y `CLAUDE.md`. El acuerdo de trabajo de ese repositorio corresponde a aquella entrega; aquí se aplica la instrucción actual de implementar material Java.

Se toma como referencia el problema, no se copia una implementación Java preexistente: valorar posiciones, comparar con una distribución objetivo y proponer compras/ventas fraccionadas. Ejemplo compartido: 10 META a 500 USD, 5 AAPL a 200 USD; objetivo 40/60; vender 5.2 META y comprar 13 AAPL.

| Aspecto | Referencia C# | Kata Zero |
|---|---|---|
| Entrada | Biblioteca y CLI JSON | Menú println y BufferedReader |
| Diseño | Stock, Portfolio y Order | Todo en main; después se extrae una fórmula |
| Números | decimal | BigDecimal construido con cadenas |
| Cantidad de orden | Cuatro decimales, ToEven | Cuatro decimales, HALF_EVEN |
| Distribución | Pesos positivos de instrumentos objetivo | Arreglo fijo con pesos de 0 a 1; cero excluye el instrumento |
| Ejecución | Apply separado | Solo plan; no ejecuta |
| Cobertura | Suite completa | Primera prueba deliberadamente pequeña |

Los precios y la cuenta son ficticios y no se consultan cotizaciones reales. No se atribuyen las reglas del ejercicio a Fintual o GBM.
