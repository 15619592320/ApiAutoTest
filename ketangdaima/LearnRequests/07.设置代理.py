'''
1.爬虫之类的场景，避免服务器认为是攻击，将IP屏蔽掉
2.代理抓包，定位问题
'''

import requests
# 打开fiddler
proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}

requests.get("http://www.httpbin.org",proxies=proxy)
# requests.put() 更新
# requests.delete()