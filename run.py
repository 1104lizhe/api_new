# _*_coding:utf-8_*_
import pytest, os, allure
import math

if __name__ == "__main__":
    # os.system('cd C:\Users\ly\PycharmProjects\api_new_git')
    # al = r'pytest C:/Program Files (x86)/Jenkins/workspace/new_api/testcase/ --alluredir C:/Program Files (x86)/Jenkins/workspace/new_api/allure-report --clean-alluredir'
    pt = r'pytest C:\Users\ly\PycharmProjects\api_new_git\testcase\ --alluredir report --clean-alluredir'
    os.system(pt)