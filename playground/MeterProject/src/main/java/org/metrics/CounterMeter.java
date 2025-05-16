package org.metrics;

public class CounterMeter implements Meter {
    private Long counter;

    public CounterMeter() {
        this.counter = 0L;
    }

    public void increment(){
        this.counter ++;
    }

    public void increment(Long increment) {
        this.counter += increment;
    }

    public String getData() {
        return counter.toString();
    }
}
