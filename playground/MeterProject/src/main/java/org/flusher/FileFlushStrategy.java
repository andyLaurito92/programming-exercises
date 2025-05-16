package org.flusher;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileFlushStrategy implements FlushStrategy {
    @Override
    public void flush(String data) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("metrics.log", true))) {
            writer.write(data);
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace(); // Consider using a logger
        }
    }
}
