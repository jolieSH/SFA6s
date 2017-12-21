# -*- coding: utf-8 -*-

import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

class login(unittest.TestCase):
    def setUp(self):
        self.PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
        self.desired_caps={'platformName': 'Android','platformVersion': '6.0.1','deviceName': 'SM-G9208',
                           'browserName': '','appPackage':'com.ebestmobile.sfa6s','appActivity':'com.ebestmobile.sfa6s.MainActivity'}
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)

        #redmi
        #desired_caps['platformVersion'] = '5.0.2'
        #desired_caps['deviceName'] = 'LRX22G'
        #desired_caps['app'] = PATH('C:\\Users\\Redmi\\Desktop\\sfa6s.apk')

    def settings(self,connection='sandbox',ip='idcsfaqatemp.ebestmobile.net', port='443', title='Sales Rep', language='English'):
        self.connection = connection
        self.ip = ip
        self.port = port
        self.title = title
        self.language = language
        driver.find_element_by_xpath("//android.widget.Button[@index='1']").click()
        # driver.find_element_by_xpath("//input[@type='text' and @class='ng-untouched ng-pristine ng-valid']").clear()
        # driver.find_element_by_xpath("//input[@type='text' and @class='ng-untouched ng-pristine ng-valid']").send_keys(settings_info.ip)
        # driver.find_element_by_xpath("//input[@type='number' and @class='ng-untouched ng-pristine ng-valid']").clear()
        # driver.find_element_by_xpath("//input[@type='number' and @class='ng-untouched ng-pristine ng-valid']").send_keys(settings_info.port)
        # driver.find_element_by_xpath("//android.webkit.WebView/android.view.View/android.view.View/android.view.View[@index='1']/android.view.View/android.view.View/android.view.View[@index='0']/android.view.View/android.view.View/android.view.View[@index='2']/android.widget.Button").click()
        driver.find_element_by_xpath("//android.view.View[@index='2']/android.widget.Button[@index='0']").click()

    class Account(object):
        def __init__(self,username,password):
            self.username = username
            self.password = password

    account_info = Account(username='ts08@dev.com', password='Test$2017')
    def SFA_login(self,account_info):
        self.username = account_info.username
        self.password = account_info.password
        driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.EditText").clear()
        driver.find_element_by_xpath("//android.view.View[@index='0']/android.widget.EditText").send_keys(self.username)
        driver.find_element_by_xpath("//android.view.View[@index='1']/android.widget.EditText[@index='0']").clear()
        driver.find_element_by_xpath("//android.view.View[@index='1']/android.widget.EditText[@index='0']").send_keys(self.password)
        driver.find_element_by_accessibility_id("登录").click()

    #settings=Settings('标准','idcsfaqatemp.ebestmobile.net', '443', '销售代表', '中文')


    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    unittest.main()




