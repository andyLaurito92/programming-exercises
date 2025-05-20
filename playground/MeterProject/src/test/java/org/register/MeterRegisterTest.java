package org.register;

import junit.framework.TestCase;
import org.junit.jupiter.api.Test;
import org.metrics.GaugeMeter;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * Unit test for simple App.
 */
public class MeterRegisterTest extends TestCase {
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */

    private MeterRegister meterRegister;

    public MeterRegisterTest(String testName )
    {
        super( testName );
        testName.hashCode();
        this.meterRegister = new MeterRegister();
    }

    /**
     * Rigourous Test :-)
     */
    /*public void testAddingMetric() {
        this.meterRegister.addMeter("myGauge");
        assertEquals(this.meterRegister.getMeters());
    }*/

    public void testGivenMetricNullWhenAddMetricThenIllegalArgumentRaised() throws IllegalArgumentException {
        assertThrows(IllegalArgumentException.class, () -> {
            meterRegister.addMeter(null);
        });
    }
}
