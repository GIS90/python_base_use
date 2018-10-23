package com.tsnav;

import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import org.apache.log4j.Logger;
import org.apache.log4j.LogManager;

import java.util.concurrent.atomic.AtomicLong;

/**
 * User: mac
 * Date: 8/15/15
 * Time: 1:33 PM
 * To change this template use File | Settings | File Templates.
 */

public class FrameDecoder extends SimpleChannelInboundHandler<ByteBuf> {

    private Parser parser = new Parser();

    private static final Logger logger = LogManager.getLogger(FrameDecoder.class);

    private static AtomicLong gpsCount = new AtomicLong(0);

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) throws Exception {
        try {
            int length = msg.readableBytes();
            if (length <= 0) {
                logger.error("channelRead0 the length is less than 0 value is " + length);
                return;
            }
            byte[] body = new byte[length];
            msg.readBytes(body);
            GPSInfo info = this.parser.parseBuffer(body);
            if (info != null) {
                gpsCount.getAndIncrement();
                Gps2File.getInstance().writeToCache(info);
            }
            body = null;
        } catch (Exception e) {
            logger.error("channelRead0 " + e.getMessage());
            ctx.close();
        } finally {
            if (0 == gpsCount.get() % 10000) {
                logger.debug("GPS count " + gpsCount.get());
            }
        }
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        try {
            String msg = "exceptionCaught caught, error is " + cause.getMessage() + "remote addr is " + ctx.channel().remoteAddress().toString();
            logger.error(msg);
            super.exceptionCaught(ctx, cause);
        } catch (Exception e) {
            logger.error(e.getMessage());
        }
    }

    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception {
        try {
            super.channelInactive(ctx);
        } catch (Exception e) {
            logger.error("channelInactive got exception , remote addr is " + ctx.channel().remoteAddress().toString() + " error is " + e.getMessage());
        }
    }

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        try {
            super.channelActive(ctx);
        } catch (Exception e) {
            logger.error("channelActive got exception , remote addr is " + ctx.channel().remoteAddress().toString() + " error is " + e.getMessage());
        }
    }
}
