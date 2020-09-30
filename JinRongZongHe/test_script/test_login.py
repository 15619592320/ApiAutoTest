# 登陆逻辑
import pytest

from JinRongZongHe.baw.DbOp import DbOp
from JinRongZongHe.baw.member import Member
from JinRongZongHe.caw.Assert import Assert
from JinRongZongHe.caw.DataRead import DataRead


@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param

def test_login(login_data,url,register,base_requests):
    # 登录的测试逻辑
    print(f"执行登录的用例,测试数据为{login_data}")
    r = Member().login(url,base_requests,login_data['data'])
    # 断言
    Assert().equal(login_data['expect'], r.json(), "msg,status,code")