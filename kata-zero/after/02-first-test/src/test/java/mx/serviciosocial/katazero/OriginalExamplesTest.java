package mx.serviciosocial.katazero;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class OriginalExamplesTest {
    @Test
    @DisplayName("El ejemplo original propone vender 2 META")
    void sellsWholeSharesInOriginalExample() {
        assertEquals(-2.0, RebalanceCalculator.quantityToTrade(2000, 40, 100, 10), 0.000001);
    }

    @Test
    @DisplayName("El ejemplo original propone comprar 2 AAPL")
    void buysWholeSharesInOriginalExample() {
        assertEquals(2.0, RebalanceCalculator.quantityToTrade(2000, 60, 100, 10), 0.000001);
    }
}
