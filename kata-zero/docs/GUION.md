# Guion introductorio en siete momentos

Duración: 7–8 minutos. Español de México. Objetivo: querer aprender pruebas unitarias después de ver un problema conocido. No enseñar todavía arquitectura JUnit, AAA, refactorización, mocking ni precisión financiera completa.

## 1. El programa original · 0:00–1:00

Después de la portada, explicar brevemente el propósito de Panther Broker y luego presentar el fragmento original de Panther Broker: datos, valor total y cálculo de las órdenes. Explicar que proponía un plan por consola para acciones completas, sin ejecutar compras o ventas. Después presentar la cuenta: diez META y diez AAPL, ambas a 100 USD; objetivos ingresados 40/60. Explicar brevemente rebalancear por valor. Calcular a mano vender 2 META y comprar 2 AAPL. Abrir before, mostrar el menú y ejecutar el caso.

«Hice un programa para acciones completas. Lo ejecuté, comparé los números y parece funcionar».

## 2. El requisito nuevo · 1:00–1:30

«Ahora debe permitir comprar y vender fracciones de una acción». Dar un ejemplo de cantidad decimal sin profundizar en intermediarios reales.

## 3. El cambio rápido y la misma comprobación · 1:30–2:30

Cambiar el tipo de retorno de quantityToTrade y de targetShares de int a double. Ejecutar after/01-naive-fractions con los mismos datos. Mostrar la captura manual-original: vender 2.0 y comprar 2.0.

«Sigue dando lo mismo. Entonces lo doy por terminado». Pausar para que resulte reconocible esa forma de trabajar, sin ridiculizarla. Todavía no señalar la división.

## 4. Otros valores revelan el error · 2:30–3:45

Entregar otro precio: solo META pasa de 100 a 150 USD. La cuenta vale 2500 USD; META debería representar 1000 USD. Necesita conservar 1000/150 = 6.666666… acciones y vender aproximadamente 3.333333.

Mostrar manual-fractional: propone vender 4.0. Para reproducir, editar el primer literal del arreglo de precios en una copia y recompilar; el menú no edita precios.

«Cambiar el tipo del resultado no fue suficiente». No exigir que el espectador descubra el defecto por su cuenta.

## 5. Introducir pruebas unitarias · 3:45–4:45

«Podemos dejar estas expectativas escritas en código y pedir que se comprueben cada vez que cambiamos el programa».

Mostrar dos pruebas del ejemplo original en verde. Aclarar: ese resultado no habría descubierto la fracción omitida; hacen falta casos que ejerzan el nuevo requisito. Tener una suite con ese caso al hacer el cambio habría permitido detectarlo antes.

## 6. Demostración: verde, rojo y verde · 4:45–6:45

Mostrar una sola prueba fraccionaria, con @Test, llamada y assertEquals. No explicar todavía todas las anotaciones ni parámetros. La tolerancia es un margen pequeño para comparar esta aproximación double.

Mostrar tests-fractional-red: tres pruebas, una falla; esperado -3.333333, obtenido -4.0. Las dos anteriores siguen pasando.

Señalar `targetValue / price`: ambos son int, por lo que 1000/150 produce 6 antes de guardarse como 6.0. Precisar que es truncamiento, no un error binario de double. Promover el denominador a double y mostrar tests-fixed-green: las tres pasan sin cambiar expectativas.

El cálculo ya está en quantityToTrade desde la versión original; la prueba lo llama directamente. No llamar TDD a este recorrido.

## 7. Qué aprenderemos · 6:45–7:30

Anunciar componentes de una prueba y assertions; AAA y ciclo de vida; excepciones y casos límite; parametrización; Mockito y aislamiento; TDD y refactorización; tiempo, precisión y cobertura. No enseñar esas técnicas ahora.

«Durante el curso aprenderemos a elegir casos, escribir pruebas y entender sus resultados para cambiar código con más confianza».

Cerrar con formato: videos y práctica opcional sin calificación. No agregar una tarea ni un tutorial de instalación a esta introducción.

## Preparación y capturas

Ejecutar `sdk env` y `python3 scripts/verify-kata-zero.py`. Las seis capturas y sus extractos están en presentation/intro-junit-kata-zero/public/terminal. Son imágenes renderizadas a partir de salidas reales, no fotos de una ventana ni resultados inventados.

Las etiquetas v4 conservan el estado rojo y su corrección. El deck es apoyo a la historia, no un sustituto del programa y sus resultados.

## Reproducción de terminal en las diapositivas

En la presentación interactiva, dejar que el terminal aparezca y se reproduzca automáticamente a mitad de velocidad; en el caso rojo aparece después de recorrer el código. Al terminar, el panel inferior revela los resultados reales de las pruebas en orden didáctico. Hacer clic en el terminal permite pausar o continuar. Se pueden pausar mientras se explica la cuenta o el fallo; al cambiar de diapositiva se detiene la reproducción. Para volver a grabar las cinco sesiones: `python3 scripts/record-kata-zero.py` desde la raíz. Las entradas son automatizadas, las salidas son reales y el JDK es Zulu 25.0.5.0+8-zulu. El PDF conserva capturas estáticas. Los comandos de consola parten de proyectos Maven compilados previamente.
