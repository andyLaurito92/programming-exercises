package org.metrics;

public class MeterFactory {
    public static Meter buildFrom(String name) {
        switch (name.toLowerCase()) {
            case "counter":
                return new CounterMeter();
            case "gauge":
                return new GaugeMeter();
            default:
                throw new IllegalArgumentException(
                        String.format("Metric type '%s' is not valid. Must be 'counter' or 'gauge'.", name)
                );
        }
    }
}
