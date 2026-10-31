# Después 2: primera prueba y corrección

Se agrega JUnit 6.1.3 y una sola comprobación: con META a 150 USD, total de cuenta 2500 USD y objetivo 40%, proponer una venta de 3.3333 META.

Desde la raíz, después de `sdk env`:

```sh
./mvnw -f kata-zero/after/02-first-test/pom.xml test
./mvnw -q -f kata-zero/after/02-first-test/pom.xml compile exec:java
```

La prueba pasó después de conservar la fracción y redondear una sola vez la orden. Main es idéntico a after/01; el calculador tiene una corrección explícita. El ejemplo inicial sigue dando vender 2 y comprar 2.

El estado fallido está guardado en la etiqueta `kata-zero-v3-first-test-red`. Allí la misma prueba espera -3.3333 y obtiene -4.0000. La versión actual debe terminar en verde. No cambiar el esperado para acomodarlo al resultado defectuoso.

Para reproducir rojo sin cambiar de revisión, sustituir temporalmente el calculador por el de after/01, ejecutar la prueba y restaurar el archivo corregido. El script de preparación lo hace en una copia temporal.
