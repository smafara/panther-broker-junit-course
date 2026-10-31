# Revisión colegiada de la simplificación

Fecha: 31 de octubre de 2026. Solicitada explícitamente por el usuario. Participaron el implementador y dos revisores independientes: enseñanza y revisión técnica del defecto. Los revisores consultaron el código y las decisiones y no editaron archivos.

## Diagnóstico

El main de 140 líneas dedicaba demasiado espacio a editar datos y validarlos. Para llegar a la primera prueba había que entender cinco opciones, tres símbolos, captura de proporciones y varias rutas de error.

## Acuerdos

- Reducir a unos 50 renglones, dos instrumentos fijos y tres opciones: ver, proponer rebalanceo y salir.
- Mantener el estilo de consola solicitado y extraer solamente una fórmula.
- Introducir un defecto plausible de precisión: tratar una cantidad de acciones como dinero con dos decimales y luego completar a cuatro para mostrarla.
- Conservar el defecto durante la extracción y corregirlo después de observar una prueba fallida.
- La versión entregada de after/02 pasa; before y after/01 conservan el defecto como material docente identificado en documentación.

## Escenarios considerados

El revisor de enseñanza propuso una compra de 0.3333 acciones que el bug reduce a 0.3300. El revisor técnico propuso mantener la cuenta conocida y cambiar solo el precio de META de 500 a 350 USD: venta esperada 4.8571 y venta defectuosa 4.8600.

Se eligió el segundo: conserva símbolos, cantidades y porcentajes y cambia un solo precio. Ambos revisores coincidieron independientemente en la causa del defecto y en que el ejemplo inicial lo oculta.

## Precauciones incorporadas

El nuevo precio se representa como un escenario de prueba, no como una opción que ya no existe en el menú. El instructor puede reproducirlo cambiando el literal 500.00 por 350.00 en una copia del programa. No usar un cambio de escala como único motivo de falla: los resultados comparados son numéricamente diferentes.

La refactorización no arregla el defecto por sí sola. La prueba lo documenta y permite comprobar la corrección posterior. El guion diferencia estos momentos y no presenta el ejercicio como TDD.

## Revisión posterior: acciones completas y fraccionadas

El usuario pidió un defecto menos sutil. Ambos revisores aprobaron sustituir la pérdida de diezmilésimas por una conversión a entero heredada: un programa antes pensado para acciones completas conserva int al adaptarse a fracciones.

Escenario vigente: 10 META y 10 AAPL a 100 USD producen una venta de 2 y una compra de 2. Cambiar solo META a 150 USD exige vender 3.3333, pero el int propone vender 4. AAPL requiere comprar 5.

Se proporciona el resultado a mano y se comprueba únicamente META en la primera prueba. La corrección conserva decimales y redondea una sola vez la orden final. La revisión del defecto de dos decimales queda como antecedente; las decisiones vigentes son D017 y D018.
