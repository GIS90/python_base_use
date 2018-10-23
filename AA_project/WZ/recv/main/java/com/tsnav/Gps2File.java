package com.tsnav;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

/**
 * User: mac
 * Date: 7/30/15
 * Time: 11:41 AM
 * To change this template use File | Settings | File Templates.
 */

public class Gps2File implements Runnable {

    private static Gps2File instance = null;
    private boolean runFlag = false;
    private final Queue<GPSInfo> queue = new LinkedList<GPSInfo>();
    private static final Logger logger = LogManager.getLogger(Gps2File.class);
    private final Lock queueLock = new ReentrantLock();

    //use DCL to make thread safe
    public static Gps2File getInstance() {
        if (null == Gps2File.instance) {
            synchronized (Gps2File.class) {
                Gps2File.instance = new Gps2File();
            }
        }
        return Gps2File.instance;
    }

    private static boolean writeDataToFile(String content, String fileName) {
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
            logger.debug("writeDataToFile success");
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
                    logger.debug("run the info is empty, current thread is " + Thread.currentThread().getId());
                    TimeUtil.Sleep(5 * 1000);
                    continue;
                }
                gpsTotalCount += info.getVertexNum();
                gpsCount += 1;
                if (0 == gpsCount % 4096) {
                    String msg = "GPSToFile gps info is " + gpsCount + " total count is " + gpsTotalCount;
                    logger.debug(msg);
                }
                sb.append(info.prettyPrintAll());
                //we flush the data every 4MB
                if (sb.length() > 4 * 1024 * 1024) {
                    logger.debug("we will flush the data to file");
                    String fileName = TimeUtil.getCurrentTime() + ".data";
                    if (!Gps2File.writeDataToFile(sb.toString(), fileName)) {
                        logger.error("Write data to file failed");
                    }
                    sb.delete(0, sb.length());
                }
                info = null;
            }
        }
    }

    public void writeToCache(GPSInfo info) {
        if (info == null) {
            return;
        }
        synchronized (this.queue) {
            this.queue.add(info);
        }
    }

    public void stop() {
        logger.debug("stop called");
        this.runFlag = false;
    }
}
