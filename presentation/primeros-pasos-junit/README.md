# Primeros pasos con JUnit

Presentación Slidev en español de México, continuación de «Introducción a las pruebas unitarias con JUnit». Incluye notas por diapositiva, ejemplos fieles a `primeros-pasos-junit/after` y práctica opcional sin calificación.

```sh
cd presentation/primeros-pasos-junit
npm ci
npm run dev
npm run build
npm run check:deck
npm run export:pdf
```

Abrir http://localhost:3031/; las notas están en /presenter/. Para `check:deck`, mantener el servidor iniciado. La exportación y la verificación usan Chromium de Playwright. Los proyectos Maven y su configuración se documentan en ../../primeros-pasos-junit/README.md.

La explicación de Maven presenta sus funciones y enfoca por partes fragmentos reales del POM; el archivo completo sigue en el proyecto de ejemplo. Véanse las guías oficiales de [Maven](https://maven.apache.org/what-is-maven.html) y del [POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html).

La diapositiva de ejecución reproduce una sesión real de Maven con asciinema al 50 %; el panel se actualiza al terminar con el resultado del reporte XML de Surefire. La captura para PDF deriva del mismo reporte. Para regenerar los recursos desde la raíz, ejecutar `python scripts/record-primeros-pasos.py` con PyMuPDF instalado; el script usa el JDK del curso y un directorio temporal. El ejemplo usa JDK 25.0.5.0+8-zulu, JUnit 6.1.3 y Surefire 3.6.1. Los fragmentos de configuración omiten secciones del POM que están en el proyecto completo.

Referencias oficiales: [JUnit 6: integración con Maven](https://docs.junit.org/6.1.2/running-tests/build-support.html), [doctest](https://github.com/doctest/doctest), [xUnit.net](https://xunit.net/), [pytest](https://docs.pytest.org/en/latest/getting-started.html) y [Jest](https://jestjs.io/).

Los logotipos de la diapositiva de herramientas se guardan localmente y proceden de los repositorios de [JUnit](https://github.com/junit-team/junit.org/blob/main/assets/img/junit6-temporary-logo.svg), [doctest](https://github.com/doctest/doctest/blob/master/scripts/data/logo/icon_1.svg), [xUnit.net](https://github.com/xunit/media/blob/main/logo-transparent.svg), [pytest](https://github.com/pytest-dev/design/blob/master/pytest_logo/pytest_logo_notext.svg) y [Jest](https://github.com/jestjs/jest/blob/main/website/static/img/jest.png). El diseño de pytest pertenece al equipo de pytest y se distribuye bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); los logotipos de xUnit.net se usan para identificar el proyecto de acuerdo con sus [condiciones de uso](https://github.com/xunit/media).

La comparación de dependencias usa una ilustración local de archivo JAR, el [icono de Apache Maven de Simple Icons](https://simpleicons.org/?q=apachemaven) y el [icono de Gradle de Simple Icons](https://simpleicons.org/?q=gradle), con su color adaptado al fondo oscuro.
