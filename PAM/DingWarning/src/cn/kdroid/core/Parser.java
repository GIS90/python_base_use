package cn.kdroid.core;

import cn.kdroid.exception.OApiException;
import cn.kdroid.util.Env;
import org.apache.commons.cli.*;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.log4j.Logger;
import org.apache.log4j.Priority;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.Collection;
import java.util.List;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public class Parser {
    /*日志管理器*/
    private static Logger mLog = Logger.getLogger(Parser.class);

    public static void main(String args[]){
        try {
            String userValue = null;
            String partyValue = null;
            String msg = null;
            CommandLineParser parser = new BasicParser();
            Options options = new Options();
            options.addOption("h", "help", false,"Help Message");
            options.addOption("u", "uvalue", true, "[name1|name2] send msg to some people\n");
            options.addOption("p", "pvalue", true, "[partname1|partname2] send msg to some department");
            options.addOption("m", "msg", true, "message");
            // Parse the program arguments
            CommandLine commandLine = parser.parse(options, args);
            // Set the appropriate variables based on supplied options
            if (commandLine.hasOption('h')) {
                Collection<Option> options1 = options.getOptions();
                for(Option option: options1){
                    System.out.println("-"+option.getOpt()+"\t-"+option.getLongOpt()+"\t"+option.getDescription());
                }
                System.exit(0);
            }

            if (commandLine.hasOption("u")) {
                userValue = commandLine.getOptionValue("u");
            }
            if (commandLine.hasOption("p")) {
                partyValue = commandLine.getOptionValue("p");
            }
            if (commandLine.hasOption('m')) {
                msg = commandLine.getOptionValue('m');
            }


            new MsgHandler.MessageBuilder()
                    .setToUserValue(userValue)
                    .setToPartyValue(partyValue)
                    .build().sendText(msg);
            System.err.println("true");
        } catch (Exception e) {
            System.err.println("false");
//            mLog.info(e);
        } finally {
            System.exit(0);
        }
    }



}
