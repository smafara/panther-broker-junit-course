package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class RebalanceCalculatorTest {
    @Test
    void buysTwoSharesWhenBelowTarget() {
        // Arrange: cuenta de 2000 USD, objetivo 60%, precio 100 USD y 10 acciones.
        int totalValue = 2000;
        int targetPercent = 60;
        int price = 100;
        int currentQuantity = 10;

        // Act: calcular la operación propuesta.
        double order = RebalanceCalculator.quantityToTrade(
                totalValue, targetPercent, price, currentQuantity);

        // Assert: se deben comprar dos acciones.
        assertEquals(2.0, order, 0.000001);
    }
}
