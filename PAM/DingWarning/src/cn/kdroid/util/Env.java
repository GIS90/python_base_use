package cn.kdroid.util;

import com.alibaba.fastjson.JSONObject;
import org.apache.log4j.Logger;

import java.io.File;
import java.lang.reflect.Field;
import java.net.URL;
import java.net.URLDecoder;

/**
 * Created by Huangjianxiong on 2016/2/16.
 * Email: kdroid@163.com
 */
public class Env {
    private Env() {
        init();
    }

    /*日志管理器*/
    private static Logger mLog = Logger.getLogger(Env.class);
    public String OAPI_HOST = "";
    public String CORP_ID = "";
    public String CORP_SECRET = "";
    public String SSO_Secret = "";
    public String AGENTID = "";
    private static Env env = null;

    public static Env x() {
        if (env == null) {
            synchronized (Env.class) {
                if (env == null) {
                    env = new Env();
                }
            }
        }
        return env;
    }

    private void init() {
        String path = new File(getAbPath("config.json")).getAbsolutePath();
        JSONObject object = FileUtils.read2JSON(path);
        if (object == null || object.size() == 0) {
            return;
        }
        Class ownerClass = Env.class;
        Field[] declaredFields = ownerClass.getDeclaredFields();

        for (Field field : declaredFields) {
            String string = object.getString(field.getName());
            if (string != null) {
                try {
                    field.set(this, string);
                } catch (IllegalAccessException e) {
                    mLog.info(e);
                }
            }
        }
    }


    public static String getAbPath(String path) {
        URL url = Env.class.getProtectionDomain().getCodeSource().getLocation();
        String filePath = null;
        try {
            filePath = URLDecoder.decode(url.getPath(), "utf-8");// 转化为utf-8编码
        } catch (Exception e) {
            mLog.info(e);
        }
        if (filePath.endsWith(".jar")) {// 可执行jar包运行的结果里包含".jar"
            // 截取路径中的jar包名
            filePath = filePath.substring(0, filePath.lastIndexOf("/") + 1);
            filePath+= path;
            filePath = new File(filePath).getAbsolutePath();
            return filePath;
        }else{
            return path;
        }
    }
}
