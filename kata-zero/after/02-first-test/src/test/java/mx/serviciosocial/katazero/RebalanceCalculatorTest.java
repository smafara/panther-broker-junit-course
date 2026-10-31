package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RebalanceCalculatorTest {
    @Test
    @DisplayName("Con META a 150 USD, propone vender 3.3333 acciones")
    void preservesFractionalSharesWhenPriceChanges() {
        // Preparar: 10 META a 150 USD + 10 AAPL a 100 USD = 2500 USD.
        BigDecimal totalValue = new BigDecimal("2500.00");

        // Ejecutar: META debe representar 40% de la cuenta.
        BigDecimal order = RebalanceCalculator.quantityToTrade(totalValue,
                new BigDecimal("0.40"), new BigDecimal("150.00"), new BigDecimal("10"));

        // Comprobar: 1000 / 150 - 10 = -3.333333...; cuatro decimales.
        assertEquals(new BigDecimal("-3.3333"), order);
    }
}
