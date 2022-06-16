import headers_txt
import requests
import json

headers_txt_0 = headers_txt.headers_0




post_url = 'https://fanyi.baidu.com/sug'
word = input('enter a word : ')
data_0 = {
    'kw': word
}

#  发请求
response = requests.post(url = post_url,data = data_0,headers = headers_txt_0)

# 获取 响应 数据 .json()  方法返回时obj （ 如果确认响应数据时json类型，才可以使用.json() ）
'''
在抓包 响应头 里面 
Content-Type : application/json
中查看
 '''
dic_obj = response.json()


# 进行持久化 存储
fileName = word + '.json'
fp = open(fileName,'w',encoding = 'utf-8')
json.dump(dic_obj, fp=fp,ensure_ascii = False) # 中文不能给ascii码 编码 ，所以必须False

print('is done!!!')





