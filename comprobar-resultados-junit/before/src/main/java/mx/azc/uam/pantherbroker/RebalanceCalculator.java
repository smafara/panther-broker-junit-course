package mx.azc.uam.pantherbroker;

final class RebalanceCalculator {
    /** Calcula cuántas acciones comprar o vender. */
    static double quantityToTrade(int totalValue, int targetPercent,
                                  int price, int currentQuantity) {
        int targetValue = totalValue * targetPercent / 100;
        double targetShares = targetValue / (double) price;
        return targetShares - currentQuantity;
    }
}
