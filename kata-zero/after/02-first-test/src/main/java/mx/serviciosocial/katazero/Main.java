package mx.serviciosocial.katazero;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] symbols = {"META", "AAPL"};
        BigDecimal[] prices = {new BigDecimal("100.00"), new BigDecimal("100.00")};
        BigDecimal[] quantities = {new BigDecimal("10"), new BigDecimal("10")};
        BigDecimal[] weights = {new BigDecimal("0.40"), new BigDecimal("0.60")};
        System.out.println("Cuenta de Alex · precios ficticios en USD · objetivo 40/60");
        while (true) {
            System.out.println("\n1. Ver cuenta");
            System.out.println("2. Calcular rebalanceo");
            System.out.println("0. Salir");
            String option = reader.readLine();
            if (option == null || option.equals("0")) break;
            if (option.equals("1")) {
                BigDecimal total = BigDecimal.ZERO;
                for (int i = 0; i < symbols.length; i++) {
                    total = total.add(prices[i].multiply(quantities[i]));
                    System.out.println(symbols[i] + ": " + quantities[i] + " acciones a " + prices[i] + " USD");
                }
                System.out.println("Valor total: " + total + " USD");
            } else if (option.equals("2")) {
                BigDecimal total = BigDecimal.ZERO;
                for (int i = 0; i < symbols.length; i++) {
                    total = total.add(prices[i].multiply(quantities[i]));
                }
                System.out.println("Plan sugerido (no modifica la cuenta):");
                for (int i = 0; i < symbols.length; i++) {
                    BigDecimal difference = RebalanceCalculator.quantityToTrade(
                            total, weights[i], prices[i], quantities[i]);
                    if (difference.signum() != 0) {
                        System.out.println((difference.signum() < 0 ? "VENDER " : "COMPRAR ")
                                + symbols[i] + " " + difference.abs().toPlainString() + " acciones");
                    } else {
                        System.out.println("Sin cambios para " + symbols[i]);
                    }
                }
            } else {
                System.out.println("Opción no válida.");
            }
        }
        System.out.println("Hasta luego.");
    }
}
