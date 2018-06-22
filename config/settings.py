# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHROMEDRIVER_FILE = os.path.join(BASE_DIR, "bin", 'chromedriver.exe')

GECKODRIVER_FILE = os.path.join(BASE_DIR, "tools", 'geckodriver.exe')
