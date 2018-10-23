package cn.kdroid.core;

import cn.kdroid.base.Builder;
import cn.kdroid.exception.OApiException;
import cn.kdroid.exception.OApiResultException;
import cn.kdroid.helper.HttpHelper;
import cn.kdroid.util.Env;
import cn.kdroid.util.FileUtils;
import com.alibaba.fastjson.JSONObject;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public class TokenHandler {
    private static Logger mLog = Logger.getLogger(TokenHandler.class);
    private TokenHandler() {
    }

    // 调整到1小时50分钟
    public static final long cacheTime = 1000 * 60 * 55 * 2;
    public static SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    private String mCropId;
    private String mSecret;

    public static class DingBuilder implements Builder<TokenHandler> {

        TokenHandler handler;
        private String mCropId = Env.x().CORP_ID;
        private String mSecret = Env.x().CORP_SECRET;

        @Override
        public TokenHandler build() {
            handler = new TokenHandler();
            handler.mCropId = mCropId;
            handler.mSecret = mSecret;
            return handler;
        }

        public TokenHandler build(String cropId, String cropSerect) {
            mCropId = cropId;
            mSecret = cropSerect;
            return build();
        }

        public DingBuilder setCropId(String cropId) {
            mCropId = cropId;
            return this;
        }

        public DingBuilder setCropSecret(String cropSerect) {
            mSecret = cropSerect;
            return this;
        }
    }

    /*
    * 在此方法中，为了避免频繁获取access_token，
    * 在距离上一次获取access_token时间在两个小时之内的情况，
    * 将直接从持久化存储中读取access_token
    */
    public String getAccessToken(String corpId) throws OApiException, IOException {
        long curTime = System.currentTimeMillis();
        JSONObject accessTokenValue = (JSONObject) FileUtils.getValue(Env.getAbPath("accesstoken.json"), corpId);
        String accToken = "";
        if (accessTokenValue == null || curTime - accessTokenValue.getLong("begin_time") >= cacheTime) {
//            System.out.println(df.format(new Date()) + " authhelper: get new access_token");
            String url = Env.x().OAPI_HOST + "/gettoken?corpid=" + Env.x().CORP_ID + "&corpsecret=" + Env.x().CORP_SECRET;
            JSONObject response = HttpHelper.httpGet(url);
            JSONObject jsontemp = new JSONObject();
            if (response.containsKey("access_token")) {
                accToken = response.getString("access_token");
                // save accessToken
                JSONObject jsonAccess = new JSONObject();
                jsontemp.clear();
                jsontemp.put("access_token", accToken);
                jsontemp.put("begin_time", curTime);
                jsonAccess.put(corpId, jsontemp);
                FileUtils.write2File(jsonAccess, Env.getAbPath("accesstoken.json"));
            } else {
                throw new OApiResultException("Access_token");
            }
        } else {
            return accessTokenValue.getString("access_token");
        }
        return accToken;
    }

    public String getAccessToken() throws OApiException, IOException {
        return getAccessToken(Env.x().CORP_ID);
    }

}
