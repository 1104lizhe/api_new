import pytest
import allure
from api.userModule import User
from common.common import *
from configparser import ConfigParser
from common.common import parent_dir

class TestUserP0(User):
    test_data_select_p0, test_data_select_p1 = read_data('user.xlsx', 'select')
    test_data_add_p0, test_data_add_p1 = read_data('user.xlsx', 'add')
    test_data_update_p0, test_data_update_p1 = read_data('user.xlsx', 'update')
    def setup_class(self):
        cfg = ConfigParser()
        cfg.read(parent_dir + '/config/config.ini')
        self.url = cfg.get('124', 'url')
        self.company_key = cfg.get('124', 'company_key')
        self.c_secret = cfg.get('124', 'c_secret')

    # @pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
    @pytest.mark.last
    @pytest.mark.parametrize('params', test_data_select_p0)
    def test_user_select(self, params):
        hope = params.pop('预期结果')
        level = params.pop('用例级别')
        user = User()
        r, a, data = user.select(params,self.url,self.company_key,self.c_secret)
        result, result_replace, result_remove, result_add, eval_a = json_data(hope, a)
        allure.attach("{0}".format(data), "参数")
        allure.attach("{0}".format(a), "返回")
        allure.attach("{0}".format(hope), "期望")
        allure.attach("{0}".format(result), "json")
        assert r.status_code == 200
        if a['code'] != 0:
            assert result_replace == []
        assert result_remove == []
        assert result_add == []

    # @pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('params', test_data_add_p0)
    def test_user_add(self, params):
        hope = params.pop('预期结果')
        level = params.pop('用例级别')
        user = User()
        r, a, data = user.add(params,self.url,self.company_key,self.c_secret)
        result, result_replace, result_remove, result_add, eval_a = json_data(hope, a)
        allure.attach("{0}".format(data), "参数")
        allure.attach("{0}".format(a), "返回")
        allure.attach("{0}".format(hope), "期望")
        allure.attach("{0}".format(result), "json")
        assert r.status_code == 200
        assert result_remove == []
        assert result_add == []
        assert a['code'] == eval_a['code']

    # @pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('params', test_data_update_p0)
    def test_user_update(self, params):
        hope = params.pop('预期结果')
        level = params.pop('用例级别')
        user = User()
        r, a, data = user.update(params, self.url, self.company_key, self.c_secret)
        result, result_replace, result_remove, result_add, eval_a = json_data(hope, a)
        allure.attach("{0}".format(data), "参数")
        allure.attach("{0}".format(a), "返回")
        allure.attach("{0}".format(hope), "期望")
        allure.attach("{0}".format(result), "json")
        assert r.status_code == 200
        assert result_replace == []
        assert result_remove == []
        assert result_add == []


if __name__ == "__main__":
    pytest.main()






