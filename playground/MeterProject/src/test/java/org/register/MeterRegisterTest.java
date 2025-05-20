package org.register;


import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * Unit test for simple App.
 */
public class MeterRegisterTest {
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */

    private MeterRegister meterRegister;

    public MeterRegisterTest()
    {
        this.meterRegister = new MeterRegister();
    }

    /**
     * Rigourous Test :-)
     */
    /*
    @Test
    public void testAddingMetric() {
        this.meterRegister.addMeter("myGauge");
        assertEquals(this.meterRegister.getMeters());
    }*/

    @Test
    public void testGivenMetricNullWhenAddMetricThenIllegalArgumentRaised() throws IllegalArgumentException {
        assertThrows(IllegalArgumentException.class, () -> {
            meterRegister.addMeter(null);
        });
    }
}
