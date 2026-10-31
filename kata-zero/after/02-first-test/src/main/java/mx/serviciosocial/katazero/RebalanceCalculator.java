package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import java.math.RoundingMode;

final class RebalanceCalculator {
    static BigDecimal quantityToTrade(BigDecimal totalValue, BigDecimal targetWeight,
                                      BigDecimal price, BigDecimal currentQuantity) {
        return totalValue.multiply(targetWeight)
                .subtract(currentQuantity.multiply(price))
                .divide(price, 4, RoundingMode.HALF_EVEN);
    }
}
