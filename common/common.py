from configparser import ConfigParser
from hashlib import md5
import random
import xlrd
import os
import json_tools
import json

parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def read_data(filename, sheetname):
    '''
    读Excel数据
    :param filename:
    :param sheetname:
    :return: [{},[},{}]
    '''
    data = xlrd.open_workbook(parent_dir + '/data/' +filename)
    p0 = []
    p1 = []
    table = data.sheet_by_name(sheetname)
    hs = table.nrows
    for row in range(1, hs):
        one_row = table.row_values(0)
        row_data = table.row_values(row)
        new_list = [i for i in row_data if i != 'null']
        index_list = []
        one_list = []
        for i in range(len(row_data)):
            if row_data[i] == 'null':
                index_list.append(i)
        for i in index_list:
            one_list.append(one_row[i])
        for i in one_list:
            one_row.remove(i)
        for i in range(len(new_list)):
            if isinstance(new_list[i],int) or isinstance(new_list[i],float):
                if new_list[i]%1 == 0.0:
                    new_list[i] = int(new_list[i])
        asd = dict(zip(one_row, new_list))
        if asd['用例级别'] == 'p0':
            p0.append(asd)
        elif asd['用例级别'] == 'p1':
            p1.append(asd)
    return p0,p1

def get_nonce_str():
    '''
    :return: 6位随机字符串
    '''
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.sample(chars, 6))


def sign_action(key, parameters):
    '''
    :return: 生成签名
    '''
    sortedParameters = sorted(
        parameters.items(), key=lambda parameters: parameters[0])
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        if v or v == 0:
            canonicalizedQueryString += '&' + str(k).strip() + '=' + str(v).strip()
    tempstring = canonicalizedQueryString[1:] + '&' + 'company_secret=' + str(key)
    signature = md5(tempstring.strip().encode()).hexdigest().upper()
    return signature

def json_data(a, b):
    '''
    比较json串
    :param a:接口返回的json
    :param b: Excel读出的json
    :return: 两个json串的差异，返回结果相比较期望结果的差异
    '''
    a = eval(a)
    result = json_tools.diff(a, b)
    result_replace = []
    result_remove = []
    result_add = []
    for i in result:
        if 'replace' in i.keys():
            result_replace.append(i)
        elif 'remove' in i.keys():
            result_remove.append(i)
        elif 'add' in i.keys():
            result_add.append(i)
    return result, result_replace, result_remove, result_add, a


if __name__ == "__main__":
    p0,p1 = read_data('department.xlsx', 'update')
    print(p0)
    print(p1)

