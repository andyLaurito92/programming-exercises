package org.api;

import org.metrics.GaugeMeter;
import org.register.MeterRegister;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/metrics/gauge")
public class GaugeController {

    private final MeterRegister meterRegister;

    public GaugeController(MeterRegister meterRegister) {
        this.meterRegister = meterRegister;
    }

    @PutMapping("/{name}/{value}")
    public String setGauge(@PathVariable String name, @PathVariable double value) {
        GaugeMeter gauge = meterRegister.getGauge(name);  // returns a GaugeMeter
        gauge.setValue(value);
        return "OK";
    }
}