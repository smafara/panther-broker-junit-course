package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import java.math.RoundingMode;

final class RebalanceCalculator {
    // Recibe datos válidos; positivo significa comprar y negativo vender.
    static BigDecimal quantityToTrade(BigDecimal totalValue, BigDecimal targetWeight,
                                      BigDecimal price, BigDecimal currentQuantity) {
        BigDecimal difference = totalValue.multiply(targetWeight)
                .subtract(currentQuantity.multiply(price))
                .divide(price, 4, RoundingMode.HALF_EVEN);
        if (difference.signum() < 0 && difference.abs().compareTo(currentQuantity) > 0) {
            return currentQuantity.negate();
        }
        return difference;
    }
}
