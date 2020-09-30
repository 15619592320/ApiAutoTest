'''
业务AW：按模块划分
business action word
'''


REGISTER = "futureloan/mvc/api/member/register"

class Member:
    def register(self,url,base_requests,data):
        '''
        用户注册的接口
        :param url:
        :param base_requests:
        :param data:
        :return:
        '''
        real_url = url + REGISTER
        r = base_requests.post(real_url,data=data)
        return r

    def login(self,url,base_requests,data):
        real_url = url + REGISTER
        r = base_requests.post(real_url, data=data)
        return r

if __name__ == '__main__':
    from JinRongZongHe.caw.BaseRequests import BaseRequests
    r = Member().register("http://192.168.150.222:8081/",BaseRequests(),{"mobilephone":"145345"})
    print(r.text)