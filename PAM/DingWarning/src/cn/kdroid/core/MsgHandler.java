package cn.kdroid.core;

import cn.kdroid.base.Builder;
import cn.kdroid.exception.OApiException;
import cn.kdroid.exception.OApiResultException;
import cn.kdroid.helper.HttpHelper;
import cn.kdroid.util.Env;
import com.alibaba.fastjson.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public class MsgHandler {
    public static final String TO_USER = "touser";
    public static final String TO_PARTY = "toparty";
    public static final String TEXT = "text";
    public static final String CONTENT = "content";
    public static final String AGENT_ID = "agentid";
    public static final String MSG_TYPE = "msgtype";

    private boolean mToUser;
    private boolean mToParty;
    private String mToUV;
    private String mToPV;
    private String mAgentId;
    private String mMsgType;

    private MsgHandler() {
    }

    public static class MessageBuilder implements Builder<MsgHandler> {
        private MsgHandler handler;
        private UserHandler userHandler;
        private DepartmentHandler partyHandler;
        private final String TO_ALL = "@all";
        private boolean mToUser = true;
        private boolean mToParty = false;
        private String mToUV = TO_ALL;
        private String mToPV = TO_ALL;
        private String mAgentId = Env.x().AGENTID;
        private String mMsgType = TEXT;

        @Override
        public MsgHandler build() throws OApiException {
            handler = new MsgHandler();
            handler.mToUser = mToUser;
            handler.mToParty = mToParty;
            handler.mToUV = mToUV;
            handler.mToPV = mToPV;
            handler.mAgentId = mAgentId;
            handler.mMsgType = mMsgType;
            return handler;
        }


        public MessageBuilder setToUserValue(String value) throws OApiException, IOException {
            if(value==null){
                return this;
            }
            mToUser = true;
            String[] split = value.split("\\|");
            List<String> names = new ArrayList<String>();
            for (String s : split) {
                names.add(s);
            }

            if (names.size() == 0) {
                throw new OApiException(1, "there is not any people in dingtalk cause by input user list:[\"" + value + "\"]");
            }
            mToUV = getUserHandler().getUsers(names);
            return this;
        }

        public MessageBuilder setToUserValue(List values) throws OApiException, IOException {
            if (values == null || values.size() == 0) {
                throw new OApiException(1, "there is not any people in dingtalk cause by input user list");
            }
            mToUser = true;
            mToUV = getUserHandler().getUsers(values);
            return this;
        }

        public MessageBuilder setToPartyValue(String value) throws OApiException, IOException {
            if(value==null){
                return this;
            }
            mToParty = true;
            if(TO_ALL.equals(mToUV)){
                mToUser = false;
            }
            String[] split = value.split("\\|");
            List<String> names = new ArrayList<String>();
            for (String s : split) {
                names.add(s);
            }
            if (names.size() == 0) {
                throw new OApiResultException("there is not any people in dingtalk cause by input user list:[\"" + value + "\"]");
            }
            mToPV = getPartyHandler().getDepartsString(names);
            return this;
        }

        public MessageBuilder setToPartyValue(List values) throws OApiException, IOException {
            if (values == null || values.size() == 0) {
                throw new OApiException(1, "there is not any party in dingtalk cause by input party list");
            }
            mToParty = true;
            mToPV = getPartyHandler().getDepartsString(values);
            return this;
        }

        public MessageBuilder setAgentId(String agentId) {
            mAgentId = agentId;
            return this;
        }

        public void setUserHandler(UserHandler userHandler) {
            this.userHandler = userHandler;
        }

        private UserHandler getUserHandler() {
            if (userHandler == null) {
                userHandler = new UserHandler.UserBuilder().build();
            }
            return userHandler;
        }

        private DepartmentHandler getPartyHandler() {
            if (partyHandler == null) {
                partyHandler = new DepartmentHandler(Env.x().CORP_ID);
            }
            return partyHandler;
        }

        public void setPartyHandler(DepartmentHandler partyHandler) {
            this.partyHandler = partyHandler;
        }

        public boolean checker(Object var) {
            return var == null ? true : false;
        }
    }

    /**
     * {"touser":"@all","agentid":"10411984","msgtype":"text","text":{"content":""}}
     * touser : "@all" | "userid1|userid2"
     *
     * @param accessToken
     */
    public boolean sendText(String accessToken, String content) throws OApiException, IOException {
        String url = Env.x().OAPI_HOST + "/message/send?access_token=" + accessToken;
        JSONObject textJson = new JSONObject();
        textJson.put(CONTENT, content);
        JSONObject args = new JSONObject();
        if (mToUser) {
            args.put(TO_USER, mToUV);
        }
        if (mToParty) {
            args.put(TO_PARTY, mToPV);
        }
        args.put(AGENT_ID, mAgentId);
        args.put(MSG_TYPE, mMsgType);
        args.put(TEXT, textJson);
//        System.out.println(JSON.toJSON(args));
        JSONObject response = HttpHelper.httpPost(url, args);
        return true;
    }

    public boolean sendText(String content) throws OApiException, IOException {
        TokenHandler handler = new TokenHandler.DingBuilder().build();
        String accessToken = handler.getAccessToken();
        sendText(accessToken, content);
        return true;
    }
}
