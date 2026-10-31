# Validación del deck

31 de octubre de 2026, macOS aarch64, Node 26.13.0 y npm 11.20.0. Dependencias fijadas en package.json y package-lock.json.

## Comprobaciones realizadas

- `npm run build`: SPA compilada correctamente en dist.
- `npm run export:pdf`: PDF de 19 páginas generado correctamente.
- Revisión visual mediante páginas rasterizadas del PDF: portada, extracción, JUnit, AAA, primera prueba y transformación de código. Se corrigió una línea recortada en la extracción y se centraron y ajustaron los diagramas.
- `npm run check:deck`, con servidor dev activo: 19 diapositivas, 19 notas, dos diagramas Mermaid, una diapositiva con magic-move, sin errores de página, recursos externos ni desbordamientos detectados.
- Revisión del contenido contra los archivos vigentes de Kata Zero: mismos datos, conversión defectuosa a entero, esperado -3.3333, resultado defectuoso -4.0000 y fórmula corregida. Algunos fragmentos omiten imports o cambian saltos de línea para lectura.

El verificador selecciona la diapositiva activa por data-slidev-no; Slidev también mantiene vecinas precargadas en el DOM. Comprueba los revelados en su estado final. Normaliza el temporizador de animación y desactiva wake lock solo en el navegador automatizado: no mide la suavidad visual de cada cuadro de una transición.

El PDF es estático. Para grabar, ensayar los clics, focos, cambios de código y notas en el deck interactivo. No se verificó este material en Windows ni Safari. La prueba Java subyacente ya fue validada con Zulu 25.0.5+8 en Kata Zero; Shiki resalta el código y no lo ejecuta.
