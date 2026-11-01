# Antes: acciones completas

Programa original con menú y arreglos en main; RebalanceCalculator.quantityToTrade devuelve resultados int. Precios ficticios en USD, diez acciones de cada instrumento y objetivos ingresados por la persona. Por ejemplo, 40/60. El caso preparado propone vender 2 META y comprar 2 AAPL.

Desde la raíz, con `sdk env`:

```sh
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
```

Opciones: 1 consulta, 2 plan y 0 salida. No hay ejecución de operaciones ni pruebas JUnit. Solo se presenta el caso manual preparado; no se afirma que el programa resuelva cualquier distribución de acciones completas.
