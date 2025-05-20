package org.api;

public class MetricResponse {
    private final String name;
    private final String type;

    public MetricResponse(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }
}
