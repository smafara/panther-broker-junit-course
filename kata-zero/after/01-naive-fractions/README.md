# Después 1: cambiar int por double parece suficiente

Respecto a before solo cambian los tipos de targetShares y difference. Los operandos de la división permanecen int. El ejemplo manual sigue dando vender 2.0 y comprar 2.0, lo cual no prueba el requisito fraccionario.

```sh
./mvnw -q -f kata-zero/after/01-naive-fractions/pom.xml compile exec:java
```

Ejecutar desde la raíz con `sdk env`. Para el caso nuevo, cambiar solo el primer precio a 150 y recompilar una copia. El programa venderá 4.0 META, en lugar de aproximadamente 3.333333. No hay pruebas automatizadas en esta fotografía.
