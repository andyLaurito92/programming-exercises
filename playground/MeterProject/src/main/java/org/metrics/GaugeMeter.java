package org.metrics;

public class GaugeMeter implements Meter {

    private double current;

    public GaugeMeter() {
        current = 0L;
    }

    public void setValue(Double val) {
        current = val;
    }

    @Override
    public String getData() {
        return String.valueOf(current);
    }
}
