package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RebalanceCalculatorTest {
    @Test
    @DisplayName("Con META a 350 USD, propone vender 4.8571 acciones")
    void calculatesFractionalSaleWhenPriceChanges() {
        // Preparar: 10 META a 350 USD + 5 AAPL a 200 USD = 4500 USD.
        BigDecimal totalValue = new BigDecimal("4500.00");

        // Ejecutar: META debe representar 40% de la cuenta.
        BigDecimal order = RebalanceCalculator.quantityToTrade(totalValue,
                new BigDecimal("0.40"), new BigDecimal("350.00"), new BigDecimal("10"));

        // Comprobar: 1800 / 350 - 10 = -4.857142...; redondeado a cuatro decimales.
        assertEquals(new BigDecimal("-4.8571"), order);
    }
}
