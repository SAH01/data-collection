import pandas as pd
import pymysql
import xlwt

#--------------------------------------------
def get_conn():
    """
    获取连接和游标
    :return:
    """
    conn=pymysql.connect(host="127.0.0.1",
                         user="root"
                              ""
                              "",
                         password="000429",
                         db="spark",
                         charset="utf8")
    cursor=conn.cursor()
    return conn,cursor

def close_conn(conn, cursor):
    """
    关闭连接和游标
    :param conn:
    :param cursor:
    :return:
    """
    if cursor:
        cursor.close()
    if conn:
        conn.close()
#query
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
#--------------------------------------------

#读取csv文件

def get_csv(filename):
    conn,cursor=get_conn()
    csv_data=pd.read_excel(filename)
    # print(csv_data.loc[0].values[1])
    values=[]
    for i in range(len(csv_data.index.values)):
        # print(csv_data.loc[i].values)
        SQL = "insert into elec values(%s,%s,%s)"
        values.append(csv_data.loc[i].values[0])
        values.append(csv_data.loc[i].values[1])
        values.append(csv_data.loc[i].values[2])
        print(values)
        try:
            cursor.execute(SQL,values)  # 执行sql语句
            conn.commit()  # 提交事务
            print("插入成功:\n", csv_data.loc[i].values[0],"，第"+str(i+1)+"条数据！")
            print("--------------------------------------------------")
        except:
            print("插入失败:\n", csv_data.loc[i].values[0])
        finally:
            values=[]
    return

#用户类型分类
def get_type():
    conn,cursor=get_conn()
    SQL= "select * from elec_0;"
    res_data=query(SQL)
    temp_data=[]
    result=[]
    for item in res_data:
        if (float(item[1])>=707.26 and float(item[2])>=6.66):
            temp_data.append("高价值型客户")
            temp_data.append(item[0])
            print(item[0]+": 高价值型客户！")
            result.append(temp_data)
            temp_data=[]
        if (float(item[1])>=707.26 and float(item[2])<6.66):
            temp_data.append("潜力型客户")
            temp_data.append(item[0])
            print(item[0]+": 潜力型客户！")
            result.append(temp_data)
            temp_data=[]
        if (float(item[1])<707.26 and float(item[2])>=6.66):
            temp_data.append("大众型客户")
            temp_data.append(item[0])
            print(item[0]+": 大众型客户！")
            result.append(temp_data)
            temp_data=[]
        if (float(item[1])<707.26 and float(item[2])<6.66):
            temp_data.append("低价值型客户")
            temp_data.append(item[0])
            print(item[0]+": 低价值型客户！")
            result.append(temp_data)
            temp_data=[]
    INTO_SQL="insert into user_type values(%s,%s);"
    for items in result:
        VALUES=items
        cursor.execute(INTO_SQL,VALUES)
        conn.commit()  # 提交事务
    close_conn(conn,cursor)
    return result
if __name__ == '__main__':
    # get_csv("1647848272130494.xlsx")
    res=get_type()
    print(res)