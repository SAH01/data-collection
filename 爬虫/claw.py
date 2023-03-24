import requests
from bs4 import BeautifulSoup
import xlwt

def get_data():
    # 链接
    url='https://tjj.xinjiang.gov.cn/tjj/nyxfsnc/202203/2a405a2cf0334d8a9dcb3e25a4791f90.shtml'
    # 伪装请求头
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'
    }
    # 发起请求
    response = requests.get(url, headers)
    # 指定编码格式
    response.encoding = 'UTF-8'
    # 获取所有标签
    page_text = response.text
    # print(page_text)
    # soup解析
    soup = BeautifulSoup(page_text, 'lxml')
    # 获取页面所有的tr
    tr_all = soup.find_all('tr')
    # 获取 从【消费总量】到【生活消费】 的所有列
    tr_all_new = tr_all[4:-1]
    # 遍历 tr_all_new
    temp_res = []   # 暂时存储每一行数据['','','' ... ]
    res = []        # 最终存储的数据
    my_workbook = xlwt.Workbook()   # 打开一个工作薄
    sht1 = my_workbook.add_sheet('sheet1')  # 新建一个sheet
    # 遍历tr，获取所有td
    for item in tr_all_new:
        temp_item = str(item)  # 转字符串类型，不然会报错
        temp_soup = BeautifulSoup(temp_item,'lxml') # 解析
        td_all = temp_soup.find_all('td')   # 获取每一个tr里的所有td
        # 遍历每一个tr里的td
        for td_item in td_all:
            td_item = str(td_item)  # 转字符串类型，不然会报错
            temp_soup_td = BeautifulSoup(td_item,'lxml')
            # 获取td标签的文本值
            temp_res.append(temp_soup_td.find('td').text)
        res.append(temp_res)    # 把每一次遍历后的那一行数值暂存进temp_res
        temp_res = []  # 把暂存列表置为空，暂存列表始终只存一行数据
    for i in range(len(res)):
        # write([行],[列],[值])
        sht1.write(i,0,res[i][0])
        sht1.write(i,1,res[i][1])
        sht1.write(i,2,res[i][2])
        sht1.write(i,3,res[i][3])
        sht1.write(i,4,res[i][4])
        sht1.write(i,5,res[i][5])
        sht1.write(i,6,res[i][6])
        sht1.write(i,7,res[i][7])
        sht1.write(i,8,res[i][8])
        sht1.write(i,9,res[i][9])
        sht1.write(i,10,res[i][10])
    # 保存
    my_workbook.save('分行业能源消费总量和主要能源消费量.xls')
if __name__ == '__main__':
    get_data()