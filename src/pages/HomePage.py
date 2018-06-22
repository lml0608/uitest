# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base import BasePage
import time

from .guangao import GuanGao
class HomePage():



    #进入商城管理
    manager_button = (By.XPATH, "html/body/div[2]/div/ul/li[4]/a")


    seachguandao  = (By.LINK_TEXT,'搜索页公告')


    def __init__(self,driver):
        self.driver = driver
        print("home")


    def goto_uyingguanli(self):

        time.sleep(3)
        self.driver.find_element(*self.manager_button).click()

    def inrushhs(self):
        time.sleep(2)
        self.driver.find_element(*self.seachguandao).click()

        return GuanGao(self.driver)







