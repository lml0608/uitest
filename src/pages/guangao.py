# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
class GuanGao(object):

    def __init__(self,driver):

        self.driver = driver


    #iframe_id
    switch_frame_loc = 'mallmanage_index'
    addbutton = (By.ID,'addBtn')
    vnoticeinput = (By.ID,'vnotice')
    imginput = (By.XPATH,'//span[@id="up_load1"]/i')

    noticeLinkinput = (By.NAME,'noticeLink')
    vstartTimeinput = (By.ID,'vstartTime')
    vendTimeinput = (By.ID,'vendTime')




    def jirnuiframe(self):

        self.driver.switch_to.frame(self.switch_frame_loc)

        time.sleep(2)
        self.driver.find_element(*self.addbutton).click()

        time.sleep(2)

        self.driver.find_element(*self.vnoticeinput).send_keys("测试")
        time.sleep(2)

        self.driver.find_element(*self.imginput).click()

        time.sleep(10)

        os.system("D:\\django_project\\uitest\\tools\\senpng99.exe")

        time.sleep(5)







