# _*_coding:utf-8_*_
import pytest, os, allure

if __name__ == "__main__":
    # os.system('cd C:\Users\ly\PycharmProjects\api_new_git')
    pt = 'pytest testcase --alluredir ./report --clean-alluredir'
    al = 'allure generate report/  --clean'
    os.system(pt)
    os.system(al)
    print(al)