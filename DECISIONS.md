# Registro de decisiones del curso

Registrar fecha, origen, decisión, alternativas y consecuencias. Distinguir requisitos expresos del usuario de decisiones de implementación del asistente. Las modificaciones posteriores deben citar qué decisión sustituyen.

## D001 — Público y modalidad · 2026-10-31

**Origen:** usuario. Curso de servicio social para público mexicano, solo video, con actividades opcionales sin calificación.

**Decisión:** narración y material en español de México; identificadores Java en inglés y nombres visibles de pruebas en español. Explicar términos financieros sin asumir experiencia invirtiendo.

## D002 — Tecnologías · 2026-10-31

**Origen:** usuario. JDK 25, JUnit 6, Mockito reciente y Maven en cada etapa.

**Decisión:** usar JDK 25 y proyectos Maven reproducibles. JUnit aparece solo en la etapa de la primera prueba. Mockito se reserva para lecciones posteriores: Kata Zero no tiene una dependencia externa que simular.

**Consecuencia:** no incorporar herramientas por anticipado. Registrar las versiones efectivamente verificadas al terminar la implementación.

## D003 — Dominio y alcance inicial · 2026-10-31

**Origen:** usuario y revisión previa. Proyecto de inversión fraccionada inspirado en Fintual/GBM.

**Decisión previa:** el temario principal usa compras, ventas, cotizaciones y saldo. **Ampliación solicitada:** Kata Zero introduce rebalanceo como motivación inicial. No se convierte por ello en un curso de algoritmos financieros.

## D004 — Referencia para Kata Zero · 2026-10-31

**Origen:** usuario: tomar `fintual-kata` como referencia. Se encontró ese repositorio local en C#.

**Decisión:** consultar README, DECISIONS.md y Portfolio.cs, sin modificar el repositorio de referencia ni portar toda su arquitectura. Identificar la revisión usada en la documentación de la kata.

## D005 — Tres fotografías del proceso · 2026-10-31

**Origen:** usuario solicita antes, refactor pequeño y primera prueba, con carpetas before/after.

**Decisión:** `kata-zero/before`, `kata-zero/after/01-small-refactor` y `kata-zero/after/02-first-test`, cada una con POM propio. Un agregador raíz ejecuta las tres.

**Alternativa:** una sola carpeta con etiquetas. Se conservan también etiquetas, pero las carpetas permiten comparar sin cambiar de revisión. La duplicación es intencional para material docente.

## D006 — Desorden intencional · 2026-10-31

**Origen:** usuario pide todo el programa inicial en `public static void main(String[] args)`, menús con println y BufferedReader, probado por ensayo y error.

**Decisión:** arreglos paralelos, nombres breves, cálculos repetidos, menú y validación mezclados. Usar BigDecimal desde el comienzo para que extraer la fórmula no cambie también la representación numérica.

**Alternativa:** double y corregir precisión junto con la refactorización. Se descarta para separar cambios de estructura y comportamiento. El código será difícil de probar, pero no se añadirán defectos aritméticos ocultos como requisito para la demostración.

## D007 — Rebalanceo acotado · 2026-10-31

**Origen:** decisión de implementación basada en la referencia.

**Decisión:** una cuenta, catálogo fijo META/AAPL/NVDA, precios didácticos en USD, sin efectivo, comisiones, impuestos ni ejecución. El plan no modifica posiciones. Pesos objetivo entre 0 y 1 que suman exactamente 1; cero permite salir de un instrumento. Cantidades fraccionadas. Cuatro decimales HALF_EVEN para las órdenes, con tope en ventas para no vender más de lo disponible.

**Consecuencia:** se mantienen cuatro decimales de la referencia para esta kata, aunque el simulador del temario proponga seis. No es precisión atribuida a un intermediario. El redondeo puede dejar diferencias pequeñas entre compras y ventas; no se promete un ejecutor autofinanciado.

## D008 — Refactorización mínima y primera prueba · 2026-10-31

**Origen:** usuario pide un refactor pequeño y la introducción de una prueba.

**Decisión:** extraer únicamente la cantidad firmada a negociar a RebalanceCalculator. Positivo significa comprar y negativo vender. Mantener el menú desordenado. La siguiente etapa agrega una prueba JUnit con valores esperados calculados a mano, sin rediseñar producción.

**Consecuencia:** no introducir records, servicios, mocks, pruebas parametrizadas ni una arquitectura completa. La validación de entradas sigue en la consola; el cálculo extraído recibe datos válidos.

## D009 — Git y trazabilidad · 2026-10-31

**Origen:** usuario pide repositorio e historial de cada decisión.

**Decisión:** inicializar Git en la raíz del curso; conservar `fintual-kata` como referencia excluida; commits por etapa, etiquetas de recorrido, documentación del cambio y guion. No publicar ni configurar un remoto sin una solicitud posterior.

**Consecuencia:** como no había identidad Git configurada, los commits generados por el asistente usarán la identidad explícita `Codex <codex@localhost>` mediante opciones por comando, sin cambiar la configuración global.

## D010 — Distribución exacta del JDK · 2026-10-31

**Origen:** requisito explícito del usuario durante la implementación.

**Decisión:** usar exclusivamente `25.0.5.0+8-zulu` de SDKMAN para todos los proyectos, compilaciones, pruebas y ejemplos. Se fija en `.sdkmanrc`; ejecutar `sdk env` en la raíz del curso. Para el IDE, seleccionar esa misma instalación.

**Consecuencia:** sustituye cualquier uso anterior del JDK Temurin configurado por defecto en la máquina. No cambiar el JDK global; las verificaciones usarán JAVA_HOME y PATH del JDK solicitado.

## D011 — Versiones y construcción comprobadas · 2026-10-31

**Origen:** implementación y verificación del material.

**Decisión:** Maven Wrapper 3.3.4 con Maven 3.10.0; Compiler Plugin 3.16.0 (estable, evitando 4.0 beta), Surefire 3.6.1, Enforcer 3.7.0 y Exec Plugin 3.6.4. Primera prueba con BOM JUnit 6.1.3 y junit-jupiter. Las versiones se fijan en los archivos de construcción y se resolvieron y ejecutaron con el JDK solicitado.

**Consecuencia:** cada etapa funciona con su POM sin heredar configuración del agregador. Repetir configuración es intencional para que cada fotografía pueda copiarse de forma independiente. Enforcer exige Java 25.0.5 de Azul; .sdkmanrc fija el build y el script de verificación comprueba 25.0.5+8-LTS. El wrapper no cambia la configuración global del equipo.

## D012 — Evidencia docente y evidencia de producción · 2026-10-31

**Origen:** necesidad de preparar una demostración reproducible.

**Decisión:** una sola prueba JUnit como material del estudiante; un script separado de preparación compara 12 recorridos entre tres versiones y comprueba que after/02 no cambie producción respecto a after/01. Verificar además que la prueba falla con un defecto temporal y pasa tras restaurarlo.

**Consecuencia:** no confundir la primera prueba con una suite completa. El defecto no se conserva en el historial final ni se afirma que escribir una prueba después del programa sea TDD. Python es opcional y exclusivo de la preparación del material.

## D013 — Integración de la lección cero · 2026-10-31

**Origen:** nuevo enfoque solicitado por el usuario.

**Decisión:** agregar una introducción de aproximadamente 20 minutos antes de los 15 videos del temario. El video 1.2 consolida configuración y estructura ya vistas de forma breve en Kata Zero. Mantener el simulador de compras del curso principal como evolución posterior, sin introducir toda su arquitectura en la introducción.

**Consecuencia:** 16 videos principales y aproximadamente 210 minutos previstos. Los cuatro decimales de órdenes en Kata Zero siguen la referencia; los seis decimales del simulador posterior deben anunciarse como un cambio explícito de contrato cuando se implemente, no mezclarse silenciosamente.

## D014 — Simplificar Kata Zero · 2026-10-31

**Origen:** el usuario acepta que la primera versión era demasiado compleja y autoriza simplificarla.

**Decisión:** reducir main de 140 a aproximadamente 50 líneas; dos instrumentos fijos (META y AAPL), objetivo 40/60 y menú de consulta, rebalanceo y salida. Se eliminan cambios interactivos de precios, posiciones y distribución, búsqueda de símbolos y validaciones correspondientes. Se conservan BufferedReader, println, arreglos paralelos, total repetido y cálculo dentro de main como punto de partida.

**Sustituye:** el alcance de tres instrumentos y entradas editables de D006/D007. Los datos válidos están preparados; el programa no se presenta como una aplicación robusta de uso general. Se imprime en orden de catálogo y no se promete ordenar todas las ventas antes de las compras.

## D015 — Defecto realista desde el inicio · 2026-10-31

**Origen:** requisito explícito del usuario: incluir un bug que no sea evidente a primera vista, con revisión colegiada.

**Decisión:** calcular la cantidad objetivo con dos decimales, reutilizando equivocadamente precisión monetaria; después restar la posición y mostrar cuatro decimales. Los ceros añadidos no recuperan precisión. before y after/01 conservan este defecto sin señalarlo en comentarios del código estudiantil.

**Caso que lo oculta:** META a 500 USD y AAPL a 200 USD, posiciones 10 y 5, objetivo 40/60: -5.2000 y +13.0000.

**Caso que lo revela:** cambiar solo META a 350 USD. Total 4500 USD; objetivo META 1800 USD; orden exacta 1800/350 - 10 = -4.857142...; esperado -4.8571, observado -4.8600. La diferencia es numérica, no solo de escala de BigDecimal.

**Sustituye:** la exclusión de defectos iniciales de D006 y la suma temporal de D012. No se agregan impuestos, errores de punto flotante ni reglas adicionales para fabricar la falla.

## D016 — Separar extracción, prueba roja y corrección · 2026-10-31

**Origen:** revisión colegiada y requisito de conservar el proceso en Git.

**Decisión:** after/01 extrae la fórmula defectuosa sin corregirla. La primera prueba tiene un escenario y una comprobación. La etiqueta `kata-zero-v2-first-test-red` conserva la falla esperada; un commit posterior corrige solamente el cálculo de after/02, restando el valor actual antes de dividir a cuatro decimales. La versión final del agregador termina en verde.

**Sustituye:** identidad de todo el código de producción entre after/01 y after/02 en D008/D012. Main debe seguir idéntico; el cambio del calculador es ahora una corrección explícita. Las etiquetas originales de la versión extensa se conservan sin moverlas.

**Consecuencia:** verificar conservación de salida en la extracción; verificar diferencia intencional entre etapas para el escenario que revela el bug. No llamar TDD a una prueba agregada después del código existente.

## D017 — Un defecto más visible: la suposición de acciones completas · 2026-10-31

**Origen:** el usuario pide un defecto menos sutil que perder unas diezmilésimas y acepta explorar la conversión accidental a entero.

**Decisión vigente:** presentar un programa que conserva un `int` del supuesto anterior de acciones completas al adaptarse a cantidades fraccionadas. La cantidad objetivo decimal se convierte con intValue; eso descarta la fracción antes de calcular la orden. No introducir saldos residuales ni conciliación de redondeo como problema inicial.

**Caso habitual:** 10 META y 10 AAPL, ambas a 100 USD; total 2000 USD; objetivo 40/60; vender 2 META y comprar 2 AAPL. Las cantidades objetivo son enteras y ocultan el defecto.

**Caso revelador:** solo cambia el precio de META a 150 USD. Total 2500 USD; objetivo META 1000 USD; cantidad objetivo 6.6666...; venta correcta 3.3333 y defectuosa 4.0000. AAPL requiere comprar 5. La pérdida es visible y no se confunde con una diferencia de escala.

**Sustituye:** el defecto de dos decimales y los datos de D015. La etiqueta histórica `kata-zero-v2-first-test-red` se conserva como experimento anterior; `kata-zero-v3-first-test-red` identifica la primera prueba fallida del escenario vigente. Se mantiene el proceso de D016: extracción con defecto y corrección posterior separada.

## D018 — Expectativas de aprendizaje y narración · 2026-10-31

**Origen:** pregunta del usuario sobre si la expectativa es realista y revisión de enseñanza.

**Decisión:** proporcionar el resultado esperado mediante una tabla calculada a mano. No pedir a quien ve su primera prueba que descubra el defecto solo ni que deduzca un resultado con múltiples decimales sin apoyo. Mostrar primero el ejemplo entero que parece funcionar y luego un cambio de precio que evidencia el supuesto perdido.

**Consecuencia:** la historia de acciones completas es el contexto ficticio del ejercicio, no un defecto atribuido a Fintual o GBM. La primera prueba sigue teniendo una sola comprobación; el detalle de redondeo queda para lecciones posteriores.

## D019 — Guion y validación de la versión simplificada · 2026-10-31

**Origen:** implementación revisada por los dos miembros del consejo y comprobada en terminal.

**Decisión:** guion de aproximadamente 15 minutos con ejemplo entero, cambio de precio, extracción, prueba roja y corrección. Usar `kata-zero-v3-first-test-red`, `kata-zero-v3-fixed` y `kata-zero-v3-ready` sin sobrescribir etiquetas previas. La validación compara cuatro recorridos habituales en tres etapas, el precio cambiado en copias temporales y la misma prueba con ambos calculadores.

**Sustituye:** los 20 minutos de introducción de D013 y los 12 recorridos extensos de D012. El total previsto del curso pasa a 205 minutos. La comprobación actual comprende 15 ejecuciones de consola y rojo/verde, no igualdad completa de producción entre etapas.

## D020 — Presentación del primer video · 2026-10-31

**Origen:** el usuario solicita delegar la creación de diapositivas a un subagente y después acota el alcance a un solo video: «Introducción a JUnit con Kata Zero».

**Decisión:** un deck Slidev en español de México, limitado al recorrido vigente de Kata Zero: programa de consola, ejemplo entero, cambio de precio, extracción, primera prueba, defecto de int y corrección. Mantener una introducción breve a Jupiter/Platform y al patrón Preparar–Ejecutar–Comprobar; dejar assertAll y los videos 1.1–1.3 completos para después.

**Presentación:** fondo slate oscuro, acentos sutiles, Shiki para Java, focos por línea, diagramas Mermaid, revelados progresivos, dos columnas, transiciones y magic-move para el cálculo defectuoso y corregido. Notas breves por diapositiva.

**Construcción:** Slidev usa Node y npm con versiones fijadas y lockfile; los ejemplos Java y las katas siguen usando Maven y Zulu `25.0.5.0+8-zulu`. No publicar el deck. El formato interactivo conserva animaciones; una exportación PDF es material estático complementario.

## D021 — Entrega del deck introductorio · 2026-10-31

**Origen:** trabajo delegado expresamente solicitado y revisión del integrador.

**Decisión:** guardar el deck en `presentation/intro-junit-kata-zero`, con 19 diapositivas y 19 notas, dos diagramas Mermaid nativos y transformación del calculador defectuoso al corregido. Usar Slidev 53.0.0, tema base 0.25.0 y Playwright Chromium 1.64.1 con package-lock. Las fuentes son locales, sin CDN ni imágenes remotas.

**Revisión:** compilar la SPA, exportar PDF de 19 páginas, comprobar contenido contra Kata Zero v3 y revisar visualmente páginas representativas. Se dividió una línea que quedaba recortada y se centraron los diagramas. El script `check:deck` revisa las diapositivas activas y las notas en el servidor local; el PDF no sustituye la revisión de animaciones en el navegador al preparar la grabación.

**Consecuencia:** solo se entrega el video introductorio. La propuesta inicial de cubrir todo el módulo 1 quedó fuera de alcance. Los archivos generados y dependencias instaladas se excluyen de Git; se versionan fuente, configuración, lockfile e instrucciones.
