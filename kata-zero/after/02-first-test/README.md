# Después 2: la primera prueba

El código de producción es idéntico al de after/01-small-refactor. Solo se agregan JUnit 6.1.3 al POM y RebalanceCalculatorTest.

Desde la raíz:

```sh
sdk env
./mvnw -f kata-zero/after/02-first-test/pom.xml test
./mvnw -q -f kata-zero/after/02-first-test/pom.xml compile exec:java
```

En Windows usar mvnw.cmd. Desde esta carpeta: `mvn test` con el JDK de .sdkmanrc.

La prueba expresa un escenario con dos comprobaciones: vender 5.2000 META y comprar 13.0000 AAPL para llegar a 40/60. No lee el teclado ni inspecciona texto de consola.

Para mostrar una falla, cambia temporalmente `.subtract(currentQuantity.multiply(price))` por `.add(currentQuantity.multiply(price))` en RebalanceCalculator y ejecuta la prueba. Expected será -5.2000; actual, 14.8000. Restaura subtract y vuelve a ejecutar. No guardes el defecto en la versión final.

Esta prueba no cubre todo el programa. Agregar el caso de una cuenta ya balanceada es el reto opcional.
