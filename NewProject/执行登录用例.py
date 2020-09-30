'''
执行金融项目的登录功能
'''

import requests

proxy ={
    "http://192.168.150.222:8081",
    "https://192.168.150.222:8081"
}
requests.get("http://www.httpbin.org",proxies=proxy)

url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"regname":"test","pwd":"123456","mobilephone":"15619592320"}
m = requests.post(url,data=canshu)
print(m.text)