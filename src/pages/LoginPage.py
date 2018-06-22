# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.HomePage import HomePage
import time
from config import settings

#http://portaltest.wgmf.com/index.html
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        #self.driver = webdriver.Chrome(executable_path=settings.CHROMEDRIVER_FILE)

    lintonLocator = (By.ID, 'loginShow')
    staffLocator = (By.ID, 'staff_id')
    passwordLocator = (By.ID, 'password')
    submittedLocator = (By.CLASS_NAME, 'sub')


    def clickLoginButton(self):

        self.driver.find_element(*self.lintonLocator).click()


    def typeStaff(self,staff_id):

        self.driver.find_element(*self.staffLocator).send_keys(staff_id)


    def typePassword(self, password):
        self.driver.find_element(*self.passwordLocator).send_keys(password)


    def submitLogin(self):

        self.driver.find_element(*self.submittedLocator).submit()

        return HomePage(self.driver)

    def submitLoginExpectingFailure(self):

        self.driver.find_element(*self.submittedLocator).submit()

        return LoginPage(self.driver)



    def loginAs(self,staff_id, password):

        self.clickLoginButton()
        self.typeStaff(staff_id)
        self.typePassword(password)

        return self.submitLogin()

