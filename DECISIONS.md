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
