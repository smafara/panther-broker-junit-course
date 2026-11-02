---
theme: default
title: 'Comprobar resultados con JUnit'
author: 'Panther Broker'
lang: es-MX
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 1280
transition: slide-left
highlighter: shiki
lineNumbers: true
codeCopy: false
fonts:
  provider: none
  sans: 'Arial'
  mono: 'Consolas'
class: cover
---

# Comprobar resultados con JUnit



<!--
Entrada: aprender qué demuestra una comprobación y cómo interpretar su resultado.
-->

---

# Retomemos nuestra prueba

<p class="source-path" data-file="RebalanceCalculatorTest.java">comprobar-resultados-junit/after/src/test/java/…/RebalanceCalculatorTest.java</p>

```java {lines:true}
// Compra dos acciones si está por debajo del objetivo.
@Test
void buysTwoSharesWhenBelowTarget() {
    double order = RebalanceCalculator.quantityToTrade(2000, 60, 100, 10);
    assertEquals(2.0, order, 0.000001);
}
```
<p class="lead">¿Qué demuestra esta comprobación?</p>

<!--
Retomar el caso conocido. Se omiten clase e imports; llamada abreviada respecto a las variables AAA del archivo real.
-->

---

# ¿Por qué esperamos comprar 2?

<div class="trio"><div class="card"><h3>Objetivo</h3><p>60 % de 2000 USD = 1200 USD.</p></div><div class="card purple" v-click><h3>Cantidad deseada</h3><p>1200 USD ÷ 100 USD = 12 acciones.</p></div><div class="card success" v-click><h3>Operación</h3><p>Tenemos 10. Faltan 2 acciones.</p></div></div>
<p class="lead" v-click>El esperado viene del requisito y de un ejemplo que podemos comprobar.</p>

<!--
Calcular el esperado independientemente. No copiar fórmulas de producción en la prueba.
-->

---

# Esperado, obtenido y margen permitido

```java {lines:true}
assertEquals(2.0, order, 0.000001);
```
<div class="trio"><div class="card"><h3>2.0</h3><p>La cantidad esperada.</p></div><div class="card purple" v-click><h3>order</h3><p>El resultado del método.</p></div><div class="card" v-click><h3>0.000001</h3><p>Diferencia absoluta permitida.</p></div></div>

<!--
Explicar orden de argumentos. Retomar margen al cerrar con fracciones.
-->

---

# Comprar no significa comprar la cantidad correcta

<p class="source-path" data-file="RebalanceCalculatorTest.java">comprobar-resultados-junit/after/src/test/java/…/RebalanceCalculatorTest.java</p>

```java {lines:true}
double order = RebalanceCalculator.quantityToTrade(2000, 60, 100, 10);
assertTrue(order > 0);
```
<div class="split"><div class="card success" v-click><h3>Devuelve 2</h3><p>La comprobación pasa.</p></div><div class="card warning" v-click><h3>Devuelve 200</h3><p>También pasa, aunque la cantidad es incorrecta.</p></div></div>

<!--
Fragmento de proposesPurchaseWhenBelowTarget. assertTrue sirve para contratos booleanos; aquí solo comprueba dirección.
-->

---

# Comprobemos lo que pide el requisito

```java {lines:true}
assertEquals(2.0, order, 0.000001);
```
<p class="lead">Esperamos dos acciones, no cualquier cantidad positiva.</p>
<div class="card purple" v-click><p>Una prueba útil distingue el resultado correcto de un error plausible.</p></div>

<!--
Transición: error intencional de porcentaje: dividir entre10 en lugar de100. Resultado110, positivo pero incorrecto.
-->

---

# Un defecto que la comprobación débil acepta

<p class="source-path" data-file="RebalanceCalculator.java">Defecto intencional en copia temporal; no forma parte de after.</p>

```java {lines:true}
int targetValue = totalValue * targetPercent / 10; // Debía ser 100.
double targetShares = targetValue / (double) price;
return targetShares - currentQuantity;
```
<TerminalRecording name="assertion-red" alt="Maven: la cantidad exacta falla y la comprobación positiva pasa" short />

<!--
Se omiten firma y clase. El defecto devuelve110. Salida real de Maven; no cambiar el esperado para que pase.
-->

---

# Leamos la falla

<div class="split"><div class="stack"><div class="card"><h3>Qué prueba</h3><p>buysTwoSharesWhenBelowTarget</p></div><div class="card warning" v-click><h3>Qué diferencia</h3><p>Esperado: 2.0<br>Obtenido: 110.0</p></div></div><div class="card purple"><h3>Dónde investigar</h3><p>JUnit indica el archivo y la línea de la comprobación.</p><p v-click>Revisamos requisito, datos, esperado e implementación.</p></div></div>

<!--
Volver a la ubicación que señala Maven. Rojo revela una discrepancia; también puede haber un error en la prueba.
-->

---

# Corregimos el cálculo y volvemos a ejecutar

```java {lines:true}
int targetValue = totalValue * targetPercent / 100;
```
<TerminalRecording name="assertion-green" alt="Maven: suite correcta después de restaurar el porcentaje" short />
<p class="caption">No cambiamos una expectativa justificada solo para obtener verde.</p>

<!--
Restaurar100. La suite final contiene el caso fraccionario que explicamos a continuación.
-->

---

# Una aproximación también necesita un límite

<p class="source-path" data-file="RebalanceCalculatorTest.java">comprobar-resultados-junit/after/src/test/java/…/RebalanceCalculatorTest.java</p>

```java {lines:true}
// Calcula cuántas acciones fraccionarias se deben vender.
double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10);
assertEquals(-3.333333, order, 0.000001);
```
<div class="split"><div class="card"><h3>Diferencia permitida</h3><p>−3.333333333… está suficientemente cerca de −3.333333.</p></div><div class="card purple"><h3>Tu turno</h3><p>Cuenta: 2000 USD. Objetivo: 50 %. Precio: 100 USD. Tenemos 10 acciones. Predice y comprueba la operación.</p></div></div>
<p class="caption">El margen no redondea ni representa una política financiera.</p>

<!--
Práctica esperado0: predecir antes de revelarlo verbalmente. Se omiten clase, imports y método del fragmento. Próxima lección: elegir buenos casos.
-->
