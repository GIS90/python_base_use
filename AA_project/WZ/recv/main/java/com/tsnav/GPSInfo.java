package com.tsnav;

import java.math.BigInteger;
import java.util.List;

/**
 * User: mac
 * Date: 7/29/15
 * Time: 6:28 PM
 * To change this template use File | Settings | File Templates.
 */


class GPSInfo {
    public BigInteger getID() {
        return this.ID;
    }

    public int getNavStat() {
        return this.navStat;
    }

    public int getVertexNum() {
        return this.vertexNum;
    }

    public int getLon() {
        return this.lon;
    }

    public int getLat() {
        return this.lat;
    }

    public int getTime() {
        return this.time;
    }

    public int getSpeed() {
        return this.speed;
    }

    public int getAngle() {
        return this.angle;
    }

    public List<VertexInfo> getVertex() {
        return this.vertex;
    }

    private String prettyPrint() {
        String ID = String.valueOf(this.ID);
        String navStat = String.valueOf(this.navStat);
        String lon = String.valueOf(this.lon / 1000000.0);
        String lat = String.valueOf(this.lat / 1000000.0);
        String time = TimeUtil.toUTCString(this.time);
        String speed = String.valueOf(this.speed);
        String angle = String.valueOf(this.angle);
        return time + " " + ID + " " + navStat + " " + lon + " " + lat + " " + speed + " " + angle;
    }

    public String prettyPrintAll() {
        String retval = this.prettyPrint() + "\n";
        for (VertexInfo aVertex : this.vertex) {
            retval += aVertex.formatByGPSInfo(this);
            retval += "\n";
        }
        return retval;
    }

    public boolean isVertexHasBeenAdded(VertexInfo v) {
        int size = this.vertex.size();
        if (size == 0) {
            return false;
        }
        for (VertexInfo theValue : this.vertex) {
            if (VertexInfo.isVertexEqual(v, theValue)) {
                return true;
            }
        }
        return false;
    }

    public BigInteger ID;
    public int navStat;
    public int vertexNum;
    public int lon;
    public int lat;
    public int time;
    public int speed;
    public int angle;
    public List<VertexInfo> vertex;
}
