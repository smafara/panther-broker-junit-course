# Introducción a JUnit con Kata Zero

Un deck Slidev en español de México para **un solo video introductorio** de aproximadamente 15 minutos. Sigue la Kata Zero vigente del repositorio; no cubre todo el módulo 1 ni los videos 1.1–1.3.

## Ejecutar

Desde esta carpeta, con Node y npm compatibles con las versiones fijadas en package.json:

```sh
npm ci
npx playwright install chromium # una vez, para exportar o verificar
npm run dev
npm run build
npm run preview
npm run export:pdf
```

El navegador del presentador permite consultar las notas incluidas en cada diapositiva. Las flechas avanzan primero revelados y focos de código; después cambian de diapositiva.

Con `npm run dev`, abrir `http://localhost:3030/` para presentar y `http://localhost:3030/presenter/` para ver las notas. Los comandos se ejecutan según se necesiten; no todos a la vez. Para la comprobación automatizada, mantener el servidor dev abierto y ejecutar `npm run check:deck` en otra terminal.

`npm run export:pdf` genera `intro-junit-kata-zero.pdf`. La SPA compilada queda en `dist/`. Ambos son artefactos regenerables y no se incluyen en Git.

El deck interactivo es la versión principal: el PDF es una captura estática y no reproduce transiciones, revelados ni transformaciones de código. La exportación necesita Chromium/Playwright disponible según la configuración del equipo.

## Recorrido de 19 diapositivas

| Diapositivas | Momento |
|---|---|
| 1–4 | Problema, requisito de fracciones y ejemplo entero |
| 5–6 | Menú de consola y verificación manual |
| 7–9 | Cambia META a 150 USD y aparece la venta incorrecta |
| 10–13 | Extraer cálculo, JUnit, AAA y primera prueba |
| 14–17 | Rojo, int heredado, transformación a código corregido y verde |
| 18–19 | Alcance y reto opcional |

## Contenido técnico

- Datos iniciales: 10 META y 10 AAPL, ambas a 100 USD; objetivo 40/60; vender 2 y comprar 2.
- Nuevo precio: solo META pasa a 150 USD; total2500, objetivoMETA1000; vender3.3333. El cálculo heredado propone vender4 por convertir la cantidad objetivo a int.
- La extracción conserva el defecto. La prueba falla en la etiqueta `kata-zero-v3-first-test-red` y pasa tras corregir producción, sin cambiar el esperado.
- JDK del código Java: SDKMAN `25.0.5.0+8-zulu`; JUnit6.1.3 y Maven Wrapper del repositorio.
- Código de las diapositivas tomado de kata-zero; fragmentos omiten imports o cambian saltos de línea solo para lectura.
- No se afirma que este recorrido sea TDD ni que una prueba cubra todo el programa.

## Recursos visuales y edición

- `slides.md`: contenido, notas por transición, focos de líneas y `magic-move` del calculador defectuoso al corregido.
- `style.css`: paleta slate, acentos menta/violeta, tarjetas, layouts de dos columnas y transiciones accesibles.
- `setup/shiki.ts`: resaltado Java con tema oscuro.
- `setup/mermaid.ts`: diagramas nativos AAA y arquitectura mínima de JUnit.

Sin imágenes externas, fuentes web ni CDN. Mermaid se renderiza localmente dentro de Slidev; Shiki resalta Java. La etiqueta `java` identifica el lenguaje, no ejecuta Java ni valida por sí sola la compilación de los fragmentos.

Fuentes técnicas de sintaxis: [Slidev Magic Move](https://sli.dev/features/shiki-magic-move), [animaciones](https://sli.dev/guide/animations), [Mermaid](https://sli.dev/features/mermaid) y [Shiki](https://sli.dev/custom/config-highlighter). El contenido docente proviene del temario y del guion de Kata Zero del repositorio.
