package org.api;

import org.metrics.CounterMeter;
import org.metrics.GaugeMeter;
import org.register.MeterRegister;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/metrics/gauge")
public class CounterController {
    private final MeterRegister meterRegister;

    public CounterController(MeterRegister meterRegister) {
        this.meterRegister = meterRegister;
    }

    @PutMapping("/{name}")
    public String setCounter(@PathVariable String name) {
        CounterMeter counter = meterRegister.getCounter(name);  // returns a GaugeMeter
        counter.increment();
        return "OK";
    }

    @PutMapping("/{name}/{value}")
    public String setCounter(@PathVariable String name, @PathVariable Long value) {
        CounterMeter counter = meterRegister.getCounter(name);  // returns a GaugeMeter
        counter.increment(value);
        return "OK";
    }
}
