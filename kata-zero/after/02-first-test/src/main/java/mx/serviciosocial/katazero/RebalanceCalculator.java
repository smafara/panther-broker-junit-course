package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import java.math.RoundingMode;

final class RebalanceCalculator {
    static BigDecimal quantityToTrade(BigDecimal totalValue, BigDecimal targetWeight,
                                      BigDecimal price, BigDecimal currentQuantity) {
        BigDecimal target = totalValue.multiply(targetWeight)
                .divide(price, 2, RoundingMode.HALF_EVEN);
        return target.subtract(currentQuantity).setScale(4);
    }
}
