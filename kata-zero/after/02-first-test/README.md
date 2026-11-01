# Después 2: expectativas ejecutables

El cálculo ya existe desde la versión original; aquí se agregan pruebas y se corrige la división.

```sh
./mvnw -f kata-zero/after/02-first-test/pom.xml test
```

Desde la raíz y con el JDK de `sdk env`. Resultado final: tres pruebas, cero fallas. OriginalExamplesTest comprueba vender 2 META y comprar 2 AAPL. FractionalSharesTest comprueba la venta fraccionaria con META a 150 USD usando una tolerancia de 0.000001 para double.

El estado `kata-zero-v4-first-test-red` conserva `targetValue / price` y falla el caso nuevo: esperado -3.333333, obtenido -4.0. La versión actual usa `targetValue / (double) price` y pasa sin cambiar la prueba.

Los dos casos originales también pasan con el defecto. Una suite solo detecta comportamientos expresados por sus casos; no descubre requisitos por sí sola.
