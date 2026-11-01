package mx.azc.uam.pantherbroker;

final class RebalanceCalculator {
    static double quantityToTrade(int totalValue, int targetPercent,
                                  int price, int currentQuantity) {
        int targetValue = totalValue * targetPercent / 100;
        double targetShares = targetValue / price;
        return targetShares - currentQuantity;
    }
}
