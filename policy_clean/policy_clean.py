# line-height:29px
# text-indent:32px
# font-size:16px;font-family:宋体
# '[\u4e00-\u9fa5]+'多个中文字符
# \d+ 多个数字
# 读取原来数据 进行清理匹配
import re

import pymysql


def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                    user="root",
                    password="reliable",
                    db="febs",
                    charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):
    """
    通用封装查询
    :param sql:
    :param args:
    :return:返回查询结果 （（），（））
    """
    conn , cursor= get_conn()
    print(sql)
    cursor.execute(sql)
    res = cursor.fetchall()
    close_conn(conn , cursor)
    return res

def clean_text():
    regex_0 = re.compile("line-height:" + '[ ]*(\d+)' + "px")  # 修改行间距为 29px
    regex_1 = re.compile("text-indent:" + '[ ]*(\d+)' + "px")  # 修改首行缩进为 32px
    regex_2 = re.compile("font-size:" + '[ ]*(\d+)' + "px")  # 修改字体大小为 16px
    regex_3 = re.compile("font-family:[ ]*"+"微软雅黑")  # 修改微软雅黑字体为 宋体
    sql_0 = "select `name`,`text` from policy_enter ;"       # sql_0 查询原始数据

    conn,cursor = get_conn()
    res=query(sql_0)
    print(len(res))
    # print(res[0])
    count=0
    for item in res:
        name = item[0]
        content = item[1]
        # print("修改前的内容为："+content)
        # print("修改行间距为 29px")
        new_content_0 = re.sub(regex_0, 'line-height:29px', content)
        # print("修改首行缩进为 32px")
        new_content_1 = re.sub(regex_1, 'text-indent:32px', new_content_0)
        # print("修改字体大小为 16px")
        new_content_2 = re.sub(regex_2, 'font-size:16px', new_content_1)
        # print("修改字体为 宋体")
        new_content_3 = re.sub(regex_3, 'font-family:宋体', new_content_2)
        new_content_3 = new_content_3.replace("仿宋_GB2312","宋体")
        new_content_3 = new_content_3.replace("方正仿宋_GBK","宋体")
        # print("修改后的内容为："+new_content_3)
        print("入新表：")
        sql_1 = "insert into policy_clean (`name`,`content`) values (%s,%s) " # 入新表
        try:
            cursor.execute(sql_1,[name,new_content_3])  # 执行sql语句
            conn.commit()  # 提交事务
        except:
            print(name+ " 报错！")
        count=count+1
        print(str(count))
        new_content_0=""
        new_content_1=""
        new_content_2=""
        new_content_3=""

        print("----------------------------------------")

    close_conn(conn,cursor)

    return
def into_table():
    conn,cursor = get_conn()
    count = 0
    sql_get = "select * from policy_clean "
    all_data = query(sql_get)
    print(len(all_data))
    for item in all_data:
        item_name = item[0]
        item_text = item[1]
        sql_put = "update policy_enter set `text` = %s " \
                   "where `name` = %s "
        cursor.execute(sql_put,[item_text,item_name])  # 执行sql语句
        conn.commit()  # 提交事务
        count=count+1
        print(str(count))

if __name__ == '__main__':
    # clean_text()
    into_table()