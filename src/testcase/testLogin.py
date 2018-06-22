# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium import webdriver
import unittest
import time

from config import settings
from src.pages.LoginPage import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=settings.CHROMEDRIVER_FILE)

    def testlogin(self):

        self.driver.get("http://portaltest.wgmf.com/index.html")

        time.sleep(10)

        loginpage = LoginPage(self.driver)

        x = loginpage.loginAs('449','449')


        x.goto_uyingguanli()

        y = x.inrushhs()

        time.sleep(20)
        print(y)



    def tearDown(self):
        pass


if __name__ == '__main__':

    unittest.main(verbosity=2)
