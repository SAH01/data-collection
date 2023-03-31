"""
tpc_national_zonging_code 表数据，
使用Python转换成新表的结构数据(tpc_national_zonging_tree)
"""
import datetime
import into_mysql as sql_utils
"""
清理重复数据
DELETE t1
FROM
	tpc_national_zonging_code t1
INNER JOIN tpc_national_zonging_code t2
WHERE
	t1.id > t2.id
AND t1.country_name = t2.country_name
AND t1.country_name = '市辖区';
"""
def question_1():
    conn,cursor = sql_utils.get_conn()
    res_list = []   # 从数据库中拿到8个字段值
    province_code = ''  # 存省编号
    city_code = ''  # 存市编号
    country_code = ''   # 存区编号
    SQL_QUERY = 'SELECT t.province_code,t.province_name,t.city_code,t.city_name,t.country_code,' \
                't.country_name,t.towntr_code,t.towntr_name FROM `tpc_national_zonging_code` t;'
    res_list=sql_utils.query(SQL_QUERY) # 拿到所有数据
    """
    发现如下规律，set处理前五行数据之后，
    非重复列表长度正好对应了不同的省市区街道分级。
    """
    # 长度3 ：130000	河北省
    print(len(set((res_list[0]))))
    # 长度5 ：130000	河北省	130100000000	石家庄市
    print(len(set((res_list[1]))))
    # 长度7 ：130000	河北省	130100000000	石家庄市	130101000000	市辖区
    print(len(set((res_list[2]))))
    #长度7 ：130000	河北省	130100000000	石家庄市	130102000000	长安区
    print(len(set((res_list[3]))))
    #长度8 ：130000	河北省	130100000000	石家庄市	130102000000	长安区	130102001000	建北街道
    print(len(set((res_list[4]))))
    now_time = datetime.datetime.now()
    now_date = now_time.strftime("%Y-%m-%d %H:%M:%S")   # 获取当前系统时间
    for item in res_list:
        # print(item)
        flag = len(set(item))
        # print(flag)
        if (flag == 3):
            param = []
            province_code = str(item[0])
            province_name = str(item[1])
            parent_code = '0'   # 省上一级code 默认0
            # parent_code = 0; code = province_code
            SQL_INSERT = 'insert into tpc_national_zonging_tree values (NULL,%s,%s,%s,%s,%s)'
            param.extend([province_code,province_name,parent_code,now_date,now_date])
            cursor.execute(SQL_INSERT,param)
            conn.commit()
        if (flag == 5):
            param_0 = []
            city_code = str(item[2])
            city_name = str(item[3])
            # parent_code = province_code; code = city_code
            parent_code = province_code
            SQL_INSERT_0 = 'insert into tpc_national_zonging_tree values (NULL,%s,%s,%s,%s,%s)'
            param_0.extend([city_code, city_name, parent_code, now_date, now_date])
            cursor.execute(SQL_INSERT_0, param_0)
            conn.commit()
        if (flag == 7):
            param_1 = []
            country_code = str(item[4])
            country_name = str(item[5])
            # parent_code = city_code; code = country_code
            parent_code = city_code
            SQL_INSERT_1 = 'insert into tpc_national_zonging_tree values (NULL,%s,%s,%s,%s,%s)'
            param_1.extend([country_code, country_name, parent_code, now_date, now_date])
            cursor.execute(SQL_INSERT_1, param_1)
            conn.commit()
        if (flag == 8):
            param_2 = []
            towntr_code = str(item[6])
            towntr_name = str(item[7])
            # parent_code = country_code; code = towntr_code
            parent_code = country_code
            SQL_INSERT_2 = 'insert into tpc_national_zonging_tree values (NULL,%s,%s,%s,%s,%s)'
            param_2.extend([towntr_code, towntr_name, parent_code, now_date, now_date])
            cursor.execute(SQL_INSERT_2, param_2)
            conn.commit()
    sql_utils.close_conn(conn,cursor)   # 关闭数据库
    return
if __name__ == '__main__':
    question_1()
