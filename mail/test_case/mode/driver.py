#coding:utf-8
#@time     :     2017/9/29 20:40
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : driver.py
# @Software: PyCharm Community Edition


from selenium.webdriver import Remote
from selenium import webdriver
 #启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    '''
      #可以启动到远程主机中，运行自动化测试
      host = '127.0.0.1:4444' #运行主机：端口号（本机默认：127.0.0.1:4444）
      dc = {'browserName': 'chrome'}  #指定浏览器
     driver = Remote(command_execute='http://' + host + '/wd/hub',
                     desired_capabilities=dc)
    '''
    return driver
    '''
 #用于测试该脚本是否有效
 if __name__ == '__main__':
     dr = browser()
    '''