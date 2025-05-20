package org.metricsapi.controller;

import org.api.MetricResponse;
import org.register.MeterRegister;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/metrics")
public class MetricsController {
    private final MeterRegister meterRegister;

    public MetricsController(MeterRegister meterRegister) {
        this.meterRegister = meterRegister;
    }

    @PostMapping("/{type}")
    public ResponseEntity<MetricResponse> addMetric(@PathVariable String type) {
        System.out.println("Creating new gauge metric");
        String meterName = meterRegister.addMeter(type);
        return ResponseEntity.ok(new MetricResponse(meterName, type));
    }
}
