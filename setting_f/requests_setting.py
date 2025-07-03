
import requests;
import json;

'''

方法: 将传入该方法中的请求类型进行判定后调用requests对象的相应方法进行测试并返回响应信息
参数: 请请求方式   请求url   请求参数
返回值: 接口响应信息

'''

def requests_plus(inter_method,inter_url,inter_parm):
    inter_method = inter_method.lower()

    if inter_method == "get" or inter_method == "delete":

        resp = requests.get(url=inter_url,params=json.loads(inter_parm));

    elif inter_method == "post" or inter_method == "update":

        resp = requests.post(url=inter_url,data=json.loads(inter_parm));

    return resp;

'''
方法: 该方法的作用是通过传入的响应报文信息和预期结果进行判定
参数: 报文信息   预期结果
返回值: 判定结果
'''
import difflib;
from logs_f import log_file;

log_pro = log_file.get_log_pro();
def is_success_req(inter_name,resp_text,think):

    if difflib.SequenceMatcher(None,resp_text,think).ratio() > 0.8:

        is_finish = "√";
        log_pro.info(inter_name+"测试通过")

    else:

        is_finish = "×";
        log_pro.error(inter_name+"测试不通过")

    return is_finish;