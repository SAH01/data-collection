import json
import random
from time import sleep

import requests
from fake_useragent import UserAgent

from report_data.into_mysql import insert_mysql
from report_data.ip_redis import my_redis

"""
post方法参数
params:字典或字节序列，作为参数增加到链接中
data:字典，字节序列或文件对象，作为请求的内容
json:JSON格式的数据，作为Request的内容
headers：字典，HTTP定制头（模拟浏览器进行访问）
cookies：字典或CpplieJar,Request中的cookie
auth:元祖，支持HTTP认证功能
files：字典类型，传输文件
timeout:设定超时时间，秒为单位
proxies:字典类型，设定访问代理服务器，可以增加登陆认证
allow_redirects:True//False，默认为True，重定向开关
stream:True/False,默认为True,获取内容立即下载开关
verify:True/False,默认为True，认证SSL证书开关
cert：本地SSL证书路径
"""
# 页码pageList
# 分类名称参数列表 nameList
#
def get_report(page,name,tableName):
    # ------------------------------ 修改页码
    for i in range(1,page):
        print("---------------------------------")
        ua = UserAgent()
        print("【随机 UserAgent：】" + ua.random)  # 随机产生headers
        temp_headers = ua.random
        # --------------------------------------
        test_redis = my_redis()
        temp_proxy = test_redis.get_ip()
        print("【随机 IP：】" + temp_proxy)
        url="https://www.nstrs.cn/rest/kjbg/wfKjbg/list"
        # url2 = "https://www.nstrs.cn/rest/kjbg/wfKjbg/list?pageNo=2&competentOrg=&jihuaId=&fieldCode=&classification=医药、卫生&kjbgRegion=&kjbgType=&grade="
        parms = {
            "pageNo": i,
            "competentOrg": "",
            "jihuaId": "",
            "fieldCode": "",
            "classification": name,   # 修改
            "kjbgRegion": "",
            "kjbgType": "",
            "grade": ""
        }

        other_parms={
                'User-Agent': temp_headers,
                'https': 'http://'+temp_proxy,
                'http': 'http://'+temp_proxy
            }
        sleeptime = random.uniform(0, 0.7)
        sleep(sleeptime)
        # print(url)
        response = requests.post(url, parms, other_parms)
        response.encoding='utf8'
        print(response.text+'\n')
        response_data = response.text   # 返回数据
        json_data = json.loads(response_data)   # 封装字典
        res_list_data = json_data['RESULT']['list']   # 一页 长度为10的list [{ },{ },{ } ... { }] len=10

        """
        重新构建一个 list [{ }]
        """
        for item in res_list_data:
            insert_mysql(item,name,tableName)
    return

if __name__ == '__main__':
    # 页码 pageList []
    pageList = [788,779,656,584,573,510,440,361,
                315,226,224,220,155,112,112,
                87,53,50,39,33,18,12,5,4,2,2,2,2]

    nameList = [
        "社会科学总论",
        "环境科学、安全科学",
        "建筑科学",
        "轻工业、手工业",
        "数理科学与化学",
        "能源与动力工程",
        "电工技术",
        "矿业工程",
        "经济",
        "文化、科学、教育、体育",
        "水利工程",
        "交通运输",
        "自然科学总论",
        "石油、天然气工业",
        "冶金工业",
        "武器工业",
        "航空、航天",
        "哲学、宗教",
        "原子能技术",
        "历史、地理",
        "政治、法律",
        "艺术",
        "语言、文字",
        "军事",
        "综合性图书",
        "文学",
        "语言、文学",
        "马克思主义、列宁主义、毛泽东思想、邓小平理论"
    ]

    tableList = ["tech_c","tech_x","tech_tu","tech_ts","tech_o","tech_tk","tech_tm",
                 "tech_td","tech_f","tech_g","tech_tv","tech_u",
                 "tech_n","tech_te","tech_tf","tech_tj","tech_v","tech_b","tech_tl",
                 "tech_k","tech_d","tech_j","tech_h","tech_e","tech_z","tech_i","tech_i","tech_a"]
    for i in range(0,len(tableList)):
        get_report(pageList[i],nameList[i],tableList[i])