---
theme: default
title: 'Introducción a las pruebas unitarias con JUnit'
info: 'Un video introductorio · Panther Broker · Servicio social · México'
author: 'Panther Broker'
lang: es-MX
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 1280
transition: slide-left
highlighter: shiki
lineNumbers: true
codeCopy: false
magicMoveDuration: 550
fonts:
  provider: none
  sans: 'Arial'
  mono: 'Consolas'
drawings:
  persist: false
mdc: false
class: cover
---

# Introducción a las pruebas unitarias con JUnit

<!--
Entrada: presentar la historia de un cambio pequeño que dejó un defecto. Cuenta y precios son ficticios.
Transición: primero mostrar el programa antes del requisito nuevo, sin explicar todavía JUnit.
-->

---

# Supongamos que tenemos un programa: Panther Broker

<p class="intro-purpose">Panther Broker propone qué comprar y vender para repartir el valor de una cuenta como queremos.</p>

<div class="intro-flow">
  <div><strong>Cuenta actual</strong><span>10 META + 10 AAPL<br>100 USD por acción</span></div>
  <b aria-hidden="true">→</b>
  <div><strong>Lo que queremos</strong><span>40 % del valor en META<br>60 % en AAPL</span></div>
  <b aria-hidden="true">→</b>
  <div><strong>Propuesta</strong><span>Vender 2 META<br>Comprar 2 AAPL</span></div>
</div>

<TerminalRecording v-click="1" :reveal-at="1" name="intro-whole-shares" alt="Ejecución real de Panther Broker: consulta de la cuenta y propuesta de rebalanceo con acciones completas" />

<!--
Entrada: explicar el ejemplo de izquierda a derecha: una cuenta con dos acciones, el porcentaje del valor deseado para cada una y las operaciones que propone el programa. No ejecuta operaciones.
Clic: mostrar la ejecución real de la versión original: consultar la cuenta, ingresar objetivos y recibir la propuesta de acciones completas.
Transición: usar la cuenta de la demostración para explicar los porcentajes objetivo.
-->

---

# ¿Por qué vender 2 y comprar 2?

<div class="split equal">
<div>
<p class="lead">La cuenta vale <strong>2000 USD</strong>.<br>Cada acción cuesta <strong>100 USD</strong>.</p>
<div class="card" style="margin-top:24px"><h3>Comparamos con lo que tenemos</h3><p>Tenemos 10 acciones de cada empresa. El programa solo propone operaciones.</p></div>
</div>
<div class="receipt">
<div class="receipt-row"><span>META · 40 %</span><b>800 USD → 8 acciones</b></div>
<div class="receipt-row"><span>AAPL · 60 %</span><b>1200 USD → 12 acciones</b></div>
<div class="receipt-row total"><span>Plan</span><b>Vender 2 META</b></div>
<div class="receipt-row"><span></span><b>Comprar 2 AAPL</b></div>
</div>
</div>

<!--
Entrada: calcular 40 % y 60 % de 2000 USD, dividir cada resultado entre el precio de 100 USD y comparar con las 10 acciones disponibles de cada empresa.
Transición: mostrar el código que produjo esta propuesta.
-->

---

# El código original de Panther Broker

<p class="source-path" data-file="RebalanceCalculator.java">kata-zero/before/src/main/java/…/RebalanceCalculator.java</p>

<div class="split code-compact">
<div>

```java {1-2|3-4|5|*}{lines:true}
static int quantityToTrade(int totalValue, int targetPercent,
                           int price, int currentQuantity) {
    int targetValue = totalValue * targetPercent / 100;
    int targetShares = targetValue / price;
    return targetShares - currentQuantity;
}
```

</div>
<div class="stack">
<div class="card"><h3>Recibe</h3><p>Valor de la cuenta, objetivo, precio y cantidad actual.</p></div>
<div class="card purple" v-click><h3>Devuelve</h3><p>Cuántas acciones completas comprar o vender.</p></div>
</div>
</div>
<p class="caption">Método original; se omiten paquete y clase. El menú lo llama para cada acción.</p>

<!--
Entrada: mostrar el método que utiliza el menú para calcular la propuesta de acciones completas.
Focos: entradas, cálculo y diferencia. Una cantidad negativa indica venta.
Transición: introducir la compra y venta de fracciones como requisito nuevo.
-->

---
transition: fade
---

# Ahora también queremos comprar y vender fracciones

<p class="lead">La cantidad ya no tiene que ser 2, 5 o 10.<br>También puede ser <strong>3.333333 acciones</strong>.</p>

<div class="diagram" style="margin-top:30px">

```mermaid {theme: 'base', scale: 0.95}
flowchart LR
  A["Cuenta y precios"] --> B["Calcular rebalanceo"]
  B --> C["Compras y ventas\ncon cantidades fraccionadas"]
```

</div>
<div class="card purple" style="margin-top:26px" v-click><h3>«Entonces cambio int por double»</h3><p>Una adaptación que parece pequeña. ¿Será suficiente?</p></div>

<!--
Entrada: introducir el requisito sin hablar de precisión financiera avanzada.
Clic: representar el razonamiento de quien adapta el programa. Transición: mostrar exactamente ese cambio.
-->

---

# Cambiamos el tipo de la cantidad

<p class="source-path" data-file="RebalanceCalculator.java">kata-zero/before y after/01-naive-fractions · src/main/java/…/RebalanceCalculator.java</p>

<div class="split code-compact">
<div>

````md magic-move {duration:600, lines:true}
```java
static int quantityToTrade(...) {
    int targetValue = totalValue * targetPercent / 100;
    int targetShares = targetValue / price;
    return targetShares - currentQuantity;
}
```
```java
static double quantityToTrade(...) {
    int targetValue = totalValue * targetPercent / 100;
    double targetShares = targetValue / price;
    return targetShares - currentQuantity;
}
```
````

</div>
<div class="stack">
<div class="card"><h3>Antes</h3><p>Cantidades completas en variables int.</p></div>
<div class="card purple"><h3>Después</h3><p>El método y la cantidad objetivo ahora aceptan decimales.</p></div>
</div>
</div>
<p class="caption">Fragmento del método: se omiten los parámetros; los importes y precios siguen siendo enteros.</p>

<!--
Entrada: un clic transforma int en double. No señalar todavía el tipo de los operandos de la división.
Transición: hacemos lo habitual: volver a ejecutar con los mismos datos y comparar a mano.
-->

---

# El ejemplo de siempre sigue funcionando

<TerminalRecording name="manual-original" alt="Grabación real de la consola con el ejemplo habitual: vender dos META y comprar dos AAPL" />

<div class="split equal" style="margin-top:22px">
<div class="card success"><h3>Vender 2 · Comprar 2</h3><p>Coincide con lo que ya esperábamos.</p></div>
<div class="card" v-click><h3>«Listo, ya acepta fracciones»</h3><p>Pero todavía no probamos un resultado fraccionario.</p></div>
</div>

<!--
Entrada: reproducir la grabación completa del programa adaptado: comando, menú, cuenta, objetivos 40 y 60, cálculo y salida. No simular una terminal con texto inventado.
Clic: mostrar el salto de confianza. Transición: cambiar un precio, manteniendo la misma cuenta.
-->

---

# Solo cambia META: de 100 a 150 USD

<div class="trio">
<div class="card" v-click><div class="label">TOTAL DE LA CUENTA</div><h2>2500 USD</h2><p>10 × 150 + 10 × 100.</p></div>
<div class="card purple" v-click><div class="label">OBJETIVO META · 40%</div><h2>1000 USD</h2><p>1000 ÷ 150 = 6.666666… acciones.</p></div>
<div class="card success" v-click><div class="label">VENTA ESPERADA</div><h2>≈ 3.333333</h2><p>Tenemos 10; necesitamos conservar 6.666666…</p></div>
</div>
<p class="lead" style="margin-top:30px">Ese es el resultado esperado. <strong>Lo calculamos antes de ejecutar.</strong></p>

<!--
Entrada: una operación por clic y tiempo para seguirla. Se proporciona el esperado, no se pide resolver un acertijo.
Transición: ejecutar el programa adaptado con estos datos nuevos.
-->

---

# Esperábamos vender ≈ 3.333333. Propone vender 4.

<TerminalRecording name="manual-fractional" alt="Grabación real del programa adaptado con META a150USD: propone vender cuatro acciones" />

<div class="card warning" style="margin-top:24px" v-click><h3>El programa ejecuta, pero no cumple el requisito nuevo</h3><p>Ahora tenemos que volver a revisar y repetir la comparación cada vez que cambiemos el código.</p></div>

<!--
Entrada: comparar explícitamente el esperado con la salida real. No llamar redondeo correcto a la pérdida de la fracción.
Transición: reconocer que ese caso podía haberse comprobado al cambiar el requisito, antes de dar la adaptación por terminada.
-->

---

# Pudimos y debimos detectar el error antes

<v-clicks>

- No podemos comprobar **todos los casos a mano** después de cada cambio.
- Una función nueva puede introducir errores o **romper lo que ya funcionaba**.
- Necesitamos guardar las comprobaciones **en código** y ejecutarlas automáticamente.
- Con datos y condiciones controladas, podemos repetirlas y obtener **el mismo resultado**.

</v-clicks>

<!--
Entrada: conectar con el caso fraccionario que faltó comprobar al adaptar el programa. No responsabilizar a quien aprende de anticipar todos los errores posibles.
Clics: explicar el límite de la revisión manual, el riesgo de regresión y la necesidad de comprobaciones programables y deterministas. Las pruebas requieren casos adecuados y condiciones controladas.
Transición: dar nombre a esta herramienta: pruebas unitarias.
-->

---

# Presentamos las pruebas unitarias

<p class="lead">Una comprobación automática de un comportamiento concreto de una pequeña parte del programa, como un método.</p>

<div class="trio" style="margin-top:30px">
<div class="card" v-click><h3>Datos conocidos</h3><p>Una cuenta, un precio y un porcentaje objetivo.</p></div>
<div class="card purple" v-click><h3>Una operación</h3><p>Calcular cuántas acciones comprar o vender.</p></div>
<div class="card success" v-click><h3>Un resultado esperado</h3><p>Comparar lo obtenido con lo que debería pasar.</p></div>
</div>

<p class="small" style="margin-top:26px" v-click>JUnit nos ayuda a escribir y ejecutar esas pruebas en Java.</p>

<!--
Entrada: dar nombre a la comparación que acabamos de hacer a mano: una prueba unitaria la convierte en una comprobación automática de una parte pequeña del código.
Clics: conectar datos, operación y resultado esperado con el cálculo de Panther Broker. Después, revelar la frase que presenta a JUnit. No introducir todavía anotaciones ni la estructura completa de una prueba.
Transición: guardar primero las expectativas del ejemplo habitual y ejecutarlas con JUnit.
-->

---

# Un primer vistazo a una prueba

<p class="source-path" data-file="OriginalExamplesTest.java">kata-zero/after/02-first-test/src/test/java/…/OriginalExamplesTest.java</p>

<p class="lead">Una prueba es un método que llama a nuestro cálculo y comprueba lo que devuelve.</p>

<div class="code-compact">

```java {1|2|3-5|*}{lines:true}
@Test
void buysTwoSharesWhenBelowTarget() {
    assertEquals(2.0,
        RebalanceCalculator.quantityToTrade(2000, 60, 100, 10),
        0.000001);
}
```

</div>
<p class="caption"><code>@Test</code> marca la prueba; <code>assertEquals</code> compara el resultado con lo esperado. Se omiten clase e imports.</p>

<!--
Entrada: presentar brevemente la anotación, el método de prueba y la comparación.
No desarrollar aún tolerancia ni anatomía completa; se profundiza en la segunda presentación.
Transición: mostrar las dos expectativas del ejemplo original.
-->

---

# Las pruebas que pudimos tener desde la versión int

<p class="source-path" data-file="OriginalExamplesTest.java">kata-zero/after/02-first-test/src/test/java/…/OriginalExamplesTest.java</p>

<div class="code-compact">

```java {1-6|8-13|*}{lines:true}
@Test
void sellsTwoSharesWhenAboveTarget() {
    assertEquals(-2.0,
        RebalanceCalculator.quantityToTrade(2000, 40, 100, 10),
        0.000001);
}

@Test
void buysTwoSharesWhenBelowTarget() {
    assertEquals(2.0,
        RebalanceCalculator.quantityToTrade(2000, 60, 100, 10),
        0.000001);
}
```

</div>
<p class="caption">El primer argumento es el esperado; el segundo, el resultado. Un número negativo indica una venta.</p>

<!--
Entrada: volver al contrato de acciones completas. Estas dos expectativas podían haberse guardado desde la primera versión; no afirmar que el main original ya tenía pruebas.
Clics: mostrar la venta esperada y después la compra esperada. Los ejemplos corresponden a OriginalExamplesTest; se omiten imports y DisplayName y se distribuyen las llamadas en varias líneas.
El menú ya utiliza el método, y la prueba puede llamarlo directamente. Usamos la firma actual compatible con la evolución fraccionaria; el detalle de la extracción y la tolerancia se explicará durante el curso.
Transición: ejecutar esos casos después del cambio a double para comprobar que el comportamiento anterior se conserva.
-->

---

# El cambio a double conserva los casos originales

<p class="small">Reutilizamos las expectativas de la versión entera después de agregar fracciones.</p>
<TerminalRecording name="tests-original-green" alt="Grabación real de JUnit: las dos pruebas del ejemplo habitual pasan aunque el defecto sigue presente" compact />
<div class="card warning" style="margin-top:22px" v-click><h3>Dos pruebas verdes todavía pueden omitir el defecto</h3><p>Repetir automáticamente el mismo caso entero no comprueba que funcionen las fracciones.</p></div>

<!--
Entrada: reproducir Maven y mostrar el resultado real de dos pruebas. Explicar que una suite necesita ejemplos adecuados: JUnit no descubre requisitos por sí solo.
Clic: hacer explícito por qué verde no equivale a corrección universal. Transición: agregar el caso que faltaba.
-->

---

# El requisito fraccionario necesita una prueba nueva

<p class="source-path" data-file="FractionalSharesTest.java">kata-zero/after/02-first-test/src/test/java/…/FractionalSharesTest.java</p>

<div class="code-compact">

```java {1|3|4|*}{lines:true}
@Test
void preservesFractionalSharesWhenSelling() {
    double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10);
    assertEquals(-3.333333, order, 0.000001);
}
```

</div>
<TerminalRecording v-click="4" :reveal-at="4" name="tests-fractional-red" alt="Grabación real de la suite con el nuevo caso fraccionario: se esperaba aproximadamente menos3.333333 y se obtuvo menos4" short />
<p class="caption">Esperado, resultado y tolerancia: 0.000001 permite comparar valores aproximados.</p>

<!--
Entrada: los focos señalan la llamada con datos nuevos y luego el esperado con tolerancia. No enseñar todavía toda la API de assertions.
Reproducir la grabación de Maven: las pruebas anteriores pasan y la nueva revela el defecto. Transición: explicar qué quedó del supuesto de enteros.
-->

---

# Guardar en double no cambia una división entre int

<p class="source-path" data-file="RebalanceCalculator.java">kata-zero/after/02-first-test/src/main/java/…/RebalanceCalculator.java · defecto reconstruido en copia temporal</p>

<div class="split code-compact">
<div>

````md magic-move {duration:650, lines:true}
```java
static double quantityToTrade(...) {
    int targetValue = totalValue * targetPercent / 100;
    double targetShares = targetValue / price;
    return targetShares - currentQuantity;
}
```
```java
int targetValue = totalValue * targetPercent / 100;
double targetShares = targetValue / (double) price;
return targetShares - currentQuantity;
```
````

</div>
<div class="stack">
<div class="card warning"><h3>1000 / 150</h3><p>Ambos operandos son int: primero se obtiene 6; después se guarda 6.0.</p></div>
<div class="card success"><h3>1000 / 150.0</h3><p>La división conserva una aproximación de la parte fraccionaria.</p></div>
</div>
</div>
<p class="caption">Usamos un ejemplo numérico pequeño para introducir pruebas. Este ejemplo simplificado aún no resuelve la precisión del dinero ni todas las operaciones fraccionarias.</p>

<!--
Entrada: explicar el orden: primero se calcula la expresión, después se asigna. Un clic transforma solo la división.
Corregimos el cálculo, sin cambiar lo que espera la prueba. Transición: volver a ejecutar toda la suite, no solo el caso nuevo.
-->

---

# Corregimos el cálculo. Todas las pruebas pasan.

<TerminalRecording name="tests-fixed-green" alt="Grabación real de Maven y JUnit después de corregir: las tres pruebas pasan" />

<div class="split equal" style="margin-top:22px">
<div class="card success"><h3>Tres casos comprobados</h3><p>El nuevo caso fraccionario forma parte de nuestra red de pruebas.</p></div>
<div class="card" v-click><h3>Detectarlo antes</h3><p>Incluir ese caso al adaptar el programa habría señalado el defecto antes de dar el cambio por terminado.</p></div>
</div>

<!--
Entrada: reproducir Maven de principio a fin y mostrar las tres pruebas verdes. No afirmar que la suite valida todos los posibles resultados.
Clic: conectar el beneficio con la historia inicial. Transición: anunciar lo que se aprenderá durante el curso.
-->

---
class: chapter
transition: fade
---

# Pruebas que explican.<br>Cambios con confianza.

<div style="margin-top:22px">
<span class="chip" v-click>Fundamentos de JUnit y de una prueba</span>
<span class="chip" v-click>Casos complejos y dependencias</span>
<span class="chip" v-click>Pruebas en el trabajo cotidiano</span>
</div>
<p class="lead" style="margin-top:26px">Seguiremos con ejemplos del simulador Panther Broker.<br>Videos y práctica opcional.</p>

<!--
Entrada: anunciar los temas del curso sin explicar sus técnicas todavía. Los nombres son una ruta, no prerrequisitos.
Salida: esta introducción motiva el curso; los detalles y la metodología se trabajan en las siguientes lecciones.
-->
