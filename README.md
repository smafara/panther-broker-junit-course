# Curso de pruebas unitarias con Java

Material de servicio social para estudiantes de México. Videos y práctica opcional, sin entregas calificadas.

- [Temario](COURSEWORK.md).
- [Kata Zero: del menú de consola a la primera prueba](kata-zero/README.md).
- [Presentación: Introducción a JUnit con Kata Zero](presentation/intro-junit-kata-zero/README.md).
- [Decisiones del curso](DECISIONS.md).
- [Registro de cambios](CHANGELOG.md).

Cada etapa de Kata Zero es un proyecto Maven independiente. El POM raíz permite verificar todas las etapas juntas. El repositorio local `fintual-kata` es una referencia independiente y se excluye de este historial.

## Empezar

Usar **Zulu `25.0.5.0+8-zulu` de SDKMAN** en terminal, Maven y el IDE:

```sh
sdk env
./mvnw clean verify
./mvnw -q -f kata-zero/before/pom.xml compile exec:java
```

El wrapper fija Maven 3.10.0. En Windows nativo usar `mvnw.cmd` con JAVA_HOME configurado; en WSL se puede usar SDKMAN. Ver los detalles en Kata Zero.

La validación adicional para preparar los videos se ejecuta con `python3 scripts/verify-kata-zero.py` y selecciona explícitamente el JDK del curso.

No hay publicación ni remoto configurado. Las decisiones posteriores se agregan al registro sin borrar las anteriores.
