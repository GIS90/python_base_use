package com.tsnav;

import java.math.BigInteger;
import java.util.*;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

/**
 * User: mac
 * Date: 7/28/15
 * Time: 2:48 PM
 * To change this template use File | Settings | File Templates.
 */

public class Parser {

    private static final Logger logger = LogManager.getLogger(Parser.class);

    public GPSInfo parseBuffer(byte[] b) {
        if ( null == b) {
            return null;
        }
        int bLen = b.length;
        if (0x0D != b[bLen - 2] || 0x0A != b[bLen - 1]) {
            return null;
        }
        return this.parseFromBuffer(b);
    }

    private GPSInfo parseFromBuffer(byte[] b) {
        // the length is using 2 bytes character to stand, so the maximum length should be less than 64K
        if (b.length > 65536) {
            System.out.println("GPSInfo parseFromBuffer the length could not be larger than 65536");
            return null;
        }
        BigInteger ID = EndianTransform.bigToUint64(Arrays.copyOfRange(b, 0, 8));
        int navState = b[8];
        int vertexNum = b[9];
        // the vertex struct length is 8, the vertex number is the length of all vertexes + 1
        if ((b.length - 27) / 8 != vertexNum - 1) {
            logger.error("GPSInfo parseFromBuffer the data length is not correct " + b.length);
            return null;
        }
        if (vertexNum <= 0) {
            logger.error("GPSInfo parseFromBuffer the vertexNum should be bigger than 1");
            return null;
        }
        GPSInfo gpsValue = new GPSInfo();
        int lon = EndianTransform.littleToInt(Arrays.copyOfRange(b, 10, 14));
        int lat = EndianTransform.littleToInt(Arrays.copyOfRange(b, 14, 18));
        int time = EndianTransform.littleToInt(Arrays.copyOfRange(b, 18, 22));
        int speed = b[22];
        int angle = EndianTransform.littleToInt(Arrays.copyOfRange(b, 23, 25));
        gpsValue.ID = ID;
        gpsValue.navStat = navState;
        gpsValue.vertexNum = vertexNum - 1;
        gpsValue.vertex = new ArrayList<VertexInfo>(vertexNum);
        gpsValue.lon = lon;
        gpsValue.lat = lat;
        gpsValue.time = time;
        gpsValue.speed = speed;
        gpsValue.angle = angle;
        int startIndex = 25;
        VertexInfo lastV = null;
        for (int i = 0; i < vertexNum - 1; i++) {
            int realIndex = startIndex + i * 8;
            VertexInfo v = VertexInfo.parseFromBuffer(lastV, Arrays.copyOfRange(b, realIndex, realIndex + 8));
            if ( null != v ){
                if ( !gpsValue.isVertexHasBeenAdded(v)) {
                    gpsValue.vertex.add(v);
                }
                lastV = v;
            }
        }
        return gpsValue;
    }
}
