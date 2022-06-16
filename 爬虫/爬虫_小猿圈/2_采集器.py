# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
}

url = 'https://www.sogou.com/web'

kw = input('enter a word:')
param = {
    'query':kw
}

response = requests.get(url=url,params = param,headers = headers)

page_text = response.text
fileName = kw+'.html'
with open(fileName,'w',encoding='utf-8')as fp:
    fp.write(page_text)
print(fileName,'保存成功！！！！')



# UA 伪装:

# ua: User-Agent (请求载体的身份标识)
# ua伪装: 门户网站的服务器会坚持对应请求的 载体身份标识
    #   如果检测到 请求载体为某一款浏览器
    #  说明 这是一个正常的请求
    #  如果不正常 就 判定为 爬虫，服务器端就会拒绝请求
    
    
'''User-Agent
	Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'''

    
    




