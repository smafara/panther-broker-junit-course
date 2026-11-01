package mx.azc.uam.pantherbroker;

final class RebalanceCalculator {
    static int quantityToTrade(int totalValue, int targetPercent,
                                  int price, int currentQuantity) {
        int targetValue = totalValue * targetPercent / 100;
        int targetShares = targetValue / price;
        return targetShares - currentQuantity;
    }
}
