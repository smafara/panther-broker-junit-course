# Después 1: una extracción pequeña

Se extrae la fórmula repetida a RebalanceCalculator.quantityToTrade. Main sigue controlando entrada, validación, estado y presentación. No se introducen pruebas todavía y no se cambia el cálculo.

Desde la raíz:

```sh
sdk env
./mvnw -q -f kata-zero/after/01-small-refactor/pom.xml compile exec:java
```

En Windows usar mvnw.cmd. Desde esta carpeta también se puede ejecutar `mvn compile exec:java` con el JDK indicado en .sdkmanrc.

Repetir las entradas de `kata-zero/samples`. La salida debe coincidir con before. Ya es posible invocar el cálculo sin leer el teclado ni capturar la consola.
