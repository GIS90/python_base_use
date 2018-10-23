package cn.kdroid.base;

import cn.kdroid.exception.OApiException;

/**
 * Created by Huangjianxiong on 2016/2/17.
 * Email: kdroid@163.com
 */
public interface Builder<T> {
    T build() throws OApiException;
}
