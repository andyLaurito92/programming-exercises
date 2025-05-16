package org.register;

import org.flusher.FileFlushStrategy;
import org.flusher.FlushStrategy;
import org.metrics.Meter;

import java.util.*;

/**
 * My meter register
 *
 */
public class MeterRegister {
    private final FlushStrategy flushStrategy;
    public final ArrayList<Meter> registry;
    public static String ERROR_MESSAGE = "%s cannot be neither null nor empty";

    public MeterRegister() {
        this(new FileFlushStrategy());
    }

    public MeterRegister(FlushStrategy flushStrategy) {
        this.registry = new ArrayList<>();
        this.flushStrategy = flushStrategy;
    }


    public void addMeter(Meter meter) {
        if (meter == null) {
            throw new IllegalArgumentException(String.format(ERROR_MESSAGE, meter));
        }
        registry.add(meter);
    }

    /*
     * Get all meters registered in this registry
     */
    public List<Meter> getMeters() {
        return Collections.unmodifiableList(this.registry);
    }

    public void flush() {
        for (Meter meter : registry) {
            flushStrategy.flush(meter.getData());
        }
    }
}
