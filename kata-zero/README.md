# Kata Zero — De un menú de consola a la primera prueba

**Historia del ejercicio:** un programa se escribió suponiendo acciones completas. Al adaptarse para permitir fracciones, quedó una conversión a int en un cálculo intermedio. Un ejemplo con resultados enteros parece funcionar; un cambio de precio revela el defecto.

Es un contexto ficticio para enseñar pruebas; no es un bug atribuido a Fintual o GBM. La kata conserva un main pequeño y desordenado, con println, BufferedReader, arreglos paralelos y cálculos mezclados con presentación.

## Tres proyectos Maven

| Etapa | Carpeta | Estado |
|---|---|---|
| Antes | [before](before/README.md) | Todo en main; defecto inicial |
| Extracción | [after/01-small-refactor](after/01-small-refactor/README.md) | Mismo defecto en un método aislado |
| Primera prueba y corrección | [after/02-first-test](after/02-first-test/README.md) | Una prueba JUnit y cálculo corregido |

No se necesitan la solución C# de referencia ni servicios externos.

## Entorno y ejecución

Usar exactamente Zulu `25.0.5.0+8-zulu` de SDKMAN. Desde la raíz:

```sh
sdk install java 25.0.5.0+8-zulu  # solo si falta
sdk env
./mvnw -version
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
./mvnw -f kata-zero/after/02-first-test/pom.xml test
./mvnw clean verify
```

El wrapper fija Maven 3.10.0 y descarga dependencias en la primera ejecución. Seleccionar el mismo JDK en el IDE. Cada etapa tiene su POM y .sdkmanrc; también admite `mvn compile exec:java` desde su carpeta.

En Windows nativo usar mvnw.cmd y configurar JAVA_HOME al mismo build Zulu. SDKMAN se puede usar en WSL, no administra directamente un JDK nativo de Windows.

Para ejecutar otra fotografía, cambiar la ruta del POM en el comando. Las dos primeras etapas no tienen pruebas JUnit: que Maven termine allí no prueba corrección funcional.

## Demostración

1. Cuenta inicial: 10 META y 10 AAPL, ambas a 100 USD. Total 2000 USD; objetivo 40/60. El programa propone vender 2 META y comprar 2 AAPL.
2. Extraer la fórmula y repetir: misma salida.
3. Introducir en la prueba otro precio: META a 150 USD; total 2500 USD. META debe valer 1000 USD: conservar 6.6666... y vender 3.3333. La fórmula heredada propone vender 4.
4. Ver la prueba fallar, eliminar la pérdida de fracciones y ejecutarla de nuevo.

El resultado esperado se proporciona con una tabla calculada a mano. No se pide descubrir el bug sin ayuda. El menú solo consulta, calcula y sale; para reproducir el cambio de precio en consola, editar el primer literal 100.00 a 150.00 y recompilar una copia.

`samples/recorrido-inicial.txt` contiene las opciones 1, 2, 1 y 0. Se puede redirigir como entrada para repetir la demostración en una terminal compatible.

## Producción del video

- [Guion y diapositivas](docs/GUION.md).
- [Deck interactivo de introducción a JUnit](../presentation/intro-junit-kata-zero/README.md).
- [Qué cambió y por qué](docs/EVOLUCION.md).
- [Revisión colegiada](docs/CONSEJO.md).
- [Validación reproducible](docs/VALIDACION.md).
- [Referencia](docs/REFERENCIAS.md).
- [Decisiones](../DECISIONS.md).

El script opcional `python3 scripts/verify-kata-zero.py`, desde la raíz, usa el JDK exacto, construye con Maven y comprueba conservación del ejemplo habitual, diferencia intencional del caso fraccionario y rojo/verde en copias temporales. Python es para preparar el material, no un requisito de la lección.

## Historial

`kata-zero-v3-first-test-red` conserva la primera prueba fallida del escenario vigente. `kata-zero-v3-ready` identifica el material corregido y validado. Las etiquetas sin v3 son antecedentes: la versión extensa original y el experimento de redondeo más sutil. No se movieron ni borraron.

```sh
git log --oneline --decorate
git diff kata-zero-v3-first-test-red kata-zero-v3-ready -- kata-zero/after/02-first-test/src
```

## Reto opcional

Con el precio nuevo, AAPL debe representar 1500 USD; a 100 USD por acción necesita 15 acciones y ya tiene 10. Agregar una prueba que espere comprar 5.0000 AAPL. Usar solo @Test y assertEquals, sin entregar ni recibir calificación.
