package com.tsnav;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

public class Main {

    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        new Thread(Gps2File.getInstance()).start();
        System.setProperty("sun.net.client.defaultReadTimeout", String.valueOf(10000));
        TCPServer server = new TCPServer();
        server.run4ever();
    }
}
