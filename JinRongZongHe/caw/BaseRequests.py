'''
新建一个session，自动管理cookie
'''

import requests

class BaseRequests():

    def __init__(self):
        '''
        初始化的时候新建一条session，并保存在session这个属性中
        '''
        self.session = requests.Session()

    def post(self,url,data=None,json=None,**kwargs):
        '''
        重写requests中的post方法，确保使用session发送post请求
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        '''
        try:
            r =self.session.post(url,data=data,json=json,**kwargs)
            print(f"发送post请求:{url},{data},{json},{kwargs}")
            return r
        except Exception as e:
            print(f"发送post请求:{url},{data},{json},{kwargs},异常{e}")

    def get(self,url,**kwargs):
        '''
        重写get

        :param param:
        :param json:
        :param kwargs:
        :return:
        '''
        try:
            r = self.session.get(url,**kwargs)
            print(f"发送get请求：{url},{kwargs}")
            return r
        except Exception as e:
            print(f"发送get请求：{url},{kwargs},异常{e}")



if __name__ == '__main__':
    r = BaseRequests().post("http://www.httpbin.org/post",data={"user":"root"})
    print(r.text)
    r = BaseRequests().get("http://www.httpbin.org/get", params={"user": "root"})
    print(r.text)