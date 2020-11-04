import json
import requests
from common.common import sign_action,get_nonce_str

class Department(object):
    def select(self, params,url,company_key,c_secret):
        data = {}
        for i in params:
            if i != '':
                data[i] = params[i]
        api = '/api/v1/department'
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.get(url=url + api, params=data)
        a = r.json()
        return r, a, data

    def add(self,params, hope, url, company_key, c_secret):
        data = {}
        aa = eval(hope)['code']
        for i in params:
            if i != '':
                if i == 'name' and aa == 0:
                    data[i] = params[i] + get_nonce_str()
                else:
                    data[i] = params[i]
        api = '/api/v1/department/add'
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.post(url=url + api, data=data)
        a = r.json()
        return r, a, data

    def update(self,params, hope ,url,company_key,c_secret):
        data = {}
        aa = eval(hope)['code']
        for i in params:
            if i != '':
                if i == 'name' and aa == 0:
                    data[i] = params[i] + get_nonce_str()
                else:
                    data[i] = params[i]
        api = '/api/v1/department/edit'
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.post(url=url + api, data=data)
        a = r.json()
        return r, a, data