package com.tsnav;

/**
 * User: mac
 * Date: 7/28/15
 * Time: 2:48 PM
 * To change this template use File | Settings | File Templates.
 */

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;


class TCPConn implements Runnable{

    private boolean mRunFlag = false;

    private static final Logger logger = LogManager.getLogger(TCPConn.class);

    private ByteBuffer headerBuffer = ByteBuffer.allocate(2);

    private boolean isHeaderRead = false;

    private Parser parser = new Parser();

    TCPConn() {
        this.mRunFlag = true;
    }

    public void handleRead(SocketChannel sc) throws IOException{
        if (!isHeaderRead ) {
            sc.read(headerBuffer);
            isHeaderRead = true;
        } else {
            int bodyLen = EndianTransform.littleToInt(this.headerBuffer.array());
            if ( 0 == bodyLen ) {
                logger.error("handleRead bodyLen is 0");
                return;
            }
            ByteBuffer bodyBuffer = ByteBuffer.allocate(bodyLen);
            int value = sc.read(bodyBuffer);
            if ( value != bodyLen ) {
                return;
            }
            GPSInfo info = parser.parseBuffer(bodyBuffer.array());
            if ( null != info ) {
                GPSToFile.getInstance().writeToCache(info);
            } else {
                System.out.println("aaa");
            }
            bodyBuffer.clear();
            this.headerBuffer.clear();
            bodyBuffer = null;
            isHeaderRead = false;
        }
    }

    public void run() {

    }

//    private byte [] blockRead(SocketChannel sc, int len) throws IOException
//    {
//        if ( 0 == len ){
//            return null;
//        }
//        InputStream is = sc.socket().getInputStream();
//        byte [] retval = new byte[len];
//        if ( -1 == is.read(retval, 0, len) ){
//            return null;
//        }
//        return retval;
//    }

    private void stop(){
        this.mRunFlag = false;
        try{
            this.wait();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
