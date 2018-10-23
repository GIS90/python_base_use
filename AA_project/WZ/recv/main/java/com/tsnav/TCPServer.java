package com.tsnav;

import io.netty.channel.*;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;


/**
 * User: mac
 * Date: 7/28/15
 * Time: 2:47 PM
 * To change this template use File | Settings | File Templates.
 */
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;


public class TCPServer {

    private static final int listenPort = 58000;

    private static final Logger logger = LogManager.getLogger(TCPServer.class);

    public void run4ever() {
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            logger.debug("TCPServer started");
            ServerBootstrap sbs = new ServerBootstrap();
            sbs.group(bossGroup, workerGroup);
            sbs.channel(NioServerSocketChannel.class);
            sbs.childHandler(new TCPConnection());
            sbs.childOption(ChannelOption.TCP_NODELAY, true);
            sbs.childOption(ChannelOption.SO_RCVBUF, 8 * 1024 * 1024);
            sbs.childOption(ChannelOption.SO_SNDBUF, 8 * 1024 * 1024);
            sbs.childOption(ChannelOption.SO_KEEPALIVE, true);
            sbs.childOption(ChannelOption.SO_REUSEADDR, true);
            sbs.bind(TCPServer.listenPort).sync().channel().closeFuture().sync();
        } catch (Exception e) {
            logger.fatal("Server for client is ERROR!!" + e.getMessage());
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }
}
