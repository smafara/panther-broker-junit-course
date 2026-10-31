# Primera prueba — estado rojo de la versión simplificada

Esta revisión conserva intencionalmente el cálculo defectuoso extraído en after/01. La primera prueba verifica META a 350 USD: espera -4.8571 acciones y obtiene -4.8600.

```sh
sdk env
./mvnw -f kata-zero/after/02-first-test/pom.xml test
```

Aquí el comando debe fallar. La etiqueta `kata-zero-v2-first-test-red` identifica esta demostración; el siguiente cambio corrige el cálculo sin cambiar la prueba. El estado final del material estará identificado como `kata-zero-v2-ready`.
