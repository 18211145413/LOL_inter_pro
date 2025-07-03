from  setting_f import Excel_setting,requests_setting;
import pytest;
import allure;

resp_text_list = [];

is_finish_list = [];


'''
方法: 该方法的作用是通过pytest的数据驱动执行获取到的接口信息
参数: 接口
返回值: 无

'''
@allure.epic("LOL项目接口测试")
@allure.feature("lol模块")
@pytest.mark.parametrize("inter_message",Excel_setting.read_case_turn_interlist("C:\Mac\Home\Desktop\zuoye.xls","lol"))
def test_case_lol_sheet(inter_message):
    resp_text_list = [];

    is_finish_list = [];
    allure.dynamic.title(inter_message.get("jk_name"));
    result = requests_setting.requests_plus(inter_message.get("jk_method"),inter_message.get("jk_url"),inter_message.get("jk_parm"));

    is_finish = requests_setting.is_success_req(inter_message.get("jk_name"),result.text,inter_message.get("jk_think"));

    resp_text_list.append(result.text);

    is_finish_list.append(is_finish);

def test_write_lol_test_result():

    Excel_setting.write_case(resp_text_list,is_finish_list,"C:\Mac\Home\Desktop\zuoye.xls","lol")


@allure.epic("LOL项目接口测试")
@allure.feature("emp模块")
@pytest.mark.parametrize("inter_message",Excel_setting.read_case_turn_interlist("C:\Mac\Home\Desktop\zuoye.xls","emp"))
def test_case_emp_sheet(inter_message):
    resp_text_list = [];

    is_finish_list = [];
    allure.dynamic.title(inter_message.get("jk_name"));
    result = requests_setting.requests_plus(inter_message.get("jk_method"),inter_message.get("jk_url"),inter_message.get("jk_parm"));

    is_finish = requests_setting.is_success_req(inter_message.get("jk_name"),result.text,inter_message.get("jk_think"));

    resp_text_list.append(result.text);

    is_finish_list.append(is_finish);

def test_write_emp_test_result():

    Excel_setting.write_case(resp_text_list,is_finish_list,"C:\Mac\Home\Desktop\zuoye.xls","emp")



@allure.epic("LOL项目接口测试")
@allure.feature("shop模块")
@pytest.mark.parametrize("inter_message",Excel_setting.read_case_turn_interlist("C:\Mac\Home\Desktop\zuoye.xls","shop"))
def test_case_shop_sheet(inter_message):
    resp_text_list = [];

    is_finish_list = [];
    allure.dynamic.title(inter_message.get("jk_name"));
    result = requests_setting.requests_plus(inter_message.get("jk_method"),inter_message.get("jk_url"),inter_message.get("jk_parm"));

    is_finish = requests_setting.is_success_req(inter_message.get("jk_name"),result.text,inter_message.get("jk_think"));

    resp_text_list.append(result.text);

    is_finish_list.append(is_finish);

def test_write_shop_test_result():

    Excel_setting.write_case(resp_text_list,is_finish_list,"C:\Mac\Home\Desktop\zuoye.xls","shop")


