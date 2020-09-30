'''
注册接口的脚本
'''

# pytest fixture 参数化的功能
# 参数都进来
import  pytest

from JinRongZongHe.baw.member import Member
from JinRongZongHe.caw.Assert import Assert

from JinRongZongHe.caw.DataRead import DataRead
from JinRongZongHe.baw.DbOp import DbOp

# list 多组测试数据
from JinRongZongHe.test_script.conftest import url, base_requests
@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param
@pytest.fixture(params=DataRead().read_yaml(r"data_case\zhuce_success.yaml"))
def success_data(request):
    return request.param
@pytest.fixture(params=DataRead().read_yaml(r"data_case\denglu_failed.yaml"))
def login_fail_data(request):
    return request.param
@pytest.fixture(params=DataRead().read_yaml(r"data_case\denglu_success.yaml"))
def login_success_data(request):
    return request.param

# 注册失败的逻辑
def test_register_fail(fail_data,url,base_requests):
    print(f"执行注册失败的用例,测试数据为{fail_data}")
    #conftest.py
    r = Member().register(url,base_requests,fail_data['data'])
    # print(r.text)
    # assert str(fail_data['expect']['msg'] == r.json()['msg'])
    # assert str(fail_data['expect']['status'] == r.json()['status'])
    # assert str(fail_data['expect']['code'] == r.json()['code'])
    Assert().equal(fail_data['expect'], r.json(), "msg,status,code")

# 注册成功的逻辑
def test_register_success(success_data,url,db,base_requests):
    print(f"执行注册成功的用例,测试数据为{success_data}")
    # 环境初始化
    DbOp().delete_user(db,success_data['data']['mobilephone'])
    r = Member().register(url,base_requests,success_data['data'])
    # print(r.text)
    # assert str(success_data['expect']['msg'] == r.json()['msg'])
    # assert str(success_data['expect']['status'] == r.json()['status'])
    # assert str(success_data['expect']['code'] == r.json()['code'])
    Assert().equal(success_data['expect'], r.json(), "msg,status,code")
    # 清理环境
    DbOp().delete_user(db,success_data['data']['mobilephone'])

# 重复注册的逻辑
def test_register_repeat():
    pass



