package com.tsnav;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * User: mac
 * Date: 7/30/15
 * Time: 1:19 PM
 * To change this template use File | Settings | File Templates.
 */

class TimeUtil {

    public static String toUTCString(long utcTime) {
        java.text.DateFormat format = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        long utcTimeInMill = utcTime * 1000;
        Calendar c = Calendar.getInstance();
        c.setTimeInMillis(utcTimeInMill);
        return format.format(c.getTime());
    }

    public static String getCurrentTime() {
        SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");
        return df.format(new Date());
    }

    public static void Sleep(long millSeconds) {
        try {
            Thread.sleep(millSeconds);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
