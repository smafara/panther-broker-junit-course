package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class OriginalExamplesTest {
    // Vende dos acciones si está por encima del objetivo.
    @Test
    @DisplayName("Dadas 10 acciones a 100 USD, cuando el objetivo es 40%, entonces vende 2")
    void sellsTwoSharesWhenAboveTarget() {
        assertEquals(-2.0, RebalanceCalculator.quantityToTrade(2000, 40, 100, 10), 0.000001);
    }

    // Compra dos acciones si está por debajo del objetivo.
    @Test
    @DisplayName("Dadas 10 acciones a 100 USD, cuando el objetivo es 60%, entonces compra 2")
    void buysTwoSharesWhenBelowTarget() {
        assertEquals(2.0, RebalanceCalculator.quantityToTrade(2000, 60, 100, 10), 0.000001);
    }
}
