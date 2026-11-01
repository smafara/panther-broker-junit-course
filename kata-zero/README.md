# Kata Zero — Un cambio que parecía funcionar

Introducción de 7–8 minutos al curso. Primero contamos una historia; la estructura de JUnit, AAA y las metodologías se enseñan después.

## Siete momentos

1. Un programa calcula compras y ventas de acciones completas.
2. El requisito cambia: permitir cantidades fraccionadas.
3. Se cambian dos variables de int a double y se repite el ejemplo manual; parece funcionar.
4. Otros datos revelan una cantidad incorrecta.
5. Introducimos las pruebas unitarias como expectativas ejecutables.
6. Mostramos dos casos originales verdes, el nuevo caso rojo y los tres verdes después de corregir.
7. Presentamos lo que se aprenderá durante el curso.

## Fotografías Maven

| Carpeta | Contenido |
|---|---|
| [before](before/README.md) | Programa con resultados enteros, todo en main |
| [after/01-naive-fractions](after/01-naive-fractions/README.md) | Solo las variables de resultado cambian a double |
| [after/02-first-test](after/02-first-test/README.md) | Cálculo separado para probarlo, tres casos y división corregida |

El total, el valor objetivo y los precios siguen siendo int en este ejercicio. Asignar a double el resultado de una división entre int no recupera la fracción. Esto es truncamiento por división entera, no un error de representación binaria de double.

Datos iniciales: 10 META y 10 AAPL, ambas a 100 USD, objetivo ingresado 40/60. Venta de 2 META y compra de 2 AAPL. Nuevos datos: solo META pasa a 150 USD; total 2500 USD; objetivo META 1000 USD; debe vender aproximadamente 3.333333, pero la adaptación ingenua vende 4.

## Ejecutar

Desde la raíz con SDKMAN y el JDK exacto:

```sh
sdk env
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
./mvnw -q -f kata-zero/after/01-naive-fractions/pom.xml compile exec:java
./mvnw -f kata-zero/after/02-first-test/pom.xml test
./mvnw clean verify
python3 scripts/verify-kata-zero.py
```

Se usa Zulu `25.0.5.0+8-zulu` y Maven Wrapper 3.10.0. En Windows nativo usar mvnw.cmd y JAVA_HOME al mismo build; SDKMAN se puede usar en WSL. Seleccionar también ese JDK en el IDE.

El menú permite ver la cuenta, calcular y salir. Al calcular, se solicita un porcentaje entero entre 0 y 100 para cada acción; los objetivos deben sumar 100%. Por ejemplo, escribir 40 y después 60. Para cambiar el precio, editar `int[] prices = {100, 100}` a `{150, 100}` en una copia y recompilar. El plan no aplica operaciones.

La corrección final usa `targetValue / (double) price`. El alcance son estos datos preparados y una aproximación numérica; no implementa un intermediario real, precisión monetaria general, efectivo, comisiones o impuestos. BigDecimal se estudia después.

## Pruebas y capturas

OriginalExamplesTest tiene dos casos del ejemplo habitual. FractionalSharesTest agrega el nuevo precio. Tener solo las dos primeras pruebas no detectaría el defecto: la selección de ejemplos importa.

La etiqueta `kata-zero-v4-first-test-red` conserva la suite ampliada fallida; `kata-zero-v4-fixed` conserva la corrección sin cambiar las expectativas. Los estados anteriores se conservan como antecedentes.

Para regenerar las imágenes desde ejecuciones reales:

```sh
python3 -m venv /tmp/panther-broker-captures
/tmp/panther-broker-captures/bin/pip install -r scripts/requirements-captures.txt
/tmp/panther-broker-captures/bin/python scripts/verify-kata-zero.py --captures
```

El script usa el JDK exacto, verifica el reactor, ejecuta 27 recorridos de consola y reproduce verde/rojo/verde. Las imágenes son representaciones de extractos reales, con texto, SVG y manifiesto de procedencia; no son fotografías de una ventana de terminal.

## Material del video

- [Deck interactivo](../presentation/intro-junit-kata-zero/README.md).
- [Guion en siete momentos](docs/GUION.md).
- [Evolución](docs/EVOLUCION.md).
- [Validación](docs/VALIDACION.md).
- [Referencia](docs/REFERENCIAS.md).
- [Decisiones e historia de alternativas](../DECISIONS.md).
