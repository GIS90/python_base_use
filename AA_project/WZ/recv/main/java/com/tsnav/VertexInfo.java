package com.tsnav;

import java.math.BigDecimal;
import java.util.Arrays;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;
import sun.security.provider.certpath.Vertex;

import java.lang.Math;

/**
 * User: mac
 * Date: 7/30/15
 * Time: 10:14 AM
 * To change this template use File | Settings | File Templates.
 */


public class VertexInfo {

    private BigDecimal OFFSET_1 = BigDecimal.valueOf(Math.pow(10.0, 6));

    private BigDecimal OFFSET_2 = BigDecimal.valueOf(Math.pow(10.0, 5));

    private static final Logger logger = LogManager.getLogger(VertexInfo.class);

    private Vertex lastVertex = null;

    public static boolean isVertexEqual(VertexInfo left, VertexInfo right) {
        return left.lonDiff == right.lonDiff && left.latDiff == right.latDiff && left.timeDiff == right.timeDiff;
    }

    public String formatByGPSInfo(GPSInfo g){
        String ID = String.valueOf(g.ID);
        String naviState = String.valueOf(g.navStat);
        BigDecimal lonDiff = BigDecimal.valueOf(this.lonDiff).divide(this.OFFSET_2, 7, BigDecimal.ROUND_HALF_UP);
        BigDecimal latDiff = BigDecimal.valueOf(this.latDiff).divide(this.OFFSET_2, 7, BigDecimal.ROUND_HALF_UP);
        BigDecimal lon = BigDecimal.valueOf(g.lon).divide(this.OFFSET_1, 8, BigDecimal.ROUND_HALF_UP).add(lonDiff).setScale(6, BigDecimal.ROUND_HALF_UP);
        BigDecimal lat = BigDecimal.valueOf(g.lat).divide(this.OFFSET_1, 8, BigDecimal.ROUND_HALF_UP).add(latDiff).setScale(6, BigDecimal.ROUND_HALF_UP);
        String time = TimeUtil.toUTCString(g.time + this.timeDiff);
        String speed = String.valueOf(this.speed);
        String angle = String.valueOf(this.angle);
        return time +" " + ID + " " + naviState + " " + lon.toString() + " " + lat.toString() + " " + speed + " " + angle;
    }

    public static VertexInfo parseFromBuffer(VertexInfo lastV, byte[] b) {
        if (b.length != 8) {
            logger.error("VertexInfo parseFromBuffer the buffer length is not 8");
            return null;
        }
        VertexInfo retval = new VertexInfo();
        int lonDiff = EndianTransform.littleToInt(Arrays.copyOfRange(b, 0, 2));
        int latDiff = EndianTransform.littleToInt(Arrays.copyOfRange(b, 2, 4));
        int timeDiff = b[4];
        int speed = b[5];
        int angle = EndianTransform.littleToInt(Arrays.copyOfRange(b, 6, 8));
        int lastLonDiff = (null == lastV) ? 0: lastV.lonDiff;
        int lastLatDiff = (null == lastV) ? 0: lastV.latDiff;
        int lastTimeDiff = (null == lastV) ? 0: lastV.timeDiff;
        retval.lonDiff = lonDiff + lastLonDiff;
        retval.latDiff = latDiff + lastLatDiff;
        retval.timeDiff = timeDiff + lastTimeDiff;
        retval.speed = speed;
        retval.angle = angle;
        return retval;
    }

    public int getLonDiff() {
        return this.lonDiff;
    }

    public int getLatDiff() {
        return this.latDiff;
    }

    public int getTimeDiff() {
        return this.timeDiff;
    }

    public int getSpeed() {
        return this.speed;
    }

    public int getAngle() {
        return this.angle;
    }

    private int lonDiff;
    private int latDiff;
    private int timeDiff;
    private int speed;
    private int angle;
}
