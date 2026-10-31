# Antes: un programa de consola que parece funcionar

Todo está en un main de 52 líneas: menú, lectura con BufferedReader, arreglos paralelos, total repetido, cálculo e impresión. Opciones: 1 ver cuenta, 2 proponer rebalanceo y 0 salir.

Desde la raíz, después de `sdk env`:

```sh
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
```

Caso inicial: 10 META y 10 AAPL a 100 USD cada una, objetivo 40/60. Debe imprimir VENDER META 2.0000 y COMPRAR AAPL 2.0000. Volver a la opción 1 confirma que no se aplicó el plan.

Esta fotografía contiene intencionalmente un defecto del ejercicio. El instructor tiene su explicación en docs/GUION.md; no es una solución financiera terminada. No hay pruebas automatizadas.

Para preparar el segundo escenario, cambiar solo el primer precio de 100.00 a 150.00 y recompilar. No existe una opción de menú para editar precios. Conservar el original para comparar fotografías.
