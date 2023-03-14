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
# 读取源数据表std_code_2017，拆分字段插到新的数据表national_industrial_code
def func_into_new_table() :
    conn,cursor = get_conn() # 连接数据库data_cleaning
    SQL = 'SELECT * FROM std_code_2017;'
    res_data = query(SQL)
    v_rate_type = '01'
    v_rate_time = '2023'
    # print(res_data[0])
    # 分别处理 编码code 和名称name 处理一条插入一条
    for item in res_data:
        code = str(item[0])  # 编码如A0111
        name = str(item[1])  # 名称如'门类·大类·中类·小类'
        # 四级分类编码和名称分别从1~4 如下
        code_1 = code[0:1]  # 如 A
        code_2 = code[1:3]  # 如 01
        code_3 = code[1:4]  # 如 011
        code_4 = code[1:5]  # 如 0111
        name_1 = name.split('·')[0]
        name_2 = name.split('·')[1]
        name_3 = name.split('·')[2]
        name_4 = name.split('·')[3]
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
        param = (v_rate_type,v_rate_time,code_1,name_1,
                 code_2,name_2,code_3,name_3,code_4,name_4)
        cursor.execute(SQL_NEW,param)
        # 提交
        conn.commit()
    close_conn(conn,cursor) # 关闭数据库
    return 0

if __name__ == '__main__':
    func_into_new_table()
