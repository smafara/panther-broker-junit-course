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

## D022 — Introducción narrativa en siete momentos · 2026-10-31

**Origen:** el usuario considera excesivo el alcance del deck y define una secuencia nueva: programa de acciones completas; requisito de fracciones; cambio ingenuo de int a double; caso manual habitual que sigue pasando; nuevos datos que revelan el error; introducción y demostración de pruebas con capturas reales; avance de contenidos del curso.

**Decisión:** sustituir el recorrido de explicación de arquitectura, AAA y refactorización por una historia de aproximadamente 7–8 minutos. Esos conceptos se anuncian para el curso, sin enseñarlos aquí. Reducir el deck a unos 12 apoyos visuales.

## D023 — Cambio de tipo que conserva una división entera · 2026-10-31

**Origen:** requisito del usuario de mostrar un cambio de int a double que parece funcionar al repetir el ejemplo original.

**Decisión:** before usa cantidades objetivo y diferencias int. En `after/01-naive-fractions` solo cambian esas dos variables a double; los operandos de `targetValue / price` siguen siendo int. La fracción se descarta antes de asignarse a double. Esta etapa sustituye la carpeta after/01-small-refactor.

**Ejemplos:** precios 100/100, diez acciones de cada una y objetivo 40/60 dan vender 2 y comprar 2 en ambas versiones. Con META a 150 USD, el total es 2500, el objetivo META vale 1000 y la división entera 1000/150 produce 6: venta incorrecta de 4, frente a 3.333333... requerida.

**Sustituye:** el intValue heredado de D017. El error actual es truncamiento por división entera; no se atribuye a la representación binaria de double. La corrección demostrada promueve un operando de la división. Son precios enteros y datos preparados, no una implementación financiera general; BigDecimal y sus contratos se enseñan después.

## D024 — Una suite necesita casos que distingan comportamientos · 2026-10-31

**Origen:** precisión pedagógica al implementar el punto cinco solicitado.

**Decisión:** mostrar dos pruebas del ejemplo original que pasan incluso con el defecto. Agregar una tercera para el nuevo escenario, verla fallar y después ver las tres pasar con la corrección. Repetir solamente el caso original en JUnit no descubre el error.

**Consecuencia:** no afirmar que tener pruebas por sí solo garantiza detectar el defecto. Se usa una tolerancia pequeña y explícita al comparar double; el detalle de assertions y precisión queda para después. La extracción necesaria para llamar al cálculo es material de apoyo, sin ocupar una sección del video.

## D025 — Capturas verificables de las salidas · 2026-10-31

**Origen:** solicitud del usuario de capturas de terminal con resultados verdes o con errores.

**Decisión:** ejecutar los proyectos Maven con Zulu 25.0.5+8, conservar extractos textuales reales y generar imágenes de terminal a partir de esos extractos. No inventar errores, cantidades ni conteos de pruebas. Las capturas y su script reproducible se versionan como material del video.

**Historial:** `kata-zero-v4-first-test-red` conserva la fórmula defectuosa y la suite ampliada; un commit posterior corrige producción sin cambiar el esperado. Las etiquetas anteriores permanecen como antecedentes.

## D026 — Entrega de la introducción reducida · 2026-10-31

**Origen:** implementación de los siete puntos del usuario y comprobación del material.

**Decisión:** entregar 12 diapositivas con 12 notas para 7–8 minutos, cinco imágenes de salidas verificadas, un diagrama del requisito y dos transformaciones breves de código. Arquitectura y AAA se anuncian en el cierre, no se explican. El temario reserva ocho minutos a esta introducción, para un total estimado de 198 minutos.

**Evidencia:** reactor Maven en verde con tres pruebas; dos casos originales también pasan con el defecto; la suite ampliada falla uno de tres y pasa tras promover el denominador. Se verifican 15 recorridos de consola y la carga de las cinco imágenes. Deck compilado y PDF de 12 páginas exportado; revisión en navegador sin desbordamientos detectados.

**Procedencia visual:** las capturas se renderizan desde extractos reales, con colores y encabezados añadidos. No se presentan como fotos de un emulador de terminal. SVG, PNG, texto y manifest.json se versionan por el requisito explícito del usuario; esta excepción amplía la exclusión genérica de artefactos de D021. PDF, dist y dependencias permanecen excluidos.

## D027 — Código original antes del ejemplo · 2026-10-31

**Origen:** el usuario pide una diapositiva entre las primeras dos para presentar el código original y su propósito.

**Decisión:** insertar inmediatamente después de la portada un fragmento fiel de los arreglos y el cálculo de before/Main.java, con explicación de cómo propone ventas y compras para el objetivo 40/60. Se aclara que imports y menú se omiten de la diapositiva, no del programa. El deck pasa a 13 diapositivas.

## D028 — Títulos sin subtítulos ni duración · 2026-10-31

**Origen:** regla explícita del usuario para esta y las siguientes presentaciones.

**Decisión:** la presentación se titula «Introducción a JUnit», con ortografía normalizada. La portada muestra solo ese título. Quitar subtítulo, etiquetas complementarias, antetítulos decorativos y duración del contenido del deck; quitar también los tiempos de sus notas. Conservar la planificación de grabación en el guion interno. Se registra la convención en presentation/AGENTS.md para futuras ediciones.

## D029 — Panther Broker · 2026-10-31

**Origen:** el usuario elige Panther Broker como referencia a la UAM Azcapotzalco.

**Decisión:** sustituir la marca Fracción por Panther Broker en el temario vigente, presentación, documentación operativa y encabezados del programa. No se cambia el problema, los números ni las expectativas de las pruebas. Conservar las decisiones históricas como antecedentes y no incorporar logotipos institucionales ni atribuir un aval de la UAM.

## D030 — Paquete de Panther Broker · 2026-10-31

**Origen:** el usuario solicita mx.azc.uam.pantherbroker.

**Decisión:** adoptar ese paquete en las tres etapas de Kata Zero, mover fuentes y pruebas a su ruta correspondiente y actualizar mainClass, groupId de Maven y verificación reproducible. No modificar las etiquetas históricas.

## D031 — Ejecuciones reproducibles en movimiento · 2026-10-31

**Origen:** el usuario autoriza agregar grabaciones de terminal a las diapositivas.

**Decisión:** sustituir las cinco imágenes en la presentación interactiva por asciinema-player, con reproducción manual, controles y pausa al cambiar de diapositiva. Conservar PNG en PDF y como alternativa ante errores. Versionar archivos asciicast v2 grabados de pseudoterminales reales mediante un script Python, con entrada automatizada y salida completa sin editar. Los tiempos de captura son reales; el reproductor acorta solo pausas inactivas. No publicar sesiones en servidores externos.

**Reproducción:** scripts/record-kata-zero.py usa el JDK Zulu solicitado, copias temporales de los módulos Maven y valida cantidades, conteos de pruebas y códigos de salida. Documentar que la compilación de consola y la preparación de los escenarios preceden a la grabación.

## D032 — Terminal integrado y sin comandos de diagnóstico visibles · 2026-10-31

**Origen:** el usuario pide quitar echo de Salida y mejorar la integración visual.

**Decisión:** regenerar las cinco sesiones para terminar al regresar al prompt. Verificar el código de salida por un archivo de control del shell, sin imprimir diagnósticos adicionales. Usar fondo slate y acentos mint/violeta del deck, borde del mismo estilo que Shiki, controles discretos y botón de reproducción en español. Quitar el enlace de descarga bajo cada terminal; conservar archivos y procedencia en el repositorio. Mantener controles, pausa al navegar y capturas de PDF.

## D033 — Solo terminal y corrección del recorte de texto · 2026-10-31

**Origen:** el usuario solicita ocultar el reproductor y aporta una captura de texto recortado.

**Decisión:** ocultar barra de controles y superposición inicial; reproducir y pausar al hacer clic en el terminal, con botón transparente accesible por teclado y repetición al terminar. Corregir el interlineado global de pre para respetar --term-line-height: el interlineado heredado excedía la altura de las filas y recortaba los glifos. Agregar comprobaciones de geometría y controles ocultos al verificador del deck. Conservar pausa al navegar y capturas de PDF.

## D034 — Definir prueba unitaria antes de mostrar JUnit · 2026-10-31

**Origen:** el usuario pide una diapositiva breve entre las diapositivas 8 y 9.

**Decisión:** insertar «¿Qué es una prueba unitaria?» como nueva diapositiva 9. Definir la comprobación automática de un comportamiento concreto de una pequeña parte del programa y conectar datos conocidos, operación y resultado esperado con Panther Broker. Presentar a JUnit como herramienta para escribir y ejecutar esas pruebas en Java. Mantener la explicación breve, con notas y tres revelados; el deck pasa a 14 diapositivas.

## D035 — Del límite manual a una red de pruebas · 2026-10-31

**Origen:** el usuario propone explicar detección temprana, límites de probar a mano, regresiones y comprobaciones deterministas antes de presentar pruebas unitarias; después mostrar ejemplos del requisito entero, caso fraccionario rojo y solución verde.

**Decisión:** agregar una diapositiva de motivación después del fallo manual, presentar el concepto y mostrar los dos métodos reales de OriginalExamplesTest antes de su ejecución. Explicar que esos casos podían guardarse desde el requisito int y se ejecutan con el cálculo extraído y su firma vigente. Mostrar que al cambiar a double siguen verdes, agregar el caso fraccionario, corregir producción sin debilitar expectativas y terminar con tres pruebas verdes. El deck pasa a 16 diapositivas. Detectar automáticamente las diapositivas con grabaciones en el verificador para tolerar inserciones futuras.

## D036 — Presentar JUnit al finalizar el diagrama · 2026-10-31

**Origen:** el usuario pide que «JUnit nos ayuda…» aparezca al final.

**Decisión:** revelar esa frase con el cuarto clic, después de las tres tarjetas, usando la transición de aparición del deck. Actualizar la nota de presentación; el texto final del PDF permanece igual.

## D037 — Nombres de pruebas Given–When–Then · 2026-10-31

**Origen:** el usuario pide nombres reales y el esquema given → when → then.

**Decisión:** renombrar los tres métodos de pruebas con condiciones, acción de rebalanceo y resultado concreto, usando givenCondicion_whenAccion_thenResultado. Actualizar los DisplayName en español, fragmentos del deck, capturas y grabaciones que puedan incluir nombres. Mantener los datos y las expectativas sin cambios. Registrar la convención para futuras presentaciones.

## D038 — Nombres breves de comportamiento · 2026-10-31

**Origen:** el usuario acepta simplificar los nombres.

**Decisión:** usar sellsTwoSharesWhenAboveTarget, buysTwoSharesWhenBelowTarget y preservesFractionalSharesWhenSelling. Actualizar Java, deck, grabaciones y la convención; Given–When–Then describe la estructura sin imponer longitud al nombre.

## D039 — Autoplay pausado y resultados visuales verificables · 2026-10-31

**Origen:** el usuario pide fundido, reproducción automática al 50% y una lista de resultados similar a un IDE.

**Decisión:** revelar el terminal con fundido y reproducir a 0.5× solo cuando está visible en la diapositiva activa. En la prueba roja, esperar al cuarto clic después del código. Pausar al salir y reiniciar al volver. Mantener los controles ocultos y la interacción accesible para pausar/repetir. Agregar un panel inferior de pruebas cuyos nombres y estados se leen de los XML reales de Surefire; después del final de la grabación, revelar primero las dos originales y después la fraccionaria. Dos verdes y una roja con defecto; tres verdes tras corregir. Es una visualización de resultados de las diapositivas, no un IDE real ni el orden interno de ejecución. El PDF muestra estados finales. No agregar plugins Maven para fines visuales.

## D040 — Resaltado continuo de código multilínea · 2026-10-31

**Origen:** el usuario pide resaltar el bloque completo en vez de franjas del ancho de cada línea.

**Decisión:** hacer que las líneas de Shiki ocupen todo el ancho y compartan exactamente el interlineado, usando una cuadrícula que evita huecos por saltos de línea. Un rango contiguo se ve como un solo rectángulo. Conservar los focos por clic, números de línea y colores de sintaxis; no modificar el terminal.

## D041 — Objetivos elegidos y contexto antes del código · 2026-11-01

**Origen:** el usuario solicita ingresar los porcentajes objetivo y presentar el propósito antes del código original.

**Decisión:** en las tres etapas, al calcular el rebalanceo se solicita un porcentaje entero por acción y se valida que estén entre 0 y 100 y sumen 100. El ejemplo usa 40/60 como entrada, no como regla fija; se conserva el defecto de división entera de la adaptación. Insertar después de la portada una explicación breve de entradas, propósito y plan propuesto. Actualizar fragmento, grabaciones, validaciones y guía.


## D042 — Revisión pedagógica y apertura con el programa completo · 2026-11-01

**Origen:** el usuario solicita revisar la presentación en consejo, cambiar el título, mostrar el programa completo antes de explicar su propósito y aplicar las recomendaciones.

**Decisión:** titular la portada «Introducción a las pruebas unitarias con JUnit»; presentar el archivo real completo en un panel desplazable sin explicación, seguido de una descripción concisa de entradas y propuesta. El panel favorece legibilidad en pantalla; el PDF conserva solo la parte visible. Eliminar la diapositiva redundante del fragmento original. Agregar una transición explícita de extracción del cálculo antes de las pruebas; precisar resultado esperado, signo y tolerancia. Aclarar valores aproximados, menú real, división entera y límites del ejemplo; conservar los casos originales verdes, el nuevo caso rojo y su corrección. Agrupar la ruta del curso en tres temas. El verificador localiza dinámicamente la prueba roja.


## D043 — Explicar el programa sin mostrar todo el código · 2026-11-01

**Origen:** tras revisar la segunda diapositiva, el usuario prefiere retirar el archivo completo y explicar de manera sencilla de qué consta el programa y qué hace.

**Decisión:** sustituir el panel desplazable por tres tarjetas breves: datos de la cuenta, menú y cálculo de propuestas con acciones completas. Indicar que todo está en main. Conservar la siguiente diapositiva para explicar el propósito del rebalanceo y la posterior para el ejemplo concreto. El código completo sigue disponible en kata-zero/before.


## D044 — Presentar Panther Broker mediante una ejecución · 2026-11-01

**Origen:** el usuario propone mostrar una breve demostración de terminal en la segunda diapositiva.

**Decisión:** sustituir las tarjetas por una grabación asciicast de la versión original de acciones completas, generada con la misma herramienta de grabación PTY y el JDK del curso. La sesión consulta la cuenta, introduce 40/60 y muestra el plan; no se atribuye a la versión original la ejecución de la adaptación con double. Mantener reproducción automática integrada, velocidad y alternativa estática para PDF.


## D045 — Explicar el propósito antes de la demostración · 2026-11-01

**Origen:** el usuario aclara que desea una explicación en la parte superior de la segunda diapositiva, seguida de la demostración.

**Decisión:** agregar una frase y un diagrama compacto con acciones, precios, distribución objetivo y propuesta de operaciones. Revelar y reproducir la grabación al avanzar para que la explicación aparezca primero. Usar la siguiente diapositiva para aclarar que la distribución se refiere al valor de la cuenta.


## D046 — Eliminar la explicación duplicada · 2026-11-01

**Origen:** el usuario acepta retirar la diapositiva redundante después de explicar el programa en la segunda diapositiva.

**Decisión:** pasar directamente de la demostración al ejemplo de acciones completas. Explicar en ese ejemplo que los porcentajes corresponden al valor de la cuenta y que la propuesta no ejecuta operaciones ni modifica la cuenta. Actualizar la ruta de la presentación a 17 diapositivas.

## D047 — Primeros pasos con JUnit · 2026-11-01

**Origen:** el usuario solicita una nueva presentación sobre pruebas de software, JUnit, herramientas equivalentes, configuración y AAA.

**Decisión:** crear una presentación independiente con el mismo tema y notas. Explicar pruebas manuales y automáticas, escalas, JUnit Jupiter y ejemplos de otros ecosistemas; usar Jest como framework de JavaScript. Reconocer la configuración manual con JAR y recomendar Maven o Gradle; el curso utiliza Maven Wrapper, BOM JUnit 6.1.3, Jupiter y Surefire 3.6.1. Crear snapshots Maven before/after con el cálculo corregido de Kata Zero y una prueba real AAA, JDK SDKMAN 25.0.5.0+8-zulu y práctica voluntaria. La presentación muestra fragmentos del POM y la prueba del repositorio, con fuentes oficiales en su README.

## D048 — Tarjetas alineadas en cada fila · 2026-11-01

**Origen:** el usuario solicita que los elementos equivalentes dispuestos lado a lado tengan el mismo tamaño de manera consistente.

**Decisión:** estirar las tarjetas de cada fila para igualar su altura, manteniendo columnas iguales para grupos comparables. Aplicar la regla a ambas presentaciones y agregarla a las convenciones y verificadores del curso; mantener el diseño independiente de columnas con código o contenido distinto.

## D049 — Revelado automático y logotipos de herramientas · 2026-11-01

**Origen:** el usuario pide mostrar una por una las filas de la diapositiva 5 sin interacción e incluir logotipos correctos.

**Decisión:** integrar recursos SVG y PNG de los repositorios oficiales como archivos locales. Al entrar a la diapositiva, revelar cada fila automáticamente con una separación de 400 ms; reiniciar al regresar. Respetar movimiento reducido y mostrar todas las filas en la exportación PDF. Registrar fuentes y atribuciones en el README y verificar la secuencia y carga de imágenes.


## D050 — Introducir Maven y el POM antes de configurar JUnit · 2026-11-01

**Origen:** el usuario pide explicar brevemente Maven y su configuración, enfocando las partes relevantes mediante animación.

**Decisión:** agregar una diapositiva de Maven como herramienta de dependencias, compilación y pruebas, y otra con un fragmento real del POM, enfocando progresivamente la identidad del proyecto y sus propiedades. Aclarar que el archivo es XML declarativo y que el fragmento omite el resto. Mantener después las diapositivas de estructura del proyecto, BOM, dependencia y Surefire.

## D051 — Resaltado de código Tokyo Night · 2026-11-01

**Origen:** el usuario solicita una paleta de código más acorde con el fondo oscuro de las presentaciones.

**Decisión:** configurar el tema integrado Tokyo Night de Shiki en las dos presentaciones, conservando el fondo slate, el foco progresivo y la legibilidad del código. Mantener una paleta común para las próximas presentaciones.


## D052 — Mostrar el método probado y su ejecución · 2026-11-01

**Origen:** el usuario solicita conocer el contenido de quantityToTrade y mostrar la ejecución con la técnica de panel verde de la introducción.

**Decisión:** incorporar el método real de RebalanceCalculator antes de presentar su prueba, enfocando parámetros, cálculo y significado del signo. Sustituir el resumen estático por una sesión PTY real de Maven reproducida con asciinema al 50 %, con panel de resultado generado desde el XML real de Surefire después de la ejecución. Conservar una captura estática para PDF y agregar verificación de reproducción, pausa y resultado.

## D053 — Iconos para la configuración de dependencias · 2026-11-01

**Origen:** el usuario solicita un icono JAR y representaciones de Maven y Gradle en la diapositiva 6.

**Decisión:** añadir una ilustración local de archivo JAR y logotipos locales de Maven y Gradle en las dos tarjetas, conservando sus dimensiones iguales y los revelados existentes. Registrar las fuentes y comprobar la carga de las imágenes.

## D054 — Ubicación del código y de su prueba · 2026-11-01

**Origen:** el usuario solicita omitir la aclaración de actividades no calificadas y mostrar la estructura de archivos cerca del método probado.

**Decisión:** quitar la aclaración visible de las dos presentaciones; la práctica sigue siendo opcional. Agregar junto al método quantityToTrade un esquema de las rutas de producción y prueba bajo el mismo paquete, con notas explicativas.

## D055 — Contexto de archivo junto a fragmentos de código · 2026-11-01

**Origen:** el usuario propone mostrar la ubicación de los ejemplos de código y pide una revisión en consejo.

**Decisión:** conservar el árbol completo donde se introduce la estructura y usar rutas compactas junto a los demás fragmentos de archivo en ambas presentaciones. La elipsis indica segmentos de paquete omitidos. En las transiciones de Kata Zero distinguir las etapas y aclarar cuándo el defecto se reconstruye en una copia temporal. No etiquetar diagramas ni grabaciones de terminal como archivos fuente.

## D056 — Rutas visuales de archivo · 2026-11-01

**Origen:** el usuario pide una presentación más atractiva de las rutas junto al código.

**Decisión:** mostrar las rutas como pestañas de editor con icono discreto, borde mint y fondo en degradado, y armonizar el árbol de archivos con ese diseño. Mantener el texto legible, las rutas fieles y el espacio del código.

## D057 — Cabeceras de código con estilo de editor · 2026-11-01

**Origen:** el usuario busca consistencia con un editor sin reproducir una interfaz completa.

**Decisión:** presentar nombre de archivo y ruta en una cabecera compacta común a las dos presentaciones; conservar el resaltado Tokyo Night, las transiciones y las explicaciones sobre fragmentos y copias. Evitar barras de herramientas y paneles decorativos.

## D058 — Explorador del proyecto con estilo consistente · 2026-11-01

**Origen:** el usuario propone armonizar la diapositiva del árbol de archivos con las cabeceras de editor.

**Decisión:** identificar el árbol como explorador del proyecto y mostrar su carpeta raíz con la misma cabecera visual de las diapositivas de código, sin simular controles de editor.

## D059 — Explorador visual para el árbol del proyecto · 2026-11-01

**Origen:** el usuario aclara que desea rediseñar toda la diapositiva del árbol y solicita una revisión en consejo.

**Decisión:** sustituir el bloque monoespaciado por un explorador visual protagonista, con carpetas de paquete agrupadas explícitamente y tres focos coordinados: POM, producción y prueba. Mantener visibles todos los nodos, revelar sus explicaciones por clic, conservar texto además de color y mostrar todo en el PDF.

## D060 — Carpetas desplegables en el explorador · 2026-11-01

**Origen:** el usuario solicita una jerarquía de carpetas más reconocible, inspirada en el explorador de IntelliJ IDEA.

**Decisión:** mostrar src, main, test y java como carpetas anidadas y desplegables, con guías de indentación y el paquete agrupado. Utilizar controles nativos de HTML accesibles por teclado, abiertos inicialmente y también en el PDF; conservar los tres focos y evitar que un clic de carpeta avance la presentación.

## D061 — Historial de Git por cambios coherentes · 2026-11-01

**Origen:** el usuario pide mantener en adelante un historial de Git más útil para revisar o recuperar cambios.

**Decisión:** agrupar el trabajo en commits pequeños y coherentes por tema o hito, con mensajes descriptivos, al cerrar cambios autorizados. Conservar las decisiones y las verificaciones relevantes; no subir al remoto ni alterar el historial existente sin que se solicite.


## D062 — Recuperar el código original y ajustar reproducción · 2026-11-01

**Origen:** el usuario pregunta por el código original de la primera presentación y solicita acelerar sus grabaciones a 0.75×.

**Decisión:** volver a mostrar fragmentos fieles del main original después del ejemplo de acciones completas y antes del requisito fraccionario, señalando las partes omitidas. Cambiar a 0.75× las grabaciones de la introducción y actualizar su comprobación y documentación. La segunda presentación conserva su velocidad.

## D063 — Explicar la cuenta antes de la demostración · 2026-11-01

**Origen:** al preparar la grabación, el usuario señala que el diagrama abstracto de la segunda diapositiva no se entiende.

**Decisión:** sustituirlo por los datos concretos de la grabación: 10 acciones de cada empresa a 100 USD, objetivo de 40/60 del valor de la cuenta y propuesta de vender y comprar dos acciones. Mantener una frase directa y la ejecución real debajo; mejorar tamaño y contraste.

## D064 — Explicar la propuesta de rebalanceo · 2026-11-01

**Origen:** el usuario acepta convertir la tercera diapositiva en una explicación de por qué se proponen las operaciones.

**Decisión:** mostrar el cálculo del 40 % y 60 % de la cuenta y las cantidades objetivo, comparándolas con las diez acciones disponibles de cada empresa.


## D065 — Mostrar el cálculo desde la versión original · 2026-11-01

**Origen:** el usuario solicita que quantityToTrade exista desde el principio y que la primera presentación muestre brevemente una prueba en vez de introducir una extracción.

**Decisión:** separar el cálculo en RebalanceCalculator en las versiones original y fraccionaria ingenua; conservar la división entera y los mismos resultados. Presentar el método desde el inicio y sustituir la transición de extracción por un vistazo a @Test y assertEquals. Mantener el detalle para la segunda presentación y regenerar las demostraciones.

## D066 — Ajustes finales del consejo para la introducción · 2026-11-01

**Origen:** el usuario acepta los ajustes pequeños de la revisión final.

**Decisión:** conservar firma y llaves en ambos lados de la animación de corrección; precisar que cambia el tipo de retorno y la variable targetShares; explicar brevemente la tolerancia y eliminar de las notas la extracción que ya no ocurre. Evitar repetir la explicación de la estructura de prueba al presentar las dos expectativas originales.

## D067 — Conectar las primeras pruebas · 2026-11-01

**Decisión:** retomar la prueba de compra antes de añadir la venta, documentar brevemente el cálculo y mostrar los parámetros enteros al explicar la división.

## D068 — Revelar la segunda prueba · 2026-11-01

**Decisión:** mantener visible la prueba de compra y revelar la venta al avanzar; explicar los nombres en español y conservar los identificadores del código.

## D069 — Comentarios en español en las pruebas · 2026-11-01

**Decisión:** explicar con comentarios breves en español qué comprueba cada prueba, junto al código, en lugar de traducir nombres en las leyendas.

## D070 — Explicar la prueba fraccionaria · 2026-11-01

**Decisión:** agregar un comentario breve en español a la prueba fraccionaria en la diapositiva y en su fuente.

## D071 — Precisar el nombre de la prueba fraccionaria · 2026-11-01

**Decisión:** llamar calculatesFractionalQuantityToSell a la prueba porque verifica la cantidad propuesta para vender.
