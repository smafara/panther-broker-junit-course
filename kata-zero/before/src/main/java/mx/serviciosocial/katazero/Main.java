package mx.serviciosocial.katazero;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String cuenta = "Cuenta de Alex";
        String[] s = {"META", "AAPL", "NVDA"};
        BigDecimal[] p = {new BigDecimal("500.00"), new BigDecimal("200.00"), new BigDecimal("100.00")};
        BigDecimal[] q = {new BigDecimal("10"), new BigDecimal("5"), BigDecimal.ZERO};
        BigDecimal[] w = {new BigDecimal("0.40"), new BigDecimal("0.60"), BigDecimal.ZERO};
        int op = -1;
        System.out.println("FRACCIÓN - Rebalanceo de una cuenta (precios didácticos en USD)");
        while (op != 0) {
            System.out.println("\n" + cuenta);
            System.out.println("1. Ver cuenta");
            System.out.println("2. Cambiar precio");
            System.out.println("3. Cambiar distribución objetivo");
            System.out.println("4. Calcular rebalanceo");
            System.out.println("5. Cambiar acciones que tienes");
            System.out.println("0. Salir");
            System.out.println("Elige una opción:");
            String linea = br.readLine();
            if (linea == null) break;
            try {
                op = Integer.parseInt(linea.trim());
                if (op == 1) {
                    BigDecimal t = BigDecimal.ZERO;
                    for (int i = 0; i < s.length; i++) {
                        t = t.add(p[i].multiply(q[i]));
                        System.out.println(s[i] + " | acciones: " + q[i].toPlainString()
                                + " | precio USD: " + p[i].toPlainString()
                                + " | objetivo: " + w[i].multiply(new BigDecimal("100")).toPlainString() + "%");
                    }
                    System.out.println("Valor total USD: " + t.setScale(2, RoundingMode.HALF_EVEN).toPlainString());
                } else if (op == 2) {
                    System.out.println("Símbolo (META, AAPL o NVDA):");
                    String x = br.readLine();
                    if (x == null) break;
                    int j = -1;
                    for (int i = 0; i < s.length; i++) {
                        if (s[i].equals(x.trim().toUpperCase(Locale.ROOT))) j = i;
                    }
                    if (j == -1) {
                        System.out.println("Símbolo no admitido.");
                    } else {
                        System.out.println("Nuevo precio USD (usa punto decimal):");
                        String v = br.readLine();
                        if (v == null) break;
                        BigDecimal n = new BigDecimal(v.trim());
                        if (n.signum() <= 0) {
                            System.out.println("El precio debe ser positivo.");
                        } else {
                            p[j] = n;
                            System.out.println("Precio actualizado.");
                        }
                    }
                } else if (op == 3) {
                    BigDecimal[] nw = new BigDecimal[s.length];
                    BigDecimal suma = BigDecimal.ZERO;
                    boolean ok = true;
                    boolean fin = false;
                    for (int i = 0; i < s.length; i++) {
                        System.out.println("Proporción para " + s[i] + " (0.40 significa 40%):");
                        String v = br.readLine();
                        if (v == null) { fin = true; break; }
                        nw[i] = new BigDecimal(v.trim());
                        if (nw[i].signum() < 0 || nw[i].compareTo(BigDecimal.ONE) > 0) ok = false;
                        suma = suma.add(nw[i]);
                    }
                    if (fin) break;
                    if (ok && suma.compareTo(BigDecimal.ONE) == 0) {
                        w = nw;
                        System.out.println("Objetivo actualizado.");
                    } else {
                        System.out.println("Cada proporción debe estar entre 0 y 1 y la suma debe ser 1. No se cambió el objetivo.");
                    }
                } else if (op == 4) {
                    BigDecimal t = BigDecimal.ZERO;
                    for (int i = 0; i < s.length; i++) t = t.add(p[i].multiply(q[i]));
                    System.out.println("Valor total USD: " + t.setScale(2, RoundingMode.HALF_EVEN).toPlainString());
                    System.out.println("Plan sugerido (no modifica tus acciones):");
                    boolean algo = false;
                    for (int i = 0; i < s.length; i++) {
                        BigDecimal d = t.multiply(w[i]).subtract(q[i].multiply(p[i]))
                                .divide(p[i], 4, RoundingMode.HALF_EVEN);
                        if (d.signum() < 0 && d.abs().compareTo(q[i]) > 0) d = q[i].negate();
                        if (d.signum() < 0) {
                            System.out.println("VENDER " + s[i] + " " + d.abs().toPlainString() + " acciones");
                            algo = true;
                        }
                    }
                    for (int i = 0; i < s.length; i++) {
                        BigDecimal d = t.multiply(w[i]).subtract(q[i].multiply(p[i]))
                                .divide(p[i], 4, RoundingMode.HALF_EVEN);
                        if (d.signum() < 0 && d.abs().compareTo(q[i]) > 0) d = q[i].negate();
                        if (d.signum() > 0) {
                            System.out.println("COMPRAR " + s[i] + " " + d.toPlainString() + " acciones");
                            algo = true;
                        }
                    }
                    if (!algo) System.out.println("Sin operaciones: la cuenta ya está balanceada a esta precisión.");
                    System.out.println("No incluye efectivo, comisiones ni impuestos. El redondeo puede dejar diferencias pequeñas.");
                } else if (op == 5) {
                    System.out.println("Símbolo (META, AAPL o NVDA):");
                    String x = br.readLine();
                    if (x == null) break;
                    int j = -1;
                    for (int i = 0; i < s.length; i++) {
                        if (s[i].equals(x.trim().toUpperCase(Locale.ROOT))) j = i;
                    }
                    if (j == -1) {
                        System.out.println("Símbolo no admitido.");
                    } else {
                        System.out.println("Cantidad de acciones (cero o positiva):");
                        String v = br.readLine();
                        if (v == null) break;
                        BigDecimal n = new BigDecimal(v.trim());
                        if (n.signum() < 0) {
                            System.out.println("La cantidad no puede ser negativa.");
                        } else {
                            q[j] = n;
                            System.out.println("Posición actualizada.");
                        }
                    }
                } else if (op != 0) {
                    System.out.println("Opción no válida.");
                }
            } catch (NumberFormatException ex) {
                System.out.println("Escribe un número válido con punto decimal y sin separadores de miles.");
            }
        }
        System.out.println("Hasta luego.");
    }
}
