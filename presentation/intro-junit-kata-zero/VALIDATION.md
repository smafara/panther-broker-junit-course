# Validación de la introducción narrativa

31 de octubre de 2026. macOS aarch64, Node 26.13.0 y npm 11.20.0; dependencias fijadas en package.json y lockfile. Ejemplos Java ejecutados exclusivamente con SDKMAN Zulu 25.0.5.0+8-zulu y Maven.

## Verificación

- `npm run build`: SPA compilada correctamente.
- `npm run export:pdf`: PDF de 13 páginas generado.
- `npm run check:deck`, con dev activo: 13 diapositivas y 13 notas; cinco grabaciones con reproducción y pausa verificadas, cinco imágenes estáticas en exportación, un Mermaid, dos diapositivas con magic-move; sin errores de página, recursos externos ni desbordamientos detectados.
- Revisión visual de páginas rasterizadas del PDF: resultados originales verdes, nueva prueba con falla, suite corregida y cierre del curso. Se quitaron esquinas blancas de los PNG al renderizar el fondo completo.
- Verificación Java y consola mediante scripts/verify-kata-zero.py: 15 recorridos, dos pruebas originales verdes con defecto, tres pruebas con una falla al agregar el caso y tres verdes después de corregir.

## Procedencia de las capturas

Las cinco imágenes de public/terminal son representaciones de extractos de ejecuciones reales. .txt conserva las líneas; .svg describe su presentación; .png las rasteriza; manifest.json registra el estado y código de salida. Los títulos y colores se agregan para legibilidad. No se fotografió una ventana de terminal ni se inventaron resultados.

Para reproducir las capturas, usar las instrucciones de ../../kata-zero/README.md. La opción --render-only del script regenera las imágenes desde el manifiesto sin repetir Maven.

## Límites

La introducción motiva la necesidad de casos adecuados; no enseña todavía arquitectura, AAA o refactorización. El problema mostrado es división entre int antes de la asignación double, no error binario de punto flotante.

El verificador del navegador selecciona solo la diapositiva activa, comprueba los revelados en su estado final y normaliza el temporizador en modo headless. No mide la suavidad cuadro a cuadro de las transiciones. El PDF es estático; ensayar los clics y notas en la presentación interactiva antes de grabar. No se verificó Windows ni Safari.

## Ajuste de título, marca y código original

Se agregó una diapositiva inmediatamente después de la portada con un fragmento del programa original y tarjetas que explican su propósito. El nombre vigente es Panther Broker. Portada con solo «Introducción a JUnit» y contenido sin subtítulos decorativos ni estimaciones de tiempo. La regla se conserva en presentation/AGENTS.md.

## Grabaciones de terminal

Se generaron cinco archivos `.cast` con scripts/record-kata-zero.py y el JDK exacto del curso. El script comprueba las dos salidas de consola y el flujo de pruebas 2/0, 3/1 y 3/0 (pruebas/fallas), incluidos los códigos de salida 0, 1 y 0. Todas son ejecuciones reales completas; las entradas se automatizan con pausas. La compilación previa de los ejemplos de consola no forma parte de esas dos grabaciones.

El verificador abre cada demostración, carga su archivo, confirma que el contenido avanza al reproducir, pausa al hacer clic en el terminal y al navegar a otra diapositiva. La ruta de impresión carga cinco imágenes como sustitución estática. Se revisó visualmente la página del caso rojo exportada al PDF para confirmar que muestra la captura, sin controles de reproducción.

También se verificó la SPA compilada con vite preview: la grabación manual reproduce el comando, el menú, VENDER META 2.0 y el regreso al prompt con los recursos del reproductor servidos localmente y sin errores de página.

Ajuste de integración: se regeneraron las cinco sesiones sin `echo "Salida: ..."`; los códigos de salida se verifican por un archivo de control escrito al mostrar el prompt, fuera del flujo visible. El verificador rechaza grabaciones con esa salida y comprueba la paleta Panther del reproductor.

Se inspeccionó la apariencia interactiva mediante rasterización de una impresión de navegador en modo screen: fondo continuo, terminal sin controles visibles y ausencia del enlace de descarga. SPA compilada y PDF regenerados tras el ajuste.

Se corrigió el recorte vertical: el estilo global de pre heredaba un interlineado de 1.5 mientras la cuadrícula del reproductor usa 1.15. Ahora respeta --term-line-height. El verificador compara interlineado y altura de fila, además de comprobar que la barra y la superposición inicial están ocultas. Un botón transparente accesible controla reproducir/pausar/repetir.
