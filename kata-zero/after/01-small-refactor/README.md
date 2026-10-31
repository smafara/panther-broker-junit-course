# Después 1: extraer sin corregir

Se extraen las dos líneas que calculan la cantidad a negociar a RebalanceCalculator.quantityToTrade. El defecto se conserva. La lectura, el estado y la impresión siguen en main.

Desde la raíz, después de `sdk env`:

```sh
./mvnw -q -f kata-zero/after/01-small-refactor/pom.xml compile exec:java
```

El ejemplo inicial sigue proponiendo vender 2 META y comprar 2 AAPL. Con META a 150 USD conserva el resultado defectuoso de before. Esta extracción permite probar la fórmula sin navegar por el menú; no la vuelve correcta por sí misma.
