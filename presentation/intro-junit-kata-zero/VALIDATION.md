# Validación de la introducción narrativa

31 de octubre de 2026. macOS aarch64, Node 26.13.0 y npm 11.20.0; dependencias fijadas en package.json y lockfile. Ejemplos Java ejecutados exclusivamente con SDKMAN Zulu 25.0.5.0+8-zulu y Maven.

## Verificación

- `npm run build`: SPA compilada correctamente.
- `npm run export:pdf`: PDF de 12 páginas generado.
- `npm run check:deck`, con dev activo: 12 diapositivas y 12 notas; cinco imágenes de terminal cargadas, un Mermaid, dos diapositivas con magic-move; sin errores de página, recursos externos ni desbordamientos detectados.
- Revisión visual de páginas rasterizadas del PDF: resultados originales verdes, nueva prueba con falla, suite corregida y cierre del curso. Se quitaron esquinas blancas de los PNG al renderizar el fondo completo.
- Verificación Java y consola mediante scripts/verify-kata-zero.py: 15 recorridos, dos pruebas originales verdes con defecto, tres pruebas con una falla al agregar el caso y tres verdes después de corregir.

## Procedencia de las capturas

Las cinco imágenes de public/terminal son representaciones de extractos de ejecuciones reales. .txt conserva las líneas; .svg describe su presentación; .png las rasteriza; manifest.json registra el estado y código de salida. Los títulos y colores se agregan para legibilidad. No se fotografió una ventana de terminal ni se inventaron resultados.

Para reproducir las capturas, usar las instrucciones de ../../kata-zero/README.md. La opción --render-only del script regenera las imágenes desde el manifiesto sin repetir Maven.

## Límites

La introducción motiva la necesidad de casos adecuados; no enseña todavía arquitectura, AAA o refactorización. El problema mostrado es división entre int antes de la asignación double, no error binario de punto flotante.

El verificador del navegador selecciona solo la diapositiva activa, comprueba los revelados en su estado final y normaliza el temporizador en modo headless. No mide la suavidad cuadro a cuadro de las transiciones. El PDF es estático; ensayar los clics y notas en la presentación interactiva antes de grabar. No se verificó Windows ni Safari.
