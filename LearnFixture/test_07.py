# '''
# fixture嵌套
# '''
#
# import pytest
# # import faker
#
# # f = faker.Faker()
#
# @pytest.fixture()
# def username():
#     return f.username()  #生成随机的用户名
#
# @pytest.fixture()
# def pwd():
#     return f.password()  #生成随机密码
#
# @pytest.fixture()
# def get_user_pwd(username,pwd):
#     return {"username":username,"pwd":pwd}
#
# def test_login(get_user_pwd):
#     print(f"测试登录功能，登陆的用户名:{get_user_pwd["username"]},密码为:{get_user_pwd['pwd']}")