# -*- coding:utf-8 -*-
'''
__author__:liubin

'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




class BasePage(object):


    def __init__(self,driver):

        self.driver = webdriver.Chrome()

    def open(self,url,t='',timeout=10):

        '''

        :param url: 打开的URL
        :param t: 标题title
        :param timeout: 等待时间
        :return: None
        '''
        #打开浏览器
        self.driver.get(url)
        #窗口最大化
        self.driver.maximize_window()

        try:

            WebDriverWait(self.driver,timeout,1).until(EC.title_is(t))

        except TimeoutException:

            print("open %s title error" % url)

        except Exception as msg:

            print("Error:%s" % msg)


    def find_element(self,locator,timeout=10):
        """
        定位单个元素
        :param locator: 
        :param timeout: 
        :return: 
        """


        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))

        return element


    def find_elements(self,locator,timeout=10):
        """
        定位一组元素
        :param locator: 
        :param timeout: 
        :return: 
        """
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))

        return elements

    def switch_frame(self, loc):
        """
        进入iframe
        :param loc: 
        :return: 
        """
        return self.driver.switch_to.frame(loc)

    def switch_to_default(self, loc):
        """
        跳出iframe
        :param loc: 
        :return: 
        """
        return self.driver.switch_to.default_content(loc)

    def click(self,locator):
        """
        点击click
        :param locator: 
        :return: 
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self,locator,text):

        '''发送文本，清空后输入'''

        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout=10):
        '''
        p判断文本在元素里
        :param locator:
        :param text:
        :param timeout:
        :return:
        '''
        try:

            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))

        except TimeoutException:
            print("元素美定位到："+str(locator))

            return False

        else:
            return result


    def is_title(self,title,timeout=10):

        '''判断title完全等于'''


        result = WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))

        return result


    def is_title_contains(self,title,timeout=10):

        '''判断title包含'''

        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))

        return result


    def is_selected(self,locator,timeout=10):
        '''判断元素被选中'''

        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))

        return result

    def is_selected_be(self,locator,selected=True,timeout=10):


        '''判断元素的状态，selected市期望的参数'''
        #返回布尔值

        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))

        return result

    def is_alert_present(self,timeout=10):

        '''判断页面是否有alert'''
        '''
        返回alert不是true
        没有就返回false
        '''

        result = WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())

        return result

    def is_visible(self,locator,timeout=10):

        '''元素可见返回本身，不可见返回False'''

        result = WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))

        return result

    def is_clickable(self,locator,timeout=10):
        '''元素可点击返回元素本身，不可点击返回False'''

        result = WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))

        return result


    def is_located(self,locator,timeout=10):
        '''

        :param locator:
        :param timeout:
        :return:  元素定位到返回元素，美定位到返回False
        '''

        result = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))

        return result


    def move_to_element(self,locator):

        '''鼠标悬停操作'''
        element = self.find_element(locator)

        ActionChains(self.driver).move_to_element(element).perform()



    def back(self):
        '''返回'''

        self.driver.back()

    def forward(self):

        self.driver.forward()


    def close(self):

        self.driver.close()

    def quit(self):

        self.driver.quit()


    def get_title(self):

        '''获取title'''

        return self.driver.title

    def get_text(self,locator):

        '''获取文本'''

        element = self.find_element(locator)

        return element.text

    def get_attribute(self,locator,name):
        '''获取属性'''


        element = self.find_element(locator)

        return element.get_attribute(name)


    def js_execute(self,js):

        '''执行js'''
        return self.driver.execute_script(js)


    def  js_focus_element(self,locator):
        '''聚焦元素'''

        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)


    def js_scroll_top(self):
        '''滚动到顶部'''

        js = "window.scrollTo(0,0)"

        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''

        js = "window.scrollTo(0,document.body.scrollHeight)"

        self.driver.execute_script(js)


    def select_by_index(self,localtor,index):

        '''通过索引，index市索引第几个，从0开始'''

        element = self.find_element(localtor)

        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):

        '''通过value属性'''

        element = self.find_element(locator)
        Select(element).select_by_value(value)


    def select_by_text(self,locator,text):

        ''''通过文本值定位'''
        element = self.find_element(locator)

        Select(element).select_by_value(text)



# if __name__ == '__main__':
#
#     driver = browser()
#
#     driver_n = Liubin(driver)
#
#     driver_n.open("http://www.baidu.com",t='百度一下，你就知道')
#
#     print(driver_n.get_title())
#
#     #driver_n.quit()
#
#
#     input_loc = ("id","kw")
#
#     button_loc = ("id", "su")
#
#     set_loc = ("link text", "设置")
#
#
#     driver_n.send_keys(input_loc,"selenium")
#
#     driver_n.click(button_loc)
#
#     driver_n.move_to_element(set_loc)






