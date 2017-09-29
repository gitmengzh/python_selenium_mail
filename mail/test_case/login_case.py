#coding:utf-8
#@time     :     2017/9/29 20:42
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : login_case.py
# @Software: PyCharm Community Edition



from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_user_pwd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('','')
        sleep(2)
        self.assertEqual(po.login_error_hint(),'请输入帐号')
        function.insert_img(self.driver, 'user_pwd_null.jpg')

    def test_login_pwd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action('abc','')
        sleep(2)
        self.assertEqual(po.login_error_hint(),'请输入密码')
        function.insert_img(self.driver, 'pwd_null.jpg')

    def test_login_user_pwd_error(self):
        '''用户名或密码错误'''
        po = LoginPage(self.driver)
        po.open()
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "test" + character
        po.login_action(username,"$#%#")
        sleep(2)
        #print(po.login_error_hint())
        self.assertEqual(po.login_error_hint(),'帐号或密码错误')
        function.insert_img(self.driver, "user_pwd_error.jpg")

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        po = LoginPage(self.driver)
        po.open()
        user = "ldq791918813"
        po.login_action(user,"xiuxiu060801zhu")
        sleep(2)
        po2 = MailPage(self.driver)
        #print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(),user+"@163.com")
        function.insert_img(self.driver, "success.jpg")

login_case.py