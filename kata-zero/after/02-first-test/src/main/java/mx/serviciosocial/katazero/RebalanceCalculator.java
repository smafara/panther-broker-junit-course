package mx.serviciosocial.katazero;

final class RebalanceCalculator {
    static double quantityToTrade(int totalValue, int targetPercent,
                                  int price, int currentQuantity) {
        int targetValue = totalValue * targetPercent / 100;
        double targetShares = targetValue / (double) price;
        return targetShares - currentQuantity;
    }
}
