package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class OriginalExamplesTest {
    @Test
    @DisplayName("Dadas 10 acciones a 100 USD, cuando el objetivo es 40%, entonces vende 2")
    void givenTenSharesAt100_whenRebalancingTo40Percent_thenSellTwo() {
        assertEquals(-2.0, RebalanceCalculator.quantityToTrade(2000, 40, 100, 10), 0.000001);
    }

    @Test
    @DisplayName("Dadas 10 acciones a 100 USD, cuando el objetivo es 60%, entonces compra 2")
    void givenTenSharesAt100_whenRebalancingTo60Percent_thenBuyTwo() {
        assertEquals(2.0, RebalanceCalculator.quantityToTrade(2000, 60, 100, 10), 0.000001);
    }
}
