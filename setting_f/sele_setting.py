'''
方法: 该方法的功能是通过代码调用本地指定的浏览器并返回
参数: 传入要获取的浏览器
返回值: 指定的浏览器对象
'''
from selenium import webdriver;

import time;

from selenium.webdriver.common.by import By;

def get_browser(browse_name):

    #根据用户传入的浏览器名称获取不同的浏览器对象
    if browse_name == "chrome":

        return webdriver.Chrome();

    elif browse_name == "firefox":

        return webdriver.Firefox();

    elif browse_name == "edge":

        return webdriver.Edge();

    else:

        print("你调用的浏览器暂不支持!")

'''
方法: 该方法的作用是将传入的浏览器对象进行登录，将登录信息缓存在浏览器对象中并返回


'''
def login(llq):

    llq.get("http://127.0.0.1:8008");

    time.sleep(3);

    llq.find_element(by=By.NAME, value="username").clear();
    time.sleep(1)
    llq.find_element(by=By.NAME, value="username").send_keys("admin");
    time.sleep(1)
    llq.find_element(by=By.NAME, value="password").clear();
    time.sleep(1)
    llq.find_element(by=By.NAME, value="password").send_keys("admin123");
    time.sleep(1)
    llq.find_element(by=By.ID, value="btnSubmit").click();
    time.sleep(5)

    return llq;