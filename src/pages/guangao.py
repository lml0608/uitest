# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium.webdriver.common.by import By

class GuanGao(object):

    def __init__(self,driver):

        self.driver = driver


    #iframe_id
    switch_frame_loc = 'mallmanage_index'
    addbutton = (By.ID,'addBtn')
    vnoticeinput = (By.ID,'vnotice')
    noticeLinkinput = (By.NAME,'noticeLink')
    vstartTimeinput = (By.ID,'vstartTime')
    vendTimeinput = (By.ID,'vendTime')




    def jirnuiframe(self):

        self.driver.switch_to.frame(self.switch_frame_loc)


