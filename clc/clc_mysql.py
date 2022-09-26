import pandas as pd
import pymysql
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

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
"""
-----------------------------------------------------------
"""
def into_mysql(filename):
    category_code = ""      #门类编码
    category_name = ""      #门类名称
    global count
    conn,cursor=get_conn()  #连接mysql
    if(conn!=None):
        print("数据库连接成功！")
    print(filename)
    df = pd.read_excel(filename)  # 读取标准表
    for i in range(len(df.index.values)):
        # print(df.loc[i][1])
        code = str(df.loc[i][0])  # 所有的编码
        name = str(df.loc[i][1])  # 所有的名称
        print(code+": "+name)
        SQL = "insert into std_lib (lib_code,lib_name) values(%s,%s)"%("\""+code+"\"","\""+name+"\"")
        print(SQL)
        cursor.execute(SQL)  # 执行sql语句
        conn.commit()  # 提交事务
        print("--------------------------------------------------")
    close_conn(conn, cursor)  # 关闭数据库连接
    return 1

if __name__ == '__main__':
    into_mysql("中图分类号.xlsx")