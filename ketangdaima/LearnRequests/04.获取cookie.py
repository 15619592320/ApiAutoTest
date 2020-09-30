'''
获取cookie：服务的响应中如果有set-cookie，可以通过r。cookies获取
'''

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get("http://www.baidu.com",headers=headers)
c = r.cookies
print(type(c)) #<class 'requests.cookies.RequestsCookieJar'>
# RequestsCookieJar转成字典
cookies_dict = requests.utils.dict_from_cookiejar(c)
# 遍历字典
for key,value in cookies_dict.items():
    print(key,value)

# 发送百度搜索的请求，将上一步百度首页获取到的cookies带上
# wd=requests,这个是搜索的内容
# r = requests.get("http://www.baidu.com/s?wd=requests",headers=headers,cookies=cookies_dict)
# print("Requests - 简书" in r.text)
# assert "Requests - 简书" in r.text
#
r = requests.get("http://www.baidu.com/s?wd=协议",cookies=cookies_dict)
print("股东协议合同_协议范本" in r.text)
assert "股东协议合同_协议范本" in r.text