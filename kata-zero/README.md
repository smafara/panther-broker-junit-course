# Kata Zero — Del menú de consola a la primera prueba

**Pregunta inicial:** tengo una cuenta con acciones, sus precios y una distribución objetivo; ¿qué necesito vender y comprar para rebalancearla?

Este episodio introductorio muestra una forma familiar de programar: todo en main, menús con println, lectura con BufferedReader y comprobación por ensayo y error. Después extraemos un solo cálculo y escribimos la primera prueba. El objetivo es sentir la necesidad de verificar automáticamente, antes de estudiar más anotaciones de JUnit.

## Recorrido

| Etapa | Carpeta | Qué aparece |
|---|---|---|
| Antes | [before](before/README.md) | Todo dentro de main; verificación manual |
| Después 1 | [after/01-small-refactor](after/01-small-refactor/README.md) | Se extrae la cantidad a negociar |
| Después 2 | [after/02-first-test](after/02-first-test/README.md) | Mismo código de producción y primera prueba JUnit |

Cada carpeta tiene su propio POM y .sdkmanrc. No es necesario instalar ni ejecutar la solución C# de referencia.

## Entorno

Desde la raíz del repositorio, con SDKMAN instalado:

```sh
sdk install java 25.0.5.0+8-zulu  # solo si no está instalado
sdk env
java -version
./mvnw -version
```

El wrapper usa Maven 3.10.0. La primera ejecución necesita conexión para descargar Maven y dependencias. El POM exige Java 25.0.5 de Azul y .sdkmanrc identifica el build exacto del curso. En el IDE seleccionar `~/.sdkman/candidates/java/25.0.5.0+8-zulu` como JDK del proyecto y de Maven.

En Windows, si se trabaja mediante WSL, ejecutar SDKMAN en WSL. En una terminal nativa usar `mvnw.cmd` con JAVA_HOME apuntando al mismo build de Zulu; SDKMAN no administra directamente un JDK nativo de Windows.

## Ejecutar las tres fotografías

Desde la raíz, elegir una etapa:

```sh
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
./mvnw -q -f kata-zero/after/01-small-refactor/pom.xml compile exec:java
./mvnw -q -f kata-zero/after/02-first-test/pom.xml compile exec:java
```

La opción 4 propone vender 5.2000 META y comprar 13.0000 AAPL. La opción 1 confirma que las posiciones siguen siendo 10 META y 5 AAPL. Todo está expresado en USD y los precios son ficticios.

Entradas repetibles para preparar la grabación:

```sh
./mvnw -q -f kata-zero/before/pom.xml compile exec:java < kata-zero/samples/recorrido-inicial.txt
./mvnw -q -f kata-zero/before/pom.xml compile exec:java < kata-zero/samples/cambio-precio.txt
./mvnw -q -f kata-zero/before/pom.xml compile exec:java < kata-zero/samples/ya-balanceada.txt
```

## Ejecutar la primera prueba

```sh
./mvnw -f kata-zero/after/02-first-test/pom.xml test
```

Resultado esperado: 1 prueba, 0 fallas, 0 errores. Las otras dos etapas no tienen pruebas; que Maven termine correctamente allí solo demuestra compilación y empaquetado, no validación automática del comportamiento.

Para compilar todas las etapas y ejecutar la prueba desde el agregador:

```sh
./mvnw clean verify
```

El equipo que prepara el curso también puede ejecutar `python3 scripts/verify-kata-zero.py`. Selecciona el JDK exacto de SDKMAN, ejecuta Maven y compara 12 escenarios de consola entre las tres etapas. Python no es requisito para ver ni seguir la lección.

## Documentos para producir la clase

- [Evolución del código y resultados a mano](docs/EVOLUCION.md).
- [Guion y propuesta de diapositivas](docs/GUION.md).
- [Validación efectuada](docs/VALIDACION.md).
- [Referencia consultada y diferencias](docs/REFERENCIAS.md).
- [Decisiones del curso](../DECISIONS.md).

## Historial Git

Las etiquetas `kata-zero-before`, `kata-zero-refactor` y `kata-zero-first-test` identifican los avances. `kata-zero-ready` identifica el material terminado y validado. Las carpetas permiten comparar sin cambiar de revisión.

```sh
git log --oneline --decorate
git diff kata-zero-before kata-zero-refactor
git diff --no-index kata-zero/after/01-small-refactor/src/main/java kata-zero/after/02-first-test/src/main/java
```

El último comando no debe encontrar diferencias: la primera prueba se agregó sin cambiar producción.

## Reto opcional

Con una cuenta de 4.8 META y 18 AAPL a los precios iniciales, calcula a mano las cantidades a negociar. Agrega una prueba que espere cero con escala de cuatro decimales para ambos instrumentos. Usa únicamente @Test y assertEquals.

Antes de hacerlo en JUnit, puedes usar `samples/ya-balanceada.txt` para comprobar visualmente el mismo caso. La siguiente lección profundiza en la estructura de la prueba y cómo interpretar sus resultados.
