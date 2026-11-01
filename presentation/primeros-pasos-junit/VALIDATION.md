# Validación

Con SDKMAN Java 25.0.5.0+8-zulu, los dos proyectos Maven compilan; before no contiene pruebas y after ejecuta una prueba correcta. La presentación compila, exporta a PDF y el verificador revisa 15 diapositivas y notas sin errores de página ni desbordamientos.

El PDF y el navegador usan Chromium de Playwright. La exportación registra el aviso conocido de FloatingVue y termina correctamente. Las dependencias de JUnit, el BOM y Surefire se muestran como fragmentos del POM completo; la prueba AAA corresponde a la fuente Java de after.

Tras introducir Maven y el POM, la presentación tiene 17 diapositivas. Se verificaron la compilación, el PDF, las notas, la animación de herramientas y la ausencia de desbordamientos.

La presentación vigente contiene 18 diapositivas. Se verificaron el código del método, la grabación real de Maven, reproducción y pausa, el resultado verde de Surefire y el recurso estático de PDF.
