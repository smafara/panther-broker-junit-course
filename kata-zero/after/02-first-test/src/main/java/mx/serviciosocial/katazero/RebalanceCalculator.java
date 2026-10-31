package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import java.math.RoundingMode;

final class RebalanceCalculator {
    static BigDecimal quantityToTrade(BigDecimal totalValue, BigDecimal targetWeight,
                                      BigDecimal price, BigDecimal currentQuantity) {
        int target = totalValue.multiply(targetWeight)
                .divide(price, 4, RoundingMode.HALF_EVEN).intValue();
        return BigDecimal.valueOf(target).subtract(currentQuantity).setScale(4);
    }
}
