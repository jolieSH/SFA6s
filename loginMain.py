# -*- coding: utf-8 -*-

import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver



#test on website
#driver = webdriver.Chrome()
#driver.get("http://180.166.98.84:8080/sfa5s/#/login")

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
#redmi
#desired_caps['platformVersion'] = '5.0.2'
#desired_caps['deviceName'] = 'LRX22G'

#samsung
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'SM-G9208'

desired_caps['browserName'] = ''
#desired_caps['app'] = PATH('C:\\Users\\Redmi\\Desktop\\sfa6s.apk')
desired_caps['appPackage'] = 'com.ebestmobile.sfa6s'
desired_caps['appActivity'] = 'com.ebestmobile.sfa6s.MainActivity'
desired_caps['unicodeKeyboard'] =True
desired_caps['resetKeyboard'] = True
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(5)


class Settings(object):
    def __init__(self,connection='标准',ip='idcsfaqatemp.ebestmobile.net', port='443', title='销售代表', language='中文'):
        self.connection=connection
        self.ip=ip
        self.port=port
        self.title=title
        self.language=language

class Account(object):
    def __init__(self,username='',password=''):
        self.username = username
        self.password = password

def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

def do_login_as(settings_info,user_info):
    driver.find_element_by_xpath("//android.widget.Button[@index='1']").click()

    #driver.find_element_by_xpath("//input[@type='text' and @class='ng-untouched ng-pristine ng-valid']").clear()
    #driver.find_element_by_xpath("//input[@type='text' and @class='ng-untouched ng-pristine ng-valid']").send_keys(settings_info.ip)
    #driver.find_element_by_xpath("//input[@type='number' and @class='ng-untouched ng-pristine ng-valid']").clear()
    #driver.find_element_by_xpath("//input[@type='number' and @class='ng-untouched ng-pristine ng-valid']").send_keys(settings_info.port)
    wh=getSize(driver)
    x1=int(wh[0] * 0.02)
    x2 = int(wh[0] * 0.05)
    y1=int(wh[1] * 0.95)
    y2=int(wh[1] * 0.98)
    driver.tap([(x1,y1),(x1,y2)],500)


    time.sleep(5)

    driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.EditText").clear()
    driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.EditText").send_keys(user_info.username)
    driver.find_element_by_xpath("//android.view.View[@index='1']/android.widget.EditText[@index='0']").clear()
    driver.find_element_by_xpath("//android.view.View[@index='1']/android.widget.EditText[@index='0']").send_keys(user_info.password)
    driver.find_element_by_accessibility_id("登录").click()







settings=Settings('标准','idcsfaqatemp.ebestmobile.net', '443', '销售代表', '中文')
SR = Account(username='ts08@dev.com',password='Test$2017')
#supervisor = Account(username='rose.yang@5s.corm',password='Rose$2016')


do_login_as(settings,SR)


