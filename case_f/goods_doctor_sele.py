from setting_f import sele_setting;
import time;
from selenium.webdriver.common.by import By;

from selenium.webdriver.support.select import Select;
import pytest;
llq = sele_setting.get_browser("edge");

@pytest.mark.parametrize("uname,upwd,title",[("admin","123456","登录医药管理系统"),("adminsss","admin123","登录医药管理系统"),("sdcsdcs","csdcsd","登录医药管理系统1212"),
                                       ("admin","admin123","管理系统")])
def test_login(uname,upwd,title):

    llq.get("http://127.0.0.1:8008");

    time.sleep(3);

    llq.find_element(by=By.NAME,value="username").clear();
    time.sleep(3)
    llq.find_element(by=By.NAME,value="username").send_keys(uname);
    time.sleep(3)
    llq.find_element(by=By.NAME,value="password").clear();
    time.sleep(3)
    llq.find_element(by=By.NAME,value="password").send_keys(upwd);
    time.sleep(3)
    llq.find_element(by=By.ID,value="btnSubmit").click();
    time.sleep(5)
    #判定登录成功与否
    assert llq.title == title;

def test_click_index():

    login_llq = sele_setting.login(llq);

    time.sleep(5);

    login_llq.find_element(by=By.LINK_TEXT,value="首页").click();

def test_medicien_manage():

    login_llq = sele_setting.login(llq);

    time.sleep(3);

    login_llq.find_element(by=By.LINK_TEXT, value="管理").click();

    time.sleep(3);

    login_llq.find_element(by=By.LINK_TEXT, value="药品").click();

    time.sleep(3);

    frame1 = login_llq.find_element(by=By.XPATH,value="html/body/div/div/div[3]/iframe[2]");

    login_llq.switch_to.frame(frame1);

    #获取执行添加前的总条数
    before_num_text = login_llq.find_element(by=By.XPATH,value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text.split("，")[1];

    before_num = before_num_text[2:len(before_num_text)-3];


    login_llq.find_element(by=By.LINK_TEXT, value="添加").click();

    time.sleep(5);

    login_llq.switch_to.default_content();

    time.sleep(5);

    add_frame = login_llq.find_element(by=By.XPATH,value="html/body/div[3]/div[2]/iframe");

    time.sleep(3)
    login_llq.switch_to.frame(add_frame);

    time.sleep(3);

    login_llq.find_element(by=By.NAME,value="productName").send_keys("大力丸");

    time.sleep(3);

    select_obj = login_llq.find_element(by=By.NAME, value="supplierId");

    time.sleep(3)
    Select(select_obj).select_by_index(1);

    time.sleep(3);
    select_obj_unit = login_llq.find_element(by=By.NAME, value="unit");
    time.sleep(3)
    Select(select_obj_unit).select_by_index(3);
    time.sleep(3)
    login_llq.find_element(by=By.NAME,value="stockNum").send_keys("100");

    time.sleep(3)

    login_llq.find_element(by=By.NAME, value="intPrice").send_keys("80");

    time.sleep(3)

    login_llq.find_element(by=By.NAME, value="outPrice").send_keys("400");

    time.sleep(3)

    login_llq.switch_to.default_content();

    login_llq.find_element(by=By.LINK_TEXT,value="确定").click();

    time.sleep(5);

    login_llq.switch_to.frame(frame1);

    # 获取执行添加前的总条数

    after_num_text = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text.split("，")[1];

    after_num = after_num_text[2:len(after_num_text) - 3];

    print(before_num,"=---------=",after_num)

    assert after_num > before_num;

    login_llq.quit();













