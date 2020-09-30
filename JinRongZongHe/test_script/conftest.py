'''
脚本层的公共方法
'''
import pytest

# 读取环境文件,获取url
from JinRongZongHe.baw.DbOp import DbOp
from JinRongZongHe.baw.member import Member
from JinRongZongHe.caw.Assert import Assert
from JinRongZongHe.caw.DataRead import DataRead
from JinRongZongHe.caw.BaseRequests import BaseRequests

ENVPATH = r'data_env\env.ini'

# 读取环境文件,获取url
@pytest.fixture(scope='session')
def url():
    return DataRead().read_ini(ENVPATH,'url')

# 读取环境文件,获取db
@pytest.fixture(scope='session')
def db():
    return eval(DataRead().read_ini(ENVPATH,'db'))

# BaseRequests实例化,整个执行过程实例化一次
@pytest.fixture(scope='session')
def base_requests():
    return BaseRequests()

@pytest.fixture(scope='session',params=DataRead().read_yaml(r"data_case\login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture(scope='session')
def register(url, base_requests, setup_data,db):
    #注册用户
    r = Member().register(url, base_requests,setup_data['data'])
    Assert().equal(setup_data['expect'], r.json(), "msg,status,code")
    yield
    #删除注册用户
    DbOp().delete_user(db, setup_data['data']['mobilephone'])