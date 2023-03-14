# 完全复刻源文件格式 GB/T4754—2017
import pymysql
import pandas as pd
def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                    user="root",
                    password="reliable",
                    db="data_cleaning",
                    charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor
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
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def reprint() :
    conn, cursor = get_conn()  # 连接数据库data_cleaning
    df = pd.read_excel('GBT4754-2017.xlsx')  # 读取标准表
    print(len(df.index))
    v_rate_type = '01'
    v_rate_time = '2023'
    code_1 = ''
    name_1 = ''
    code_2 = ''
    name_2 = ''
    code_3 = ''
    name_3 = ''
    code_4 = ''
    name_4 = ''
    # 共11个字段需要插入，主键ID自增+两个固定字段+8个分类细节
    SQL_NEW = 'insert into national_industrial_code (' \
              'id,' \
              'rate_type,' \
              'rate_time,' \
              'category_code,' \
              'category_name,' \
              'large_code,' \
              'large_name,' \
              'medium_code,' \
              'medium_name,' \
              'small_code,' \
              'small_name)' \
              'values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    # 遍历 根据数据的位数判断 1,2,3,4位
    for i in range(len(df.index.values)):
        # print(df.loc[i][1])
        code = str(df.loc[i][0])  # 编码
        name = str(df.loc[i][1])  # 名称
        if(len(code) == 1):
            code_1 = str(df.loc[i][0])  # 编码
            name_1 = str(df.loc[i][1])  # 名称
            print(code_1,name_1)
            param = (v_rate_type, v_rate_time, code_1, name_1,
                     None, None, None, None, None, None )
            cursor.execute(SQL_NEW, param)
            # 提交
            conn.commit()
        if (len(code) == 2):
            code_2 = str(df.loc[i][0])  # 编码
            name_2 = str(df.loc[i][1])  # 名称
            param = (v_rate_type, v_rate_time, code_1, name_1,
                     code_2, name_2, None, None, None, None)
            cursor.execute(SQL_NEW, param)
            # 提交
            conn.commit()
        if (len(code) == 3):
            code_3 = str(df.loc[i][0])  # 编码
            name_3 = str(df.loc[i][1])  # 名称
            param = (v_rate_type, v_rate_time, code_1, name_1,
                     code_2, name_2, code_3, name_3, None, None)
            cursor.execute(SQL_NEW, param)
            # 提交
            conn.commit()
        if (len(code) == 4):
            code_4 = str(df.loc[i][0])  # 编码
            name_4 = str(df.loc[i][1])  # 名称
            param = (v_rate_type, v_rate_time,code_1, name_1,
                     code_2, name_2, code_3, name_3, code_4, name_4)
            cursor.execute(SQL_NEW, param)
            # 提交
            conn.commit()
    close_conn(conn, cursor)  # 关闭数据库
    return 0

# def reprint_2() :
#     df = pd.read_excel('GBT4754-2017(all).xlsx')  # 读取标准表
#     print(len(df.index))
#     # 遍历 根据数据的位数判断 1,2,3,4位
#     for i in range(len(df.index.values)):
#         print()
#     return 0

if __name__ == '__main__':
    reprint()
    # reprint_2()