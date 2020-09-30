'''
fixture带参数
'''
import pytest
import requests
# 测试数据，可以从csv读取，也可以从xml读取，也可以从yaml文件中读取
data = [{"data":{"mobilephone":"18012345678","pwd":"123456"},"expect":{"msg":"手机号已被注册","code":"20110","status":"0"}},
        {"data":{"mobilephone":"15619592320","pwd":"123"},"expect":{"msg":"密码长度必须为6-18","code":"20108","status":"0"}}]

@pytest.fixture(params=data)
def register_data(request): # request 是fixture中的关键字
    return request.param   #通过request.param获取每一组测试数据

def test_register(register_data):
    print(register_data)
    ret = requests.post("http://192.168.150.52:8089/futureloan/mvc/api/member/register",register_data['data'])
    assert str(ret.json()['msg']) == register_data['expect']['msg']
    assert str(ret.json()['code']) == register_data['expect']['code']
    assert str(ret.json()['status']) == register_data['expect']['status']

def test_list():
    ret = requests.get("http://192.168.150.52:8089/futureloan/mvc/api/member/list")
    print(ret.text)