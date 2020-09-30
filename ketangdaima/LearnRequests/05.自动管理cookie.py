'''
自动管理cookies
'''

import requests

# 新建一个session
s=requests.Session()
print(s.cookies) #RequestsCookieJar
print(requests.utils.dict_from_cookiejar(s.cookies)) #CookieJar转字典

# 访问百格首页
r = s.get("https://www.bagevent.com")
print("访问首页后，打印Cookie，Cookie有2条")
print(s.cookies) #RequestsCookieJar
print(requests.utils.dict_from_cookiejar(s.cookies)) #CookieJar转字典

param={
    "access_type":	1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"2780487875@qq.com",
    "password":"qq2780487875",
    "remindmeBox":	"on",
    "remindme":1,
}
r = s.post("https://www.bagevent.com/user/login",data=param)
print("登录之后，打印Cookie,Cookie有5条")
print(s.cookies) #RequestsCookieJar
print(requests.utils.dict_from_cookiejar(s.cookies)) #CookieJar转字典

r = s.get("https://www.bagevent.com/vlist/common/surveyList")
print(r.json())
print(r.json()["list"][0]["survey_id"])