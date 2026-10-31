# Introducción a JUnit con Kata Zero

Deck Slidev en español de México para **un video introductorio de 7–8 minutos**, con 12 diapositivas. Motiva las pruebas con una historia de cambio de requisito; no es todavía un tutorial de arquitectura, AAA, refactorización ni de la API completa de JUnit.

## Ejecutar

Desde esta carpeta:

```sh
npm ci
npx playwright install chromium # una vez, para verificar o exportar
npm run dev
npm run build
npm run preview
npm run export:pdf
```

Las versiones de Node y paquetes deben cumplir package.json. El presentador de Slidev muestra notas para cada transición. Avanzar recorre primero los revelados y focos de código; después cambia de diapositiva.

La versión interactiva conserva revelados y transformaciones. El PDF es una captura estática. La exportación necesita Chromium/Playwright disponible según la configuración del equipo.

## Historia en siete pasos

| Paso | Diapositivas | Contenido |
|---|---|---|
| 1 | 1–2 | Presentar el programa de acciones completas |
| 2 | 3 | Permitir comprar y vender fracciones |
| 3 | 4–5 | Cambiar int por double y volver a probar con el ejemplo habitual |
| 4 | 6–7 | Otros valores revelan la pérdida de la fracción |
| 5 | 8 | Introducir pruebas unitarias; automatizar el mismo caso todavía omite el defecto |
| 6 | 9–11 | Agregar el caso fraccionario, ver rojo, corregir y ejecutar tres pruebas verdes |
| 7 | 12 | Presentar lo que enseñará el curso |

## Datos y defecto vigentes

- Cuenta inicial: 10 META y 10 AAPL a 100 USD cada una; objetivo 40/60. Vender 2 META y comprar 2 AAPL parece funcionar.
- Nuevo precio: META pasa a 150 USD. Total2500; objetivoMETA1000; cantidadobjetivo6.666666…; vender aproximadamente3.333333. AAPL requiere comprar5.
- Adaptación ingenua: `targetShares` cambia de int a double, pero `targetValue / price` sigue dividiendo dos int. Se calcula6 y luego se guarda6.0; la venta propuesta es4.
- Corrección: `targetValue / (double) price`, conservando la parte fraccionaria aproximada.
- Primera comprobación fraccionaria: `double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10); assertEquals(-3.333333, order, 0.000001)`.

La suite original tiene dos casos enteros verdes. El caso fraccionario añadido detecta el defecto; después de corregir pasan los tres. La idea es incluir casos adecuados, no prometer que las pruebas encuentran requisitos que nunca se expresaron.

El JDK de los ejemplos sigue siendo SDKMAN `25.0.5.0+8-zulu`, con JUnit6.1.3 y Maven. El uso de double mantiene pequeño este ejemplo introductorio; no se presenta como una implementación de dinero exacto para producción.

## Capturas y recursos visuales

Las diapositivas usan **imágenes PNG generadas desde salidas reales** del flujo de preparación del repositorio, en public/terminal. Se agregan encabezados y colores para legibilidad; no son fotografías de una ventana de terminal:

- manual-original.png
- manual-fractional.png
- tests-original-green.png
- tests-fractional-red.png
- tests-fixed-green.png

Los extractos de terminal se conservan junto a las imágenes, con SVG y manifest.json. Para reproducir las ejecuciones y capturas, ver ../../kata-zero/README.md y scripts/verify-kata-zero.py --captures desde la raíz. No reemplazar capturas por resultados inventados en HTML.

`slides.md` contiene contenido y notas; `style.css` define paleta slate, tipografía y tarjetas. Shiki ofrece foco y números de línea; magic-move muestra los cambios de código. Mermaid se usa solo para el flujo del requisito, sin introducir aún la arquitectura de JUnit. No hay fuentes web ni imágenes de CDN.

La narración, las notas y las capturas corresponden al guion vigente de introducción. Las versiones anteriores del deck y de los defectos se conservan como antecedentes en Git.

## Presentar y verificar

Con npm run dev, abrir http://localhost:3030/; las notas están en http://localhost:3030/presenter/. Con el servidor abierto, ejecutar npm run check:deck en otra terminal. La comprobación incluye la carga de las cinco imágenes.

El PDF estático se genera como intro-junit-kata-zero.pdf; la SPA compilada queda en dist. El fuente, las capturas y su procedencia se versionan; el PDF y dist se regeneran.
