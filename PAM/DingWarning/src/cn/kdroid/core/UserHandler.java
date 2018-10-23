package cn.kdroid.core;

import cn.kdroid.base.Builder;
import cn.kdroid.exception.OApiException;
import cn.kdroid.exception.OApiResultException;
import cn.kdroid.helper.HttpHelper;
import cn.kdroid.util.Env;
import cn.kdroid.util.FileUtils;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public class UserHandler {

    private UserHandler() {
    }

    // 调整到23小时50分钟
    public static final long cacheTime = 1000 * 60 * (60 * 24 - 10);
    public static SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    private String mDepartId;
    private String mCropId;

    public static class UserBuilder implements Builder<UserHandler> {
        UserHandler handler;
        private String mDepartId = "1";
        private String mCropId = Env.x().CORP_ID;

        @Override
        public UserHandler build() {
            handler = new UserHandler();
            handler.mDepartId = mDepartId;
            handler.mCropId = mCropId;
            return handler;
        }

        public UserHandler build(String cropId, String departId) {
            mDepartId = departId;
            mCropId = cropId;
            return build();
        }

        public UserBuilder setDepartId(String departId) {
            mDepartId = departId;
            return this;
        }

        public UserBuilder setCropId(String cropId) {
            mCropId = cropId;
            return this;
        }
    }

    public String getUsers(List<String> names) throws OApiException, IOException {
        String ret = "";
        String users = getUsersJson();
        List<JSONObject> list = JSON.parseObject(users, List.class);
        for (String name : names) {
            for (JSONObject object : list) {
                if (object.getString("name").equals(name)) {
                    ret += object.getString("userid");
                    ret += "|";
                    break;
                }
            }
        }
        if (ret.length() != 0) {
            ret = ret.substring(0, ret.length() - 1);
        } else {
            throw new OApiException(1, "not found any person in your input person list");
        }
        return ret;
    }

    public String getUsersJson() throws OApiException, IOException {
        return getUsers(new TokenHandler.DingBuilder().build().getAccessToken());
    }

    /*
    * 在此方法中，为了避免频繁获取用户列表，
    * 在距离上一次获取users时间在一天内的情况，
    * 将直接从持久化存储中读取
    * https://oapi.dingtalk.com/user/simplelist?access_token=d189027a25be34e39608a4026afd969e&department_id=1
    * {"errcode":0,"errmsg":"ok","userlist":[{"name":"黄剑雄","userid":"01661269049021"},{"name":"黄剑雄","userid":"manager3935"}]
    */
    public String getUsers(String accessToken) throws OApiException, IOException {
        long curTime = System.currentTimeMillis();
        JSONObject usersValue = (JSONObject) FileUtils.getValue(Env.getAbPath("users.json"), mDepartId);
        String userlist = "";
        if (usersValue == null || curTime - usersValue.getLong("begin_time") >= cacheTime) {
//            System.out.println(df.format(new Date()) + " userhandler: get all userinfo");
            String url = Env.x().OAPI_HOST + "/user/simplelist?access_token=" + accessToken + "&department_id=" + mDepartId;
            JSONObject response = HttpHelper.httpGet(url);
            JSONObject jsontemp = new JSONObject();
            if (response.containsKey("userlist")) {
                userlist = response.getString("userlist");
                // save userlist
                JSONObject userList = new JSONObject();
                jsontemp.clear();
                jsontemp.put("userlist", userlist);
                jsontemp.put("begin_time", curTime);
                userList.put(mDepartId, jsontemp);
                FileUtils.write2File(userList, Env.getAbPath("users.json"));
            } else {
                throw new OApiResultException("get userlist exception");
            }
        } else {
            return usersValue.getString("userlist");
        }
        return userlist;
    }
}
