package com.tsnav;

import io.netty.channel.Channel;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInitializer;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

/**
 * User: mac
 * Date: 8/15/15
 * Time: 12:53 PM
 * To change this template use File | Settings | File Templates.
 */

//public class TCPChannelHandler extends SimpleChannelInboundHandler<Integer> {
public class TCPConnection extends ChannelInitializer {

    private static final Logger logger = LogManager.getLogger(TCPConnection.class);

    @Override
    protected void initChannel(Channel ch) throws Exception {
        logger.debug("TCPConnection got new connection from " + ch.remoteAddress().toString());
        ch.pipeline().addFirst(new HeaderDecoder());
        ch.pipeline().addLast(new FrameDecoder());
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        try {
            super.exceptionCaught(ctx, cause);
            ctx.close();
        } catch (Exception e) {
            String msg = "exceptionCaught exception, error is " + cause.getMessage() + " remote addr is " + ctx.channel().remoteAddress().toString();
            logger.error(msg);
        }
    }

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        super.channelActive(ctx);
    }
}
