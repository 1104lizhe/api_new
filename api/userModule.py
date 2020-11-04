import json
import requests
from common.common import sign_action,get_nonce_str

class User(object):
    def select(self, params,url,company_key,c_secret):
        data = {}
        for i in params:
            if i != '':
                data[i] = params[i]
        api = '/api/v1/user'
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.get(url=url + api, params=data)
        a = r.json()
        return r, a, data

    def add(self,params,url,company_key,c_secret):
        data = {}
        for i in params:
            if i != '':
                data[i] = params[i]
        api = '/api/v1/add/user'
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.post(url=url + api, data=data)
        a = r.json()
        return r, a, data

    def update(self,params,url,company_key,c_secret):
        targets = {}
        data = {}
        l = []
        api = '/api/v2/user/edit'
        for i in params:
            if i != '':
                targets[i] = params[i]
        if len(targets) != 0:
            l.append(targets)
            data['targets'] = json.dumps(l)
        data['company_key'] = company_key
        company_secret = c_secret
        data['nonce_str'] = get_nonce_str()
        data['sign'] = sign_action(company_secret, data)
        r = requests.post(url=url + api, data=data)
        a = r.json()
        return r, a, data
