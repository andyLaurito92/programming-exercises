package org.schedulable;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class FlusherScheduler implements Schedulable {
    private final Runnable task;
    private final long interval;
    private final ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();

    public FlusherScheduler(Runnable task, long interval) {
        this.task = task;
        this.interval = interval;
    }

    @Override
    public void schedule() {
        executor.scheduleAtFixedRate(task, interval, interval, TimeUnit.SECONDS);
    }
}

