package mx.azc.uam.pantherbroker;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

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
    @Test
    void proposesPurchaseWhenBelowTarget() {
        // Solo comprueba la dirección, no la cantidad requerida.
        double order = RebalanceCalculator.quantityToTrade(2000, 60, 100, 10);
        assertTrue(order > 0);
    }

    @Test
    void calculatesFractionalQuantityToSell() {
        // Calcula cuántas acciones fraccionarias se deben vender.
        double order = RebalanceCalculator.quantityToTrade(2500, 40, 150, 10);
        assertEquals(-3.333333, order, 0.000001);
    }

}
