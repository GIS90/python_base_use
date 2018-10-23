package cn.kdroid.test;

import cn.kdroid.core.*;
import cn.kdroid.exception.OApiException;
import cn.kdroid.util.Env;
import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Huangjianxiong on 2016/2/16.
 * Email: kdroid@163.com
 */
public class DebugUtil {
    @Test
    public void testAccessToken() throws IOException, OApiException {
            String accessToken = new TokenHandler.DingBuilder().build().getAccessToken();
            System.out.print(accessToken);
    }

    /**
     * {"touser":"@all","agentid":"10411984","msgtype":"text","text":{"content":""}}
     */
    @Test
    public void testSend() throws IOException {
        try {
            String msg = "您好，Builder";
//            DingHandler handler = new DingHandler.DingBuilder().build();
//            System.out.println(handler.getAccessToken());
            new MsgHandler.MessageBuilder().build().sendText(msg);
        } catch (OApiException e) {
            e.printStackTrace();
        }
    }
    @Test
    public void testUsers(){
        try {
            List<String> list = new ArrayList<String>();
            list.add("黄剑雄");
            list.add("Manager");
            String users = new UserHandler.UserBuilder().build().getUsers(list);
            System.out.println(users);
        } catch (OApiException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testSendByName() throws IOException {
        try {
            String msg = "您好，huang";
            new MsgHandler.MessageBuilder().setToUserValue("黄剑雄").build().sendText(msg);
        } catch (OApiException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testDepartment(){
        try {
            List list = new ArrayList();
            list.add("技术部");
            list.add("kdroid");
            String departsString = new DepartmentHandler(Env.x().CORP_ID).getDepartsString(list);
            System.out.println(departsString);
        } catch (OApiException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
