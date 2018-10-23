package com.tsnav;

import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.LengthFieldBasedFrameDecoder;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import java.nio.ByteOrder;

/**
 * User: mac
 * Date: 8/15/15
 * Time: 9:41 PM
 * To change this template use File | Settings | File Templates.
 */

public class HeaderDecoder extends LengthFieldBasedFrameDecoder {

    private static final Logger logger = LogManager.getLogger(HeaderDecoder.class);

    public HeaderDecoder() {
        super(ByteOrder.LITTLE_ENDIAN, 65535, 0, 2, 0, 2, true);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        try {
            super.exceptionCaught(ctx, cause);
            ctx.close();
        } catch (Exception e) {
            logger.error("HeaderDecoder got exception, error is " + cause.getMessage() + " remote addr is " + ctx.channel().remoteAddress().toString());
            cause.printStackTrace();
        }
    }
}
