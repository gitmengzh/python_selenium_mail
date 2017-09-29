#coding:utf-8
#@time     :     2017/9/29 20:42
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : mail_page.py
# @Software: PyCharm Community Edition



from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

class MailPage(Base):
    url = '/'
    login_success_user_loc = (By.ID, 'spnUid')

    def login_success_user(self):
        return self.find_element(*self.login_success_user_loc).text

