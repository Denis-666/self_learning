import requests
import headers_txt
import json

headers = headers_txt.headers


url = 'https://theunderminejournal.com/#us/illidan/category/herbalism'

param = {

}

response = requests.get(url = url, headers = headers)

list_data = response.text

fp = open('./tumj.html','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print('done!!!!!')



# 这方法不行，可能网页更新了，，，，

 