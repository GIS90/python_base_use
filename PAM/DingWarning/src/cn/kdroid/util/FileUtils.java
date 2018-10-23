package cn.kdroid.util;

import java.io.*;
import java.net.URL;
import java.net.URLDecoder;
import java.util.Map;
import java.util.regex.Pattern;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.apache.log4j.Logger;
import org.apache.log4j.Priority;
import org.apache.log4j.RollingFileAppender;

public class FileUtils {
	private static Logger mLog = Logger.getLogger(FileUtils.class);

	// json写入文件
	public synchronized static void write2File(Object json, String fileName) {
		BufferedWriter writer = null;
		JSONObject eJSON = null;
		File file = new File(fileName);
		System.out.println("path:" + file.getPath() + " abs path:" + file.getAbsolutePath());
		if (!file.exists()) {
			try {
				file.createNewFile();
			} catch (Exception e) {
				mLog.info("createNewFile，出现异常:",e);
			}
		} else {
			eJSON = (JSONObject) read2JSON(fileName);
		}

		try {
//			writer = new BufferedWriter(new FileWriter(file));
			writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file.getAbsolutePath()),"UTF-8"));
			if (eJSON==null) {
				writer.write(json.toString());
			} else {
				Object[] array = ((JSONObject) json).keySet().toArray();
				for(int i=0;i<array.length;i++){
					eJSON.put(array[i].toString(), ((JSONObject) json).get(array[i].toString()));
				}
				writer.write(eJSON.toString());
			}

		} catch (IOException e) {
			mLog.info(e);
		} finally {
			try {
				if (writer != null) {
					writer.close();
				}
			} catch (IOException e) {
				mLog.info(e);
			}
		}

	}

	// 读文件到json
	public static JSONObject read2JSON(String fileName) {
		File file = new File(fileName);
		if (!file.exists()) {
			return null;
		}

		BufferedReader reader = null;
		String laststr = "";
		try {
//			reader = new BufferedReader(new FileReader(file));
			reader = new BufferedReader(new InputStreamReader(new FileInputStream(file.getAbsolutePath()),"UTF-8"));
			String tempString = null;
			while ((tempString = reader.readLine()) != null) {
				laststr += tempString;
			}
			reader.close();
		} catch (IOException e) {
			mLog.info(e);
		}

		return (JSONObject) JSON.parse(laststr);
	}

	// 通过key值获取文件中的value
	public static Object getValue(String fileName, String key) {
		JSONObject eJSON = null;
		eJSON = (JSONObject) read2JSON(fileName);
		if (null != eJSON && eJSON.containsKey(key)) {
			@SuppressWarnings("unchecked")
			Map<String, Object> values = JSON.parseObject(eJSON.toString(), Map.class);
			return values.get(key);
		} else {
			return null;
		}
	}
}
