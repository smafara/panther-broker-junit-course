# Primeros pasos con JUnit

Una lección práctica basada en el cálculo de Panther Broker de Kata Zero.

- **before/**: proyecto Maven con el cálculo corregido, sin JUnit ni pruebas.
- **after/**: el mismo cálculo, JUnit Jupiter y una prueba organizada con Arrange, Act y Assert.
- **presentation/primeros-pasos-junit/**: presentación y notas de grabación.

Seleccionar en SDKMAN el JDK del curso, `25.0.5.0+8-zulu`. Desde la raíz:

```sh
sdk use java 25.0.5.0+8-zulu
./mvnw -f primeros-pasos-junit/before/pom.xml test
./mvnw -f primeros-pasos-junit/after/pom.xml test
```

La primera ejecución compila y no encuentra pruebas. La segunda ejecuta una prueba. Los proyectos fijan JUnit 6.1.3 y Surefire 3.6.1, y se incluyen en el reactor Maven de la raíz. La versión de partida ya tiene configurado Surefire y la propiedad de versión; en el paso final se agrega el BOM, la dependencia y la prueba. Consulte los POM completos, no solo los fragmentos de las diapositivas.

**Práctica opcional:** en una copia de after, escribir otro caso con AAA. La tolerancia del ejemplo sirve para comparar aproximaciones double; el cálculo es una simplificación didáctica, no un motor financiero.
