package org.metrics;

public class GaugeMeter implements Meter {

    private Long current;

    public GaugeMeter() {
        current = 0L;
    }

    public void setValue(Long val) {
        current = val;
    }

    @Override
    public String getData() {
        return current.toString();
    }
}
