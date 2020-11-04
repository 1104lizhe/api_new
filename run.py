# _*_coding:utf-8_*_
import pytest, os, allure

if __name__ == "__main__":
    # os.system('cd C:\Users\ly\PycharmProjects\api_new_git')
    al = 'pytest C:\Users\ly\PycharmProjects\api_new_git\testcase\ --alluredir=C:\Program Files (x86)\Jenkins\workspace\new_api\allure-report --clean-alluredir'
    os.system(al)
    print(al)