package cn.kdroid.core;

import cn.kdroid.exception.OApiException;
import cn.kdroid.exception.OApiResultException;
import cn.kdroid.helper.HttpHelper;
import cn.kdroid.util.Env;
import cn.kdroid.util.FileUtils;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.List;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public class DepartmentHandler {
    private String cropId = Env.x().CORP_ID;
    public DepartmentHandler(String cropId) {
        this.cropId  = cropId;
    }

    // 调整到23小时50分钟
    public static final long cacheTime = 1000 * 60 * (60 * 24 - 10);
    public static SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");


    public String getDepartsString(List<String> names) throws OApiException, IOException {
        String ret = "";
        String users = getDeparts();
        List<JSONObject> list = JSON.parseObject(users, List.class);
        for (String name : names) {
            for (JSONObject object : list) {
                if (object.getString("name").equals(name)) {
                    ret += object.getString("id");
                    ret += "|";
                    break;
                }
            }
        }
        if (ret.length() != 0) {
            ret = ret.substring(0, ret.length() - 1);
        }
        return ret;
    }

    public String getDeparts() throws OApiException, IOException {
        return getDeparts(new TokenHandler.DingBuilder().build().getAccessToken());
    }

    /*
    * 在此方法中，为了避免频繁获取用户列表，
    * 在距离上一次获取users时间在一天内的情况，
    * 将直接从持久化存储中读取
    * https://oapi.dingtalk.com/user/simplelist?access_token=d189027a25be34e39608a4026afd969e&department_id=1
    * {"errcode":0,"errmsg":"ok","userlist":[{"name":"黄剑雄","userid":"01661269049021"},{"name":"黄剑雄","userid":"manager3935"}]
    */
    public String getDeparts(String accessToken) throws OApiException, IOException {
        long curTime = System.currentTimeMillis();
        JSONObject usersValue = (JSONObject) FileUtils.getValue(Env.getAbPath("depart.json"), cropId);
        String userlist = "";
        if (usersValue == null || curTime - usersValue.getLong("begin_time") >= cacheTime) {
//            System.out.println(df.format(new Date()) + " departhandler: get all department info");
            String url = Env.x().OAPI_HOST + "/department/list?access_token=" + accessToken;
            JSONObject response = HttpHelper.httpGet(url);
            JSONObject jsontemp = new JSONObject();
            if (response.containsKey("department")) {
                userlist = response.getString("department");
                // save userlist
                JSONObject userList = new JSONObject();
                jsontemp.clear();
                jsontemp.put("department", userlist);
                jsontemp.put("begin_time", curTime);
                userList.put(cropId, jsontemp);
                FileUtils.write2File(userList,Env.getAbPath("depart.json"));
            } else {
                throw new OApiResultException("get departmeng list exception");
            }
        } else {
            return usersValue.getString("department");
        }
        return userlist;
    }
}
