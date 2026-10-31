# Antes: probar navegando por el menú

Toda la lógica está en Main.main: menú, lectura, validación, estado, cálculos y presentación. No hay pruebas automatizadas. El desorden es deliberado para la lección.

Desde la raíz del repositorio:

```sh
sdk env
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
```

En Windows usar `mvnw.cmd`. Desde esta carpeta, con Maven instalado y el mismo JDK: `mvn compile exec:java`.

Entra a la opción 4. Con los datos iniciales debes ver VENDER META 5.2000 y COMPRAR AAPL 13.0000. Vuelve a la opción 1: la cuenta sigue teniendo 10 META y 5 AAPL. El programa propone, no ejecuta.

Después cambia un precio y repite. Observa cuánto trabajo exige verificar los resultados manualmente. No añadas clases ni pruebas todavía.
