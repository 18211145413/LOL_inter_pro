import logging;
import datetime;
'''
方法: 该方法的作用是自定义一个日志对象，并进行日志的配置，返回该日志对象
参数: 无
返回值: 日志对象

'''

def get_log_pro():

    log_info = logging.getLogger("接口日志对象");

    log_info.setLevel(logging.DEBUG);

    s_h = logging.StreamHandler();
    log_file_name = str(datetime.datetime.today()).split(" ")[0]
    f_h = logging.FileHandler("../logs_f/"+log_file_name+".log",encoding="utf-8");

    log_formatter = logging.Formatter("--%(asctime)s--%(name)s--%(levelname)s--%(filename)s:[%(lineno)d]--%(message)s");

    s_h.setFormatter(log_formatter);

    f_h.setFormatter(log_formatter);

    log_info.addHandler(s_h);

    log_info.addHandler(f_h);

    return log_info;

get_log_pro()