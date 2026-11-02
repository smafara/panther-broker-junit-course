# Pruebas unitarias con JUnit 6: un simulador de inversión fraccionada

Curso de servicio social para estudiantes de México. Proyecto: **Panther Broker**. Modalidad: videos con práctica opcional, sin entregas ni calificaciones. Tecnologías previstas: JDK 25, JUnit 6 y Mockito 5.

JDK obligatorio para todos los ejemplos y verificaciones: **`25.0.5.0+8-zulu` de SDKMAN**. Está fijado en `.sdkmanrc`; activar con `sdk env` y usar la misma instalación en el IDE.

## Ruta acotada vigente · 2026-11-02

Esta ruta sustituye la secuencia y la estimación de 16 videos que se conservan abajo como referencia histórica. Panther Broker sirve para enseñar pruebas: no construiremos un intermediario completo. El contrato financiero detallado anterior queda fuera del alcance obligatorio.

1. Introducción a las pruebas unitarias con JUnit — Kata Zero, existente.
2. Primeros pasos con JUnit — configuración y AAA, existente.
3. Comprobar resultados con JUnit — esperado, obtenido, fuerza de una comprobación y diagnóstico.
4. Elegir buenos casos — ejemplos, fronteras y regresiones.
5. Comprobar entradas inválidas — excepciones y estado conservado.
6. Preparar pruebas independientes — fixtures; assertAll cuando ayude.
7. Una prueba con varios datos — parametrización centrada en CsvSource.
8. Desarrollar una regla con TDD — rojo, verde y refactorización.
9. Controlar dependencias — constructor y stub manual.
10. Simular dependencias con Mockito — respuestas y una colaboración significativa.
11. Refactorizar código existente — caracterización y red de regresión.

Meta: 11 videos; dividir Mockito solo si el ensayo lo requiere, para un total de 12. Duración pendiente de ensayos. Sin lecciones dedicadas a BigDecimal, Clock, comisiones, conversión o impuestos. Mantener calculadora, portafolio pequeño y un proveedor externo como máximo.

Presentación 3: [material](presentation/comprobar-resultados-junit/README.md). Los fragmentos y grabaciones usan los proyectos Maven before/after; el defecto intencional de porcentaje se reconstruye únicamente en una copia temporal.

## Plan anterior — referencia histórica

## Lección cero — Un cambio que parecía funcionar · 8 minutos

Introducción narrativa en siete momentos: programa de acciones completas; requisito de fracciones; cambio de int a double; el caso manual habitual sigue funcionando; otros datos revelan la división entera; pruebas que guardan expectativas y detectan el caso omitido; presentación del contenido del curso.

No se enseñan todavía arquitectura, AAA ni refactorización. Se muestran salidas reales: dos pruebas originales verdes, la suite ampliada con un caso rojo y tres pruebas verdes después de corregir. Se aclara que una suite necesita ejemplos adecuados; automatizar solo el caso habitual no habría encontrado el defecto.

Ver [Kata Zero](kata-zero/README.md), [guion](kata-zero/docs/GUION.md) y [presentación](presentation/intro-junit-kata-zero/README.md). La precisión monetaria con BigDecimal y los componentes de una prueba se desarrollan después, en el módulo 1.

## Público, idioma y objetivos

Se requieren métodos, clases, constructores, interfaces, excepciones y colecciones en Java. Explicar Maven, records y BigDecimal cuando aparecen. No se requieren conocimientos de bolsa, contabilidad o impuestos ni experiencia invirtiendo.

La narración, los títulos, las tarjetas de requisitos, el README, los mensajes de las pruebas y las soluciones serán en español de México. Mantener identificadores Java en inglés de forma consistente y usar @DisplayName para expresar comportamientos en español. Ejemplo: buysFractionalShares con @DisplayName("Compra una fracción sin gastar más del saldo disponible").

Usar «computadora», «archivo», «saldo», «tipo de cambio», «comisión» y «acciones fraccionadas». Explicar cada término técnico al introducirlo: assertion como comprobación; stub como sustituto con respuesta preparada; mock como objeto simulado que permite configurar respuestas y verificar llamadas. Presentar Arrange–Act–Assert como Preparar–Ejecutar–Comprobar.

Escribir siempre MXN o USD junto a los montos. En el código usar cadenas como "1000.00", sin separadores de miles. Explicar que comprar un instrumento estadounidense desde México involucra dos monedas. Mostrar instrucciones para Windows, macOS y Linux: mvnw.cmd test y ./mvnw test.

Al terminar, el estudiante podrá escribir y diagnosticar pruebas, elegir casos y fronteras, preparar estado independiente, comprobar excepciones y rechazos, parametrizar ejemplos, simular dependencias, controlar el tiempo y refactorizar con una red de pruebas.

## Investigación y alcance

Fintual Acciones México anuncia acciones y ETFs estadounidenses completos o fraccionados desde 1 USD, sin comisión por operación ni administración y con diferencial cambiario de 0.5%. Son condiciones de Acciones; sus fondos son productos distintos. [Fintual Acciones](https://fintual.mx/acciones/)

GBM Trading USA publica una comisión de 0.25% por compra o venta. Su experiencia actual separa la conversión de pesos a dólares de las operaciones con instrumentos. [Comisión](https://gbm.com/faqs/existe-alguna-comision-por-invertir-en-trading-usa/), [actualizaciones de GBM](https://gbm.com/faqs)

El proyecto toma ese flujo como inspiración: saldo MXN → conversión → saldo USD → compra. Sus reglas son decisiones didácticas propias. Mantener depósitos simulados, conversión, vista previa, compras y ventas parciales o totales. Dejar impuestos, SPEI, RFC/CLABE, margen, dividendos y algoritmos de inversión automática fuera del curso principal.

## Contrato del simulador

1. Los depósitos positivos aumentan el saldo MXN. La conversión consume MXN y acredita USD, conservando ambos saldos por separado.
2. El tipo de cambio se expresa en pesos por dólar. Fórmula didáctica: tipo ofrecido = referencia × (1 + diferencial); dólares = pesos / tipo ofrecido. No atribuir esta implementación a un intermediario real.
3. Los saldos usan dos decimales. La conversión acredita dólares redondeados hacia abajo; el residuo queda identificado en el comprobante y no se representa como dinero gastable.
4. El importe de compra es el monto destinado al instrumento, antes de comisión. Cantidad = importe / precio, redondeada hacia abajo a seis decimales. Importe ejecutado = cantidad × precio, redondeado a centavos con HALF_EVEN. Comisión = importe ejecutado × tasa, redondeada igual. Cargo = importe ejecutado + comisión.
5. Las políticas ficticias ZERO y STANDARD cobran 0% y 0.25%. No son una tabla combinada de Fintual y GBM. El simulador omite impuestos.
6. La venta acepta una cantidad positiva con hasta seis decimales, sin exceder la posición disponible, y acredita importe menos comisión.
7. Los datos inválidos producen excepciones. Los rechazos previstos devuelven un resultado con motivo. Una operación rechazada conserva saldo y posiciones y no publica un evento de éxito.
8. Se simula una ejecución completa e inmediata al precio suministrado. No se modelan órdenes pendientes, liquidez ni liquidación bursátil.
9. Las cotizaciones incluyen símbolo, precio USD positivo e Instant. Menos de 30 segundos de antigüedad es válido; exactamente 30 segundos ya es vencido. Rechazar fechas futuras.

Construir BigDecimal con cadenas. equals compara valor y escala; compareTo permite comparar el valor numérico. [Documentación JDK 25](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigDecimal.html)

Ejemplo recurrente: saldo 50.00 USD; compra de 40.00 USD a 125.00 USD por acción. Cantidad 0.320000; comisión STANDARD 0.10 USD; cargo 40.10 USD; saldo restante 9.90 USD. Con solo 40.00 USD disponibles, rechazar sin modificar el estado.

## Módulo 1. De revisar la consola a comprobar resultados

### 1.1 — ¿Y si el cálculo de tu saldo está mal? · 9 minutos

**Objetivo:** Distinguir observar una salida de verificar un resultado.

**Guion:** 0–2: explicar una acción fraccionada; 2–4: mostrar 0.1 + 0.2; 4–6: introducir un error de porcentaje que parece razonable en consola; 6–8: presentar BigDecimal y las reglas de redondeo; 8–9: contrastar esperado y obtenido.

**Pruébalo tú:** Anotar cantidad, comisión y cargo esperados para tres compras. Explicar qué dato revela el error. No pedir todavía JUnit.

### 1.2 — Tu primera prueba con JUnit 6 · 15 minutos

**Objetivo:** Ejecutar una prueba e interpretar su falla.

**Guion:** 0–3: revisar JDK y POM preparado; 3–5: explicar carpetas y Jupiter; 5–9: escribir @Test con Preparar–Ejecutar–Comprobar; 9–12: alterar el divisor y leer expected, actual y la línea señalada; 12–14: corregir y ejecutar Maven; 14–15: reto.

**Pruébalo tú:** Comprobar 40.00 / 125.00 = 0.320000 y 10.00 / 3.00 = 3.333333. Verificar seis decimales.

### 1.3 — Comprueba todo el desglose con assertAll · 12 minutos

**Objetivo:** Comprobar un resultado completo y entender igualdad y escala.

**Guion:** Comparar 0.32 y 0.320000; probar el comprobante recurrente; romper comisión y saldo; agrupar comprobaciones independientes con assertAll; añadir un mensaje de falla en español.

**Pruébalo tú:** Agregar una división no exacta y comprobar cantidad, importe, comisión, cargo y saldo. No copiar la fórmula de producción dentro de la prueba.

## Módulo 2. Saldo, excepciones y pruebas independientes

### 2.1 — Que una prueba no se gaste el saldo de otra · 11 minutos

**Objetivo:** Comprender la instancia por método y preparar objetos nuevos.

**Guion:** Escribir depósitos y cargos con preparación repetida; extraer una cuenta nueva a @BeforeEach; contrastar con una cuenta static compartida; explicar usos concretos de @BeforeAll y @AfterEach.

**Pruébalo tú:** Reparar pruebas con saldo compartido. Deben pasar individualmente y en conjunto sin depender del orden.

### 2.2 — Rechazar una operación sin alterar el saldo · 12 minutos

**Objetivo:** Comprobar excepciones y estado conservado.

**Guion:** Usar assertThrows con depósitos de cero y negativos; intentar vender 0.500000 acciones teniendo 0.400000; capturar la excepción y comprobar símbolo y faltante; verificar saldo y posición intactos.

**Pruébalo tú:** Probar una venta excesiva, una compra negativa y la frontera válida de vender toda la posición.

### 2.3 — Organiza tus escenarios con @Nested · 10 minutos

**Objetivo:** Estructurar pruebas por estado y comportamiento.

**Guion:** Separar cuenta vacía, cuenta con saldo y cuenta con acciones; mostrar preparación exterior e interior; usar @DisplayName en español y @Disabled con un motivo. Las pruebas omitidas no aportan evidencia de éxito.

**Pruébalo tú:** Organizar ventas parciales y totales conservando independencia y comportamiento.

## Módulo 3. Más casos con menos repetición

### 3.1 — Una prueba, varios datos de entrada · 10 minutos

**Objetivo:** Usar @ParameterizedTest, @ValueSource y @NullAndEmptySource.

**Guion:** Explicar ticker como símbolo de cotización; agrupar símbolos nulos, vacíos y en blanco; separar un símbolo no admitido por el catálogo. Una expresión regular no demuestra que una acción exista en bolsa.

**Pruébalo tú:** Parametrizar entradas inválidas y agregar un símbolo admitido.

### 3.2 — Comisiones y redondeos en una tabla · 12 minutos

**Objetivo:** Convertir ejemplos y fronteras en @CsvSource.

**Guion:** Introducir enums y BigDecimal; escribir tabla con bloque de texto y encabezados. Casos STANDARD: 40.00 → 0.10; 1.00 → 0.00; 2.00 → 0.00; 6.00 → 0.02. Explicar los empates HALF_EVEN de 0.005 y 0.015. ZERO con 40.00 → 0.00. Mostrar @EnumSource si queda tiempo.

**Pruébalo tú:** Agregar valores inmediatamente anteriores y posteriores a una frontera y explicar el cambio de comisión.

### 3.3 — Portafolios completos con @MethodSource · 12 minutos

**Objetivo:** Suministrar objetos complejos sin compartir estado mutable.

**Guion:** Preparar Stream<Arguments> para ventas parciales, totales y excesivas; dar nombres con Named; crear una cuenta nueva por caso; comprobar comprobante y estado final.

**Pruébalo tú:** Agregar otro instrumento y demostrar que vender uno conserva intacto el otro.

## Módulo 4. Probar sin conectarse al mercado

### 4.1 — Controla las cotizaciones desde tus pruebas · 14 minutos

**Objetivo:** Introducir dependencias por constructor.

**Guion:** Mostrar la inestabilidad de una cotización cambiante; extraer QuoteProvider; escribir un stub pequeño; construir TradeService explícitamente; distinguir cálculos y servicios externos; explicar una vez el agente de Mockito.

**Pruébalo tú:** Recibir FxQuoteProvider por constructor y usar una respuesta fija, sin HTTP.

### 4.2 — Simula precios y fallas con Mockito · 14 minutos

**Objetivo:** Usar MockitoExtension, @Mock, when/thenReturn y when/thenThrow.

**Guion:** Usar proveedor simulado y cuenta real en memoria; comprobar la compra recurrente; probar cotización ausente y falla del proveedor; interpretar un diagnóstico de configuración. Mostrar @InjectMocks después de comprender el constructor.

**Pruébalo tú:** Simular una falla externa y comprobar saldo y posiciones intactos.

### 4.3 — Verifica qué comprobante se publica · 12 minutos

**Objetivo:** Verificar colaboraciones con verify y ArgumentCaptor.

**Guion:** Recibir TradeEventPublisher; capturar TradeReceipt de una compra exitosa; comprobar símbolo, cantidad y cargo; verificar que un rechazo no publica éxito. Usar comprobaciones de estado para saldo e interacciones para publicación.

**Pruébalo tú:** Capturar el comprobante de una venta parcial y comprobar cantidad e ingreso neto.

## Módulo 5. Cambiar código con confianza

### 5.1 — Primero la prueba: agrega un límite de compra · 15 minutos

**Objetivo:** Completar ciclos pequeños de TDD: rojo, verde y refactorización.

**Regla:** Rechazar compras que exceden el límite por operación, antes de comisión; aceptar igualdad; no aplicar a ventas.

**Guion:** Ciclo 1: aceptar debajo del límite. Ciclo 2: rechazar arriba. Ciclo 3: aceptar igualdad. Refactorizar comparaciones repetidas con las pruebas en verde.

**Pruébalo tú:** Agregar la excepción para ventas y comprobar estado intacto ante un rechazo.

### 5.2 — Pruebas que funcionan a cualquier hora · 14 minutos

**Objetivo:** Controlar tiempo y fronteras con Clock.

**Guion:** Sustituir Instant.now() por Clock inyectado; usar Clock.fixed; probar 29, 30 y 31 segundos y fechas futuras; cambiar < por <= y observar qué prueba falla. Explicar que ejecutar una línea no demuestra que calcule bien.

**Pruébalo tú:** Agregar casos inmediatamente antes y exactamente en el vencimiento con precisión menor a un segundo.

### 5.3 — Refactoriza código existente con una red de pruebas · 18 minutos

**Objetivo:** Separar cambios de estructura y comportamiento.

**Guion:** Usar una versión desordenada del servicio conocido; caracterizar divisiones, redondeos, saldo insuficiente y ventas; contrastar resultados observados con el contrato; extraer métodos y ejecutar pruebas tras cada cambio. Corregir defectos conocidos en cambios separados con pruebas de regresión.

**Pruébalo tú:** Refactorizar otro método familiar. Proporcionar solución comentada en video.

## Producción y materiales

Duración estimada: **198 minutos en 16 videos**, incluyendo Kata Zero. La introducción cierra presentando la ruta del curso. Los demás videos presentan una regla, piden predecir un resultado, muestran una falla útil y terminan con práctica opcional de 5–15 minutos. Incluir soluciones sin calificación y criterios observables.

Entregar README y guiones en español de México, instrucciones para los tres sistemas operativos y Maven Wrapper. Etiquetas inmutables por episodio: ep-1.2-start, ep-1.2-end y ep-1.2-solution. Cada end pasa toda la suite; identificar fallas intencionales. Se puede seguir el curso solo viendo los videos.

Extensiones opcionales: calendario de mercado, pruebas de mutación y diferencias entre pruebas unitarias y de integración.

## Precisiones de contexto y versiones

NYSE opera su sesión regular de 09:30 a 16:00 hora de Nueva York, con días inhábiles y cierres anticipados. Usar America/New_York; no fijar un horario anual de CDMX. Los horarios del intermediario pueden diferir. [NYSE](https://www.nyse.com/markets/hours-calendars)

GBM puede dejar órdenes pendientes fuera de horario; una orden limitada requiere contraparte. La ejecución inmediata del curso es una simplificación. [Órdenes GBM](https://gbm.com/faqs/con-que-tipo-de-ordenes-existen-en-trading-usa/)

No tratar CETES como ETF estadounidense, importar reglas wash-sale como si fueran mexicanas ni presentar retenciones fiscales universales. Las explicaciones y fuentes de estas correcciones se conservan en [la investigación completa en inglés](COURSEWORK.en.md).

Versiones identificadas: JUnit 6.1.3, Mockito 5.24.0 y Surefire 3.6.1, junto con JDK 25 solicitado. [JUnit](https://docs.junit.org/6.1.3/overview.html), [Mockito](https://github.com/mockito/mockito/releases/tag/v5.24.0), [Surefire](https://github.com/apache/maven-surefire/releases)

El agente de Mockito requiere configuración tanto en Maven como en el IDE, o delegar pruebas a Maven. Seguir las instrucciones oficiales para Java 21+. [Mockito](https://javadoc.io/static/org.mockito/mockito-core/5.24.0/org.mockito/org/mockito/Mockito.html#0.3)

Kata Zero ya cuenta con proyectos Java ejecutables y construcción verificada con Zulu 25.0.5+8. El resto del curso permanece en diseño. Antes de grabar, ejecutar las comprobaciones también desde el IDE elegido. La evidencia de terminal se registra en [VALIDACION.md](kata-zero/docs/VALIDACION.md).
