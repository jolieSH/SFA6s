#coding=utf-8
import unittest

def createsuite():
    testunit=unittest.TestSuite()
    #定义测试查找的目录
    dir='D:\\SFA6s\\SFA6s'
    #定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(dir,pattern='*.py',top_level_dir=None)
    #discover筛选出的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

if __name__ ==  '__main__':
    runner=unittest.TextTestRunner()
    runner.run(testunit)

