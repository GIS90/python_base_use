# -*- coding: utf-8 -*-
"""
内置一些常用的方法
"""
import datetime
import os


def current_stime():
    dt = datetime.datetime.now()
    format_time = '%Y-%m-%d %H:%M:%S'
    now = dt.strftime(format_time)
    return now


def current_time():
    return datetime.datetime.now()


def time_transfer_str(dt):
    format_time = '%Y-%m-%d %H:%M:%S'
    return dt.strftime(format_time)


def get_config_file():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    config_dir = os.path.abspath(os.path.join(os.path.join(__curr_dir, '..'), 'config'))
    config_file = os.path.abspath(os.path.join(__config_dirr, "config.toml"))
    return config_dir, config_file


def cal_time(seconds):

    assert isinstance(seconds, int)
    DAY = 24 * 60 * 60
    HOUR = 1 * 60 * 60
    MINUTE = 1 * 60

    if seconds < MINUTE:
        second = seconds
        return "cost time is %d second" % second
    elif seconds < HOUR:
        if seconds % MINUTE == 0:
            minute = seconds / MINUTE
            return "cost time is %d minute" % minute
        else:
            minute = seconds / MINUTE
            second = seconds % MINUTE
            return "cost time is %d minute %d second " % (minute, second)
    elif seconds < DAY:
        if seconds % HOUR == 0:
            hour = seconds / HOUR
            return "cost time is %d hour" % hour
        elif seconds % MINUTE == 0:
            hour = seconds / HOUR
            minute = (seconds - hour * HOUR) / MINUTE
            return "cost time is %d minute %d second " % (hour, minute)
        else:
            hour = seconds / HOUR
            minute = (seconds - hour * HOUR) / MINUTE
            second = (seconds - hour * HOUR) % MINUTE
            return "cost time is %d hour %d minute %d second " % (hour, minute, second)
    else:
        if seconds % DAY == 0:
            day = seconds / DAY
            return "cost time is %d day" % day
        elif seconds % HOUR == 0:
            day = seconds / DAY
            hour = (seconds - day * DAY) / HOUR
            return "cost time is %d day %d hour" % (day, hour)
        elif seconds % MINUTE == 0:
            day = seconds / DAY
            hour = (seconds - day * DAY) / HOUR
            minute = (seconds - day * DAY - hour * HOUR) / MINUTE
            return "cost time is %d day %d minute %d second " % (day, hour, minute)
        else:
            day = seconds / DAY
            hour = (seconds - day * DAY) / HOUR
            minute = (seconds - day * DAY - hour * HOUR) / MINUTE
            second = (seconds - day * DAY - hour * HOUR) % MINUTE
            return "cost time is %d day %d hour %d minute %d second " % (day, hour, minute, second)







cal_time(3601001)