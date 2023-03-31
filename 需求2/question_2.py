"""
需要把爬取的数据，行业名称和tpc_national_industrial_tree
表的code对应一下，将tpc_national_industrial_tree 表的code
添加到tpc_consumption_detail表即可
"""
import into_mysql as sql_utils
"""
需要处理的表：tpc_consumption_detail
需要处理的字段：trade_code、trade_name
trade_name 需要对应到表 tpc_national_industrial_tree 的 code_name 字段
trade_code 对应 code字段
其中或需要用到模糊匹配，要清除空格等无效字符
"""
def question_2():
    res_trade_code = []
    conn,cursor = sql_utils.get_conn()
    # 拿到所有的 trade_name
    SQL_TRADE_NAME = 'select trade_name from tpc_consumption_detail'
    trade_name_list = sql_utils.query(SQL_TRADE_NAME)
    # print(trade_name_list)
    # 查询标准表的名称和编码
    # SQL_STD = 'select code,code_name from tpc_national_industrial_tree'
    # std_list = sql_utils.query(SQL_STD)
    # print(std_list[0])
    for item_outer in trade_name_list:
        # print(item_outer[0])
        item_outer_0 = str(item_outer[0]).replace(' ','')   # 替换空格
        item_outer_1 = item_outer_0.replace('\t','')    # 替换制表符
        item_outer_2 = item_outer_1.replace('\u2002','')    # 替换特殊字符
        # 第一次清洗 常规全模糊匹配
        SQL_RES = "SELECT `code` FROM `tpc_national_industrial_tree` where " \
                  "code_name like '%%%s%%' ORDER BY `code` LIMIT 1;"%item_outer_2
        temp_trade_code = None
        temp_trade_code = sql_utils.query(SQL_RES)
        # print(temp_trade_code)
        """
        黑色金属冶炼及压延加工业
        黑色金属冶炼和压延加工业
        """
        # 第二次清洗 以‘和’分割字符串 取前者模糊匹配
        if len(temp_trade_code) == 0:
            item_outer_3 = item_outer_2.split('和')[0]
            SQL_RES = "SELECT `code` FROM `tpc_national_industrial_tree` where " \
                      "code_name like '%%%s%%' ORDER BY `code` LIMIT 1;"%item_outer_3
            temp_trade_code = sql_utils.query(SQL_RES)
        # 第三次清洗 以‘及’分割字符串 取前者模糊匹配
        if len(temp_trade_code) == 0:
            item_outer_4 = item_outer_2.split('及')[0]
            SQL_RES = "SELECT `code` FROM `tpc_national_industrial_tree` where " \
                      "code_name like '%%%s%%' ORDER BY `code` LIMIT 1;"%item_outer_4
            temp_trade_code = sql_utils.query(SQL_RES)
        # 第四次清洗 直接取原字符串的前3个字符模糊匹配
        if len(temp_trade_code) == 0:
            item_outer_5 = item_outer_2[:2]
            SQL_RES = "SELECT `code` FROM `tpc_national_industrial_tree` where " \
                      "code_name like '%%%s%%' ORDER BY `code` LIMIT 1;"%item_outer_5
            temp_trade_code = sql_utils.query(SQL_RES)
        if len(temp_trade_code) == 0:
            print('没有匹配到code值')
            # 如果没有匹配到，存入空值
            res_trade_code.append(None)
        else:
            res_trade_code.append(str(temp_trade_code[0][0]))   # 清洗结果转字符串存入列表
    # print(len(res_trade_code))
    # 分别遍历清洗后的列表和原始数据
    for code,name in zip(res_trade_code,trade_name_list):
        param = []  # 暂时存code和name
        param.append(code)
        param.append(name)
        # 根据name找到需要更新的那一行，然后把其对应的code插入到trade_code字段
        SQL_UPDATE = 'update tpc_consumption_detail set trade_code = %s where trade_name = %s'
        cursor.execute(SQL_UPDATE,param)    # 执行sql
    conn.commit()   # 提交事务
    sql_utils.close_conn(conn,cursor)   # 关闭数据库
    return
if __name__ == '__main__':
    question_2()