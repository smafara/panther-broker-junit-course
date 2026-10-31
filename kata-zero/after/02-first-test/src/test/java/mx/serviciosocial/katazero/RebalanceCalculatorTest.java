package mx.serviciosocial.katazero;

import java.math.BigDecimal;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RebalanceCalculatorTest {
    @Test
    @DisplayName("Propone vender 5.2 META y comprar 13 AAPL para llegar a 40/60")
    void calculatesSellAndBuyForFortySixtyAllocation() {
        // Preparar: 10 META a 500 USD y 5 AAPL a 200 USD valen 6000 USD.
        BigDecimal totalValue = new BigDecimal("6000.00");

        // Ejecutar: negativo significa vender; positivo, comprar.
        BigDecimal metaOrder = RebalanceCalculator.quantityToTrade(totalValue,
                new BigDecimal("0.40"), new BigDecimal("500.00"), new BigDecimal("10"));
        BigDecimal appleOrder = RebalanceCalculator.quantityToTrade(totalValue,
                new BigDecimal("0.60"), new BigDecimal("200.00"), new BigDecimal("5"));

        // Comprobar: valores calculados a mano, incluida la escala de cuatro decimales.
        assertEquals(new BigDecimal("-5.2000"), metaOrder, "META debe venderse");
        assertEquals(new BigDecimal("13.0000"), appleOrder, "AAPL debe comprarse");
    }
}
