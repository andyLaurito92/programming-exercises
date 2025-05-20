package org.register;

import org.flusher.FileFlushStrategy;
import org.flusher.FlushStrategy;
import org.metrics.CounterMeter;
import org.metrics.GaugeMeter;
import org.metrics.Meter;
import org.metrics.MeterFactory;
import org.springframework.stereotype.Component;

import java.util.*;

/**
 * My meter register
 *
 */
@Component
public class MeterRegister {
    private final FlushStrategy flushStrategy;
    public final HashMap<String, Meter> registry;
    public static String ERROR_MESSAGE = "%s cannot be neither null nor empty";

    public MeterRegister() {
        this(new FileFlushStrategy());
    }

    public MeterRegister(FlushStrategy flushStrategy) {
        this.registry = new HashMap<>();
        this.flushStrategy = flushStrategy;
    }


    public String addMeter(String type) {
        if (type == null) {
            throw new IllegalArgumentException(String.format(ERROR_MESSAGE, type));
        }
        UUID uuid = UUID.randomUUID();
        String meterName = uuid.toString();
        registry.put(meterName, MeterFactory.buildFrom(type));
        return meterName;
    }

    /*
     * Get all meters registered in this registry
     */
    public Collection<Meter> getMeters() {
        return Collections.unmodifiableCollection(this.registry.values());
    }

    public void flush() {
        for (Meter meter : registry.values()) {
            flushStrategy.flush(meter.getData());
        }
    }

    public Meter getMeter(String name) {
        Meter val = registry.get(name);
        if (val == null) {
            throw new IllegalArgumentException(String.format("Invalid metric name %s", name));
        }
        return val;
    }

    public GaugeMeter getGauge(String name) {
        return (GaugeMeter) getMeter(name);
    }

    public CounterMeter getCounter(String name) {
        return (CounterMeter) getMeter(name);
    }
}
