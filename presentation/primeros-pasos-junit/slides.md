---
theme: default
title: 'Primeros pasos con JUnit'
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

# Primeros pasos con JUnit

<!--
Entrada: recordar brevemente que Kata Zero convirtió una comparación manual en una prueba.
Transición: ampliar la mirada antes de volver a Java.
-->

---

# ¿Qué significa probar software?

<p class="lead">Comprobar si el software se comporta como esperamos en situaciones concretas.</p>

<div class="trio" style="margin-top:34px">
<div class="card"><h3>Elegir un caso</h3><p>Una cuenta y una distribución objetivo conocidas.</p></div>
<div class="card purple" v-click><h3>Ejecutar</h3><p>Solicitar una propuesta de rebalanceo.</p></div>
<div class="card success" v-click><h3>Comparar</h3><p>Contrastar el resultado con lo esperado.</p></div>
</div>
<p class="small" style="margin-top:28px" v-click>Una prueba puede hacerse manualmente o automatizarse.</p>

<!--
Entrada: vincular con el caso manual de Panther Broker sin repetir la introducción.
Clics: presentar caso, ejecución y comparación. Aclarar que automatizar es una forma de ejecutar pruebas.
Transición: no todas las pruebas observan el software a la misma escala.
-->

---

# Podemos probar a distintas escalas

<div class="trio">
<div class="card"><h3>Unitaria</h3><p>Un cálculo o comportamiento pequeño.</p></div>
<div class="card purple" v-click><h3>Integración</h3><p>La colaboración entre componentes.</p></div>
<div class="card" v-click><h3>Sistema</h3><p>Un flujo completo de la aplicación.</p></div>
</div>
<p class="lead" style="margin-top:38px" v-click>En este curso empezamos por las <strong>pruebas unitarias</strong>.</p>

<!--
Entrada: dar ejemplos orientativos, no presentar límites rígidos entre categorías.
Clics: distinguir colaboración y flujo completo; enfocar el curso en unidades.
Transición: necesitamos una herramienta para escribir y ejecutar esas pruebas en Java.
-->

---

# ¿Qué es JUnit?

<p class="lead">Un conjunto de herramientas para escribir y ejecutar pruebas en Java y en la JVM.</p>

<div class="split equal" style="margin-top:34px">
<div class="card"><h3>Escribir</h3><p>Marcamos métodos de prueba y expresamos lo esperado.</p></div>
<div class="card success" v-click><h3>Ejecutar</h3><p>Una herramienta descubre las pruebas y presenta sus resultados.</p></div>
</div>
<p class="small" style="margin-top:30px" v-click>Usaremos JUnit Jupiter, la API de pruebas de JUnit 6.</p>

<!--
Entrada: relacionar JUnit con el resultado verde y rojo de Kata Zero.
Clics: diferenciar escribir expectativas de ejecutar pruebas; nombrar Jupiter sin entrar aún en arquitectura.
Transición: la idea no es exclusiva de Java.
-->

---

# La idea existe en otros lenguajes

<TestingTools />
<p class="small" style="margin-top:24px">Cada ecosistema ofrece varias opciones; la idea de comprobar comportamientos es compartida.</p>

<!--
Entrada: las filas se revelan automáticamente una por una. Mencionar que hay alternativas para la mayoría de lenguajes y más de una por ecosistema.
No explicar sus APIs. En JavaScript la herramienta es Jest.
Transición: volver a JUnit y preparar un proyecto.
-->

---

# ¿Cómo incorporamos JUnit?

<div class="split equal">
<div class="card"><div class="dependency-card-heading"><ToolLogo file="jar.svg" alt="" class="jar-icon" /><h3>Archivos JAR</h3></div><p>Podemos agregar bibliotecas y configurar sus dependencias y el classpath manualmente.</p></div>
<div class="card success" v-click><div class="dependency-card-heading"><div class="build-logos"><ToolLogo file="maven.svg" alt="Apache Maven" /><ToolLogo file="gradle.svg" alt="Gradle" /></div><h3>Maven o Gradle</h3></div><p>Declaramos dependencias y versiones; la herramienta las resuelve y ejecuta las pruebas.</p></div>
</div>
<p class="lead" style="margin-top:34px" v-click>En el curso usaremos <strong>Maven</strong> y el Maven Wrapper del repositorio.</p>

<!--
Entrada: reconocer que se puede trabajar con JAR y classpath, sin sugerir que basta un único JAR para cualquier configuración.
Clics: explicar dependencias transitivas y reproducibilidad de versiones en términos sencillos. Elegir Maven; Gradle es otra opción.
Transición: explicar qué hace Maven antes de abrir su configuración.
-->

---

# ¿Qué es Maven?

<p class="lead">Una herramienta que ayuda a organizar, construir y probar proyectos Java.</p>

<div class="trio" style="margin-top:32px">
<div class="card"><h3>Dependencias</h3><p>Descarga las bibliotecas que el proyecto necesita.</p></div>
<div class="card purple" v-click><h3>Construcción</h3><p>Compila el código con la configuración del proyecto.</p></div>
<div class="card success" v-click><h3>Pruebas</h3><p>Ejecuta las pruebas y muestra sus resultados.</p></div>
</div>
<p class="small" style="margin-top:25px" v-click>El archivo <code>pom.xml</code> describe el proyecto y su configuración.</p>

<!--
Entrada: explicar que Maven organiza la construcción, no es solamente un descargador de bibliotecas.
Clics: dependencias, compilación y pruebas; presentar el POM como un archivo XML declarativo.
Transición: abrir una pequeña parte del POM real.
-->

---

# El proyecto se configura en pom.xml

<p class="source-path" data-file="pom.xml">primeros-pasos-junit/after/pom.xml</p>

<div class="split equal">
<div>

```xml {1-4|5-9|*}{lines:true}
<modelVersion>4.0.0</modelVersion>
<groupId>mx.azc.uam.pantherbroker</groupId>
<artifactId>primeros-pasos-junit-after</artifactId>
<version>1.0.0</version>
<properties>
    <maven.compiler.release>25</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <junit.version>6.1.3</junit.version>
</properties>
```


</div>
<div class="stack">
<div class="card"><h3>Identidad</h3><p>Grupo, nombre del artefacto y versión del proyecto.</p></div>
<div class="card purple" v-click><h3>Propiedades</h3><p>Versión de Java, codificación y versión de JUnit.</p></div>
</div>
</div>
<p class="caption">Fragmento real de <code>primeros-pasos-junit/after/pom.xml</code>; se omiten la raíz XML y las demás secciones.</p>

<!--
Entrada: explicar que pom.xml es un archivo de configuración declarativa, no un programa Java.
Focos: identidad y propiedades del proyecto. release 25 indica el nivel de compilación; el POM completo también valida la versión y el proveedor del JDK.
Transición: ubicar el POM, el código y las pruebas en el proyecto.
-->

---

# ¿Dónde va cada archivo?

<div class="project-layout">
  <div class="project-explorer">
    <div class="explorer-heading"><span>EXPLORADOR</span><strong>primeros-pasos-junit/after/</strong></div>
    <div class="explorer-tree" aria-label="Árbol de archivos del proyecto">
      <div class="explorer-row"><span class="tree-spacer"></span><span class="file-badge xml">XML</span><span>pom.xml</span><span class="tree-tag" v-click="1">Configuración</span></div>
      <details open>
        <summary class="explorer-row" @click.stop><span class="folder-mark" aria-hidden="true"></span><span>src</span></summary>
        <div class="tree-children">
          <details open>
            <summary class="explorer-row" @click.stop><span class="folder-mark" aria-hidden="true"></span><span>main</span></summary>
            <div class="tree-children">
              <details open>
                <summary class="explorer-row" @click.stop><span class="folder-mark source-folder" aria-hidden="true"></span><span>java</span></summary>
                <div class="tree-children">
                  <details open>
                    <summary class="explorer-row" @click.stop><span class="folder-mark" aria-hidden="true"></span><span>mx.azc.uam.pantherbroker</span></summary>
                    <div class="tree-children"><div class="explorer-row"><span class="tree-spacer"></span><span class="file-badge java">J</span><span>RebalanceCalculator.java</span><span class="tree-tag" v-click="2">Producción</span></div></div>
                  </details>
                </div>
              </details>
            </div>
          </details>
          <details open>
            <summary class="explorer-row" @click.stop><span class="folder-mark" aria-hidden="true"></span><span>test</span></summary>
            <div class="tree-children">
              <details open>
                <summary class="explorer-row" @click.stop><span class="folder-mark test-folder" aria-hidden="true"></span><span>java</span></summary>
                <div class="tree-children">
                  <details open>
                    <summary class="explorer-row" @click.stop><span class="folder-mark" aria-hidden="true"></span><span>mx.azc.uam.pantherbroker</span></summary>
                    <div class="tree-children"><div class="explorer-row"><span class="tree-spacer"></span><span class="file-badge java">J</span><span>RebalanceCalculatorTest.java</span><span class="tree-tag" v-click="3">Prueba</span></div></div>
                  </details>
                </div>
              </details>
            </div>
          </details>
        </div>
      </details>
    </div>
  </div>
  <div class="explorer-explanations">
    <div class="explorer-callout" v-click="1"><strong>pom.xml</strong><span>Configura el proyecto y sus dependencias.</span></div>
    <div class="explorer-callout" v-click="2"><strong>src/main/java</strong><span>Contiene el código de producción.</span></div>
    <div class="explorer-callout" v-click="3"><strong>src/test/java</strong><span>Contiene las pruebas automatizadas.</span></div>
  </div>
</div>
<p class="caption">El paquete se muestra agrupado, como en el explorador de un IDE.</p>

<!--
Entrada: mostrar el árbol completo; abrir o cerrar carpetas si ayuda a explicar la jerarquía. El paquete está agrupado como en un IDE.
Clics: identificar el POM, la clase de producción y la clase de prueba, cada uno con su explicación.
Transición: preparar el proyecto usando el POM.
-->

---

# Fijar la versión de JUnit

<p class="source-path" data-file="pom.xml">primeros-pasos-junit/after/pom.xml</p>

<p class="small">En <code>pom.xml</code>, el BOM mantiene alineados los módulos de JUnit:</p>

```xml {1-3|4-13|*}{lines:true}
<properties>
    <junit.version>6.1.3</junit.version>
</properties>
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.junit</groupId>
            <artifactId>junit-bom</artifactId>
            <version>${junit.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

<p class="caption">Fragmentos del POM: se omiten otras propiedades. El proyecto ya configura Java 25.</p>

<!--
Entrada: señalar la propiedad y explicar que el BOM alinea versiones de artefactos JUnit.
Es un fragmento: la sección properties completa incluye también la versión de Java y codificación.
Transición: declarar Jupiter usando la versión gestionada.
-->

---

# Configurar JUnit con Maven

<p class="source-path" data-file="pom.xml">primeros-pasos-junit/after/pom.xml</p>

<p class="small">En <code>pom.xml</code>, declaramos JUnit Jupiter para las pruebas:</p>

```xml {1-3|4|*}{lines:true}
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <scope>test</scope>
</dependency>
```

<div class="card purple" v-click><h3>¿Dónde está la versión?</h3><p>El proyecto la fija en <code>junit-bom</code>: <strong>6.1.3</strong>.</p></div>
<p class="caption">Fragmento del POM completo del proyecto after. El BOM alinea las versiones de los módulos de JUnit.</p>

<!--
Entrada: señalar grupo y artefacto; test limita la dependencia al contexto de pruebas.
Clic: explicar que el BOM del POM completo gestiona la versión. Mostrar el archivo real si hace falta.
Transición: Maven también necesita una versión compatible del plugin que ejecuta pruebas.
-->

---

# ¿Quién ejecuta las pruebas?

<p class="source-path" data-file="pom.xml">primeros-pasos-junit/after/pom.xml</p>

<div class="split equal">
<div>

```xml {lines:true}
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.6.1</version>
</plugin>
```

</div>
<div class="stack">
<div class="card"><h3>Maven Surefire</h3><p>Ejecuta las pruebas durante la fase <code>test</code>.</p></div>
<div class="card purple" v-click><h3>JUnit Jupiter</h3><p>Proporciona la API y el motor para las pruebas que escribimos.</p></div>
</div>
</div>
<p class="caption">Fragmento del POM real. JUnit 6 requiere Surefire 3.0.0 o posterior.</p>

<!--
Entrada: diferenciar la herramienta de construcción, el plugin y el framework.
Clic: decir que el POM completo también fija compilador, BOM y JDK.
Transición: abrir la primera prueba del proyecto.
-->

---

# ¿Qué hace quantityToTrade?

<p class="source-path" data-file="RebalanceCalculator.java">primeros-pasos-junit/after/src/main/java/…/RebalanceCalculator.java</p>

<div class="split code-compact">
<div>

```java {1-2|3-4|5|*}{lines:true}
static double quantityToTrade(int totalValue, int targetPercent,
                              int price, int currentQuantity) {
    int targetValue = totalValue * targetPercent / 100;
    double targetShares = targetValue / (double) price;
    return targetShares - currentQuantity;
}
```

<div class="file-context" aria-label="Ubicación de la clase y su prueba">
<div><strong>primeros-pasos-junit/after/</strong></div>
<div><span>src/main/java/</span>mx/azc/uam/pantherbroker/<br>└── <strong>RebalanceCalculator.java</strong></div>
<div><span>src/test/java/</span>mx/azc/uam/pantherbroker/<br>└── RebalanceCalculatorTest.java</div>
</div>

</div>
<div class="stack">
<div class="card"><h3>Recibe</h3><p>Valor de la cuenta, porcentaje objetivo, precio y cantidad actual.</p></div>
<div class="card purple" v-click><h3>Calcula</h3><p>Cuántas acciones corresponden al objetivo y la diferencia frente a las actuales.</p></div>
<div class="card success" v-click><h3>Devuelve</h3><p>Positivo: comprar. Negativo: vender. Cero: sin operación.</p></div>
</div>
</div>
<p class="caption">Método real de RebalanceCalculator.java; se omiten paquete y clase. Ejemplo didáctico con importes enteros.</p>

<!--
Entrada: mostrar el método que probaremos. Ya se extrajo y corrigió en Kata Zero.
Ubicar la clase en src/main/java y su prueba en src/test/java; comparten el mismo paquete.
Focos: parámetros, valor y cantidad objetivo, y diferencia; señalar el signo de la operación.
La división del valor objetivo sigue usando int; el código simplifica el dominio financiero.
Transición: abrir la clase que comprueba este comportamiento.
-->

---

# Nuestra primera clase de prueba

<p class="source-path" data-file="RebalanceCalculatorTest.java">primeros-pasos-junit/after/src/test/java/…/RebalanceCalculatorTest.java</p>

```java {1-4|6-7|8|*}{lines:true}
package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class RebalanceCalculatorTest {
    @Test
    void buysTwoSharesWhenBelowTarget() {
        // ... preparación, cálculo y comprobación
    }
}
```

<p class="caption">Esqueleto; el cuerpo completo aparece a continuación.</p>

<!--
Entrada: el paquete sitúa la prueba junto a la clase en la estructura de test.
Focos: imports, clase y anotación. JUnit reconoce el método mediante Test; el nombre describe el comportamiento.
Transición: abrir el cuerpo real y recorrerlo por partes.
-->

---

# Una prueba en tres pasos: AAA

<div class="trio">
<div class="card"><h3>Arrange</h3><p>Preparamos los datos y condiciones.</p></div>
<div class="card purple" v-click><h3>Act</h3><p>Ejecutamos el comportamiento.</p></div>
<div class="card success" v-click><h3>Assert</h3><p>Comparamos el resultado con lo esperado.</p></div>
</div>
<p class="small" style="margin-top:34px" v-click>Es una manera de organizar una prueba, no una regla de sintaxis de JUnit.</p>

<!--
Entrada: traducir cada paso y conectar con el cálculo de Panther Broker.
Clics: preparar, ejecutar y comprobar; recalcar que los comentarios son opcionales.
Transición: reconocer las tres partes en una prueba real.
-->

---

# AAA en Panther Broker

<p class="source-path" data-file="RebalanceCalculatorTest.java">primeros-pasos-junit/after/src/test/java/…/RebalanceCalculatorTest.java</p>

<div class="code-compact">

```java {3-7|9-11|13-14|*}{lines:true}
@Test
void buysTwoSharesWhenBelowTarget() {
    // Arrange: cuenta de 2000 USD, objetivo 60%, precio 100 USD y 10 acciones.
    int totalValue = 2000;
    int targetPercent = 60;
    int price = 100;
    int currentQuantity = 10;

    // Act: calcular la operación propuesta.
    double order = RebalanceCalculator.quantityToTrade(
            totalValue, targetPercent, price, currentQuantity);

    // Assert: se deben comprar dos acciones.
    assertEquals(2.0, order, 0.000001);
}
```

</div>
<p class="caption">Esperado: 2.0 · resultado: order · tolerancia: 0.000001. Se omiten imports y clase.</p>

<!--
Entrada: recorrer el método real por bloques resaltados.
Focos: datos de la cuenta, llamada única y comparación. Una orden positiva representa compra.
Explicar brevemente que la tolerancia permite comparar aproximaciones double; no es una política monetaria.
Transición: ejecutar la prueba con el wrapper.
-->

---

# Ejecutar la prueba

<p class="small">Desde la raíz del repositorio, ejecutamos la prueba con Maven:</p>

<TerminalRecording name="primera-prueba" alt="Ejecución real de Maven: la prueba buysTwoSharesWhenBelowTarget pasa" compact />

<p class="caption">JDK SDKMAN 25.0.5.0+8-zulu · El panel presenta el resultado real de Surefire.</p>

<!--
Entrada: reproducir la ejecución real. Al terminar, el panel revela el resultado leído del reporte de Surefire.
Mencionar que una falla indica una diferencia que debemos investigar.
Transición: cerrar invitando a cambiar un dato y ejecutar de nuevo.
-->

---

# Tu turno: cambia un caso

<p class="lead">En una copia de <code>after</code>, cambia el porcentaje objetivo y calcula primero qué operación esperas.</p>

<div class="card purple" style="margin-top:32px"><h3>Práctica opcional</h3><p>Escribe otra prueba con AAA y ejecútala con Maven. Después, cambia temporalmente la expectativa para observar una falla.</p></div>

<!--
Entrada: invitar a practicar voluntariamente sin asumir entrega ni calificación.
Salida: anunciar que en la siguiente lección se profundizará en las comprobaciones.
-->
