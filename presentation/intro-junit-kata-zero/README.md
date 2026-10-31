# Introducción a JUnit

Deck Slidev en español de México para **un video introductorio**, con 13 diapositivas. Motiva las pruebas con una historia de cambio de requisito; no es todavía un tutorial de arquitectura, AAA, refactorización ni de la API completa de JUnit.

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
| 1 | 1–3 | Portada, código original y propósito del programa; después el ejemplo entero |
| 2 | 4 | Permitir comprar y vender fracciones |
| 3 | 5–6 | Cambiar int por double y volver a probar con el ejemplo habitual |
| 4 | 7–8 | Otros valores revelan la pérdida de la fracción |
| 5 | 9 | Introducir pruebas unitarias; automatizar el mismo caso todavía omite el defecto |
| 6 | 10–12 | Agregar el caso fraccionario, ver rojo, corregir y ejecutar tres pruebas verdes |
| 7 | 13 | Presentar lo que enseñará el curso |

## Datos y defecto vigentes

- Cuenta inicial: 10 META y 10 AAPL a 100 USD cada una; objetivo 40/60. Vender 2 META y comprar 2 AAPL parece funcionar.
- Nuevo precio: META pasa a 150 USD. Total2500; objetivoMETA1000; cantidadobjetivo6.666666…; vender aproximadamente3.333333. AAPL requiere comprar5.
- Adaptación ingenua: `targetShares` cambia de int a double, pero `targetValue / price` sigue dividiendo dos int. Se calcula6 y luego se guarda6.0; la venta propuesta es4.
- Corrección: `targetValue / (double) price`, conservando la parte fraccionaria aproximada.
- Primera comprobación fraccionaria: `double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10); assertEquals(-3.333333, order, 0.000001)`.

La suite original tiene dos casos enteros verdes. El caso fraccionario añadido detecta el defecto; después de corregir pasan los tres. La idea es incluir casos adecuados, no prometer que las pruebas encuentran requisitos que nunca se expresaron.

El JDK de los ejemplos sigue siendo SDKMAN `25.0.5.0+8-zulu`, con JUnit6.1.3 y Maven. El uso de double mantiene pequeño este ejemplo introductorio; no se presenta como una implementación de dinero exacto para producción.

## Capturas y recursos visuales

El PDF usa **imágenes PNG generadas desde salidas reales** del flujo de preparación del repositorio, en public/terminal. Se agregan encabezados y colores para legibilidad; no son fotografías de una ventana de terminal:

- manual-original.png
- manual-fractional.png
- tests-original-green.png
- tests-fractional-red.png
- tests-fixed-green.png

Los extractos de terminal se conservan junto a las imágenes, con SVG y manifest.json. Para reproducir las ejecuciones y capturas, ver ../../kata-zero/README.md y scripts/verify-kata-zero.py --captures desde la raíz. No reemplazar capturas por resultados inventados en HTML.

`slides.md` contiene contenido y notas; `style.css` define paleta slate, tipografía y tarjetas. Shiki ofrece foco y números de línea; magic-move muestra los cambios de código. Mermaid se usa solo para el flujo del requisito, sin introducir aún la arquitectura de JUnit. No hay fuentes web ni imágenes de CDN.

La narración, las notas y las capturas corresponden al guion vigente de introducción. Las versiones anteriores del deck y de los defectos se conservan como antecedentes en Git.

## Presentar y verificar

Con npm run dev, abrir http://localhost:3030/; las notas están en http://localhost:3030/presenter/. Con el servidor abierto, ejecutar npm run check:deck en otra terminal. La comprobación incluye las cinco grabaciones, reproducción, pausa al cambiar de diapositiva y las imágenes de exportación.

El PDF estático se genera como intro-junit-kata-zero.pdf; la SPA compilada queda en dist. El fuente, las capturas y su procedencia se versionan; el PDF y dist se regeneran.

## Convención de presentación

El programa se llama **Panther Broker**, referencia elegida a la UAM Azcapotzalco. El deck se titula **Introducción a JUnit** y la portada muestra solo el título, sin subtítulo ni duración. Se omiten también antetítulos decorativos y tiempos en las diapositivas y sus notas. La regla para las siguientes presentaciones está en [AGENTS.md](../AGENTS.md).

## Grabaciones de terminal

Las cinco demostraciones se reproducen con **asciinema-player 3.17.0**, instalado desde npm y servido localmente. Presionar ▶ para comenzar; los controles permiten pausar, recorrer la línea de tiempo, cambiar velocidad y expandir el terminal. Al salir de una diapositiva se pausa su grabación. El PDF conserva los PNG como alternativa estática.

Para regenerarlas desde la raíz:

```sh
python3 scripts/record-kata-zero.py
```

El script selecciona exclusivamente SDKMAN `25.0.5.0+8-zulu`, prepara copias temporales de los proyectos Maven y registra sesiones reales de pseudoterminal en formato asciicast v2. Teclea automáticamente los comandos y las opciones 1, 2 y 0 con pausas: no es una persona escribiendo ni una animación fabricada de resultados. Los ejemplos de consola ya están compilados antes de grabar; las tres sesiones de pruebas muestran Maven completo, su resultado. El código de salida se valida internamente, sin imprimir comandos adicionales en la demostración. La preparación modifica únicamente las copias temporales para reconstruir el defecto y cambiar META a 150 USD.

`public/terminal/*.cast` conserva las salidas completas con sus tiempos originales; `recordings.json` documenta comandos, duración, JDK y códigos de salida. El reproductor comprime pausas sin actividad a dos segundos; no elimina salida. No se suben grabaciones a servicios externos. Si falla el reproductor, se muestra la imagen estática.

Referencias: [integración del reproductor](https://docs.asciinema.org/manual/player/quick-start/), [opciones](https://docs.asciinema.org/manual/player/options/) y [formato asciicast v2](https://docs.asciinema.org/manual/asciicast/v2/).

El reproductor usa la misma paleta slate/mint que los bloques de código, con controles discretos y un botón «Reproducir ejecución». No muestra enlaces de descarga debajo del contenido; las grabaciones siguen disponibles en public/terminal. Las sesiones terminan al volver al prompt, sin echo de estado.
