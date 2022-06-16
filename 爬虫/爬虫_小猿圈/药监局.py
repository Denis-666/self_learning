import requests
import json
import headers_txt
import pymysql

headers = headers_txt.headers

id_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalaction.do?method=getXkzsList'

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', database='python_data')
cur = conn.cursor()
# f = open('datain.txt','w',encoding='utf-8')
for i in range(5):
    id_data = {
        'on': 'true',
        'page': 'i + 1',  # 第i+1页
        'pageSize': '15',  # 每页15条信息
        'productName': ' ',
        'conditionType': '1',
        'applyname': ' ',
        'applysn': ' ',
    }
    response = requests.post(url=id_url, data=id_data, headers=headers)
    content_dic = response.json()
    # # 得到一个包含第i+1页所有企业id和企业名字的字典
    for dic in content_dic['list']:
        eps_id = dic['ID']
        data_id = {'id': eps_id}
        # 这样得到了每个企业的id
        # 可以将每个企业的id作为参数来爬取企业信息
        eps_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        eps_dic = requests.post(url=eps_url, data=data_id, headers=headers).json()
        # 得到相应企业信息的一个字典
        # f.write('名字:' + eps_dic['epsName'] + '      地址:' + eps_dic["epsAddress"] + '\n')
        sql = 'insert into yaojianju value (%s,%s)'
        cur.execute(sql, (eps_dic['epsName'], eps_dic["epsAddress"]))
        conn.commit()
print('写入完成')
# f.close()
conn.close()

