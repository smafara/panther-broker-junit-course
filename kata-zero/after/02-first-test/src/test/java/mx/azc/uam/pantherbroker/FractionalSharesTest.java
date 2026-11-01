package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class FractionalSharesTest {
    // Conserva la fracción de acciones al vender.
    @Test
    @DisplayName("Dadas 10 acciones a 150 USD, cuando el objetivo es 40%, entonces vende 3.333333")
    void preservesFractionalSharesWhenSelling() {
        double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10);
        assertEquals(-3.333333, order, 0.000001);
    }
}
