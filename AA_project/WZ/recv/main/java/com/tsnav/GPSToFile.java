package com.tsnav;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import com.sun.javafx.tools.packager.Log;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

/**
 * User: mac
 * Date: 7/30/15
 * Time: 11:41 AM
 * To change this template use File | Settings | File Templates.
 */

public class GPSToFile implements Runnable {

    private static GPSToFile instance = null;
    private boolean runFlag = false;
    private final Queue<GPSInfo> queue = new LinkedList<GPSInfo>();
    private static final Logger logger = LogManager.getLogger(GPSToFile.class);
    private final Lock queueLock = new ReentrantLock();

    //use DCL to make thread safe
    public static GPSToFile getInstance() {
        if (null == GPSToFile.instance) {
            synchronized (GPSToFile.class) {
                GPSToFile.instance = new GPSToFile();
            }
        }
        return GPSToFile.instance;
    }

    private static boolean writeDataToFile(String content, String fileName) {
        logger.debug("writeDataToFile called");
        RandomAccessFile randomFile = null;
        try {
            randomFile = new RandomAccessFile(fileName, "rw");
            long fileLength = randomFile.length();
            randomFile.seek(fileLength);
            randomFile.writeBytes(content);
            return true;
        } catch (IOException e) {
            logger.error("writeDataToFile got exception, the error is " + e.toString());
            return false;
        } finally {
            if (randomFile != null) {
                try {
                    randomFile.close();
                } catch (IOException e) {
                    logger.error("writeDataToFile close got exception, the error is " + e.toString());
                }
            }
        }
    }

    @Override
    public void run() {
        this.runFlag = true;
        StringBuilder sb = new StringBuilder();
        long gpsCount = 0;
        long gpsTotalCount = 0;
        while (this.runFlag) {
            this.queueLock.lock();
            if (this.queue.isEmpty()) {
                this.queueLock.unlock();
                TimeUtil.Sleep(1);
            } else {
                GPSInfo info = this.queue.poll();
                this.queueLock.unlock();
                if (null == info) {
                    continue;
                }
                gpsTotalCount += info.getVertexNum();
                gpsCount += 1;
                if (0 == gpsCount % 1024) {
                    String msg = "GPSToFile gps info is " + gpsCount + " total count is " + gpsTotalCount + "\n";
                    logger.debug(msg);
                }
                String value = info.prettyPrintAll();
                sb.append(value);
                //we flush the data every 64KB
                if (sb.length() > 64 * 1024) {
                    logger.debug("we will flush the data to file");
                    String fileName = TimeUtil.getCurrentTime() + ".data";
                    if (!GPSToFile.writeDataToFile(sb.toString(), fileName)) {
                        logger.error("Write data to file failed");
                    }
                    sb.delete(0, sb.length());
                }
                logger.debug(info.prettyPrintAll());
            }
        }
    }

    public void writeToCache(GPSInfo info) {
        synchronized (this.queue) {
            this.queue.add(info);
        }
    }

    public void stop() {
        logger.debug("stop called");
        this.runFlag = false;
    }
}
