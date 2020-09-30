'''
发送post请求
1.使用data传参
2.使用json传参
'''

import requests
url = "http://www.httpbin.org/post"
canshu = {"username":"root","password":"123456"}
r = requests.post(url,data = canshu) #使用data传参“Content-Type”：“application/x-www-form-urlencoded”,
print(r.text)

r = requests.post(url,json=canshu) #使用json传参“Content-Type”：“application/json“，
print(r.text)
# post接口具体用data传参，还是用json传参，时后台实现决定的

# 金融项目的登录接口，post
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/login"
canshu = {"regname":"test","pwd":"123456","mobilephone":"15619592320"}
r = requests.post(url,data = canshu)
print(r.text)

# url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register"
# canshu = {"mobilephone":"15619592320","pwd":"123456","regname":"test"}
# r = requests.get(url,params=canshu)
# print(r.text)