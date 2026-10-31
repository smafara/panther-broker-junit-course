package mx.serviciosocial.katazero;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] symbols = {"META", "AAPL"};
        int[] prices = {100, 100};
        int[] quantities = {10, 10};
        int[] percentages = {40, 60};
        System.out.println("Cuenta de Alex · precios ficticios en USD · objetivo 40/60");
        while (true) {
            System.out.println("\n1. Ver cuenta\n2. Calcular rebalanceo\n0. Salir");
            String option = reader.readLine();
            if (option == null || option.equals("0")) break;
            if (option.equals("1")) {
                for (int i = 0; i < symbols.length; i++) {
                    System.out.println(symbols[i] + ": " + quantities[i] + " acciones a " + prices[i] + " USD");
                }
            } else if (option.equals("2")) {
                int total = 0;
                for (int i = 0; i < symbols.length; i++) total += prices[i] * quantities[i];
                System.out.println("Valor total: " + total + " USD");
                System.out.println("Plan sugerido (no modifica la cuenta):");
                for (int i = 0; i < symbols.length; i++) {
                    int targetValue = total * percentages[i] / 100;
                    int targetShares = targetValue / prices[i];
                    int difference = targetShares - quantities[i];
                    if (difference != 0) {
                        System.out.println((difference < 0 ? "VENDER " : "COMPRAR ")
                                + symbols[i] + " " + Math.abs(difference) + " acciones");
                    }
                }
            } else {
                System.out.println("Opción no válida.");
            }
        }
        System.out.println("Hasta luego.");
    }
}
