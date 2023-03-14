#连接数据库  获取游标
import pymysql
from tech_data.category import get_code

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                    user="root",
                    password="reliable",
                    db="tech",
                    charset="utf8mb4")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    if ((conn != None) & (cursor != None)):
        print("数据库连接成功 ...")
    else:
        print("数据库连接失败！")
    return conn, cursor
#关闭数据库连接和游标
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    return 1
# 数据表名
# 中图分类名
def insert_mysql(data,name,tableName):
    print(data['title'])

    id=data['id']
    title=data['title']
    alternativeTitle=data['alternativeTitle']
    creator=data['creator']
    abstractEn=data['abstractEn']
    keywordsEn=data['keywordsEn']
    abstractCn=data['abstractCn']
    keywordsCn=data['keywordsCn']
    creatOrorganization=data['creatOrorganization']
    prepareOrganization=data['prepareOrganization']
    publicDate=data['publicDate']
    createTime=data['createTime']
    projectName=data['projectName']
    competentOrg=data['competentOrg']
    projectSubjectName=data['projectSubjectName']
    projectSubjectId=data['projectSubjectId']
    #------------------------------
    classification=name   # 修改
    #------------------------------
    classificationCode=get_code(classification)   # 需要调用get_code(name)获取
    responsiblePerson = data['responsiblePerson']
    supportChannel = data['supportChannel']
    undertakeOrg = data['undertakeOrg']
    kjbgSource = data['kjbgSource']
    proposalDate = data['proposalDate']
    submittedDate = data['submittedDate']
    kjbgRegion = data['kjbgRegion']
    collectionDate = data['collectionDate']
    collectionNumber = data['collectionNumber']
    fieldCode = data['fieldCode']
    fieldId = data['fieldId']
    kjbgQWAddress = data['kjbgQWAddress']
    isNewRecord = data['isNewRecord']
    sourceUrl = "https://www.nstrs.cn/kjbg/detail?id="+id          # 需要自己拼 https://www.nstrs.cn/kjbg/detail?id=

    conn, cursor = get_conn()
    # ------------------------------ 修改表名
    sql = "insert into `"+tableName+"` (id,title,alternativeTitle,creator,abstractEn," \
          "keywordsEn,abstractCn,keywordsCn,creatOrorganization,prepareOrganization," \
          "publicDate,createTime,projectName,competentOrg,projectSubjectName," \
          "projectSubjectId,classification,classificationCode,responsiblePerson,supportChannel," \
          "undertakeOrg,kjbgSource,proposalDate,submittedDate,kjbgRegion," \
          "collectionDate,collectionNumber,fieldCode,fieldId,kjbgQWAddress," \
          "isNewRecord,sourceUrl) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" \
          ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        try:
            cursor.execute(sql, [id,title,alternativeTitle,creator,abstractEn,
                      keywordsEn,abstractCn,keywordsCn,creatOrorganization,prepareOrganization,
                      publicDate,createTime,projectName,competentOrg,projectSubjectName,
                      projectSubjectId,classification,classificationCode,responsiblePerson,supportChannel,
                      undertakeOrg,kjbgSource,proposalDate,submittedDate,kjbgRegion,
                      collectionDate,collectionNumber,fieldCode,fieldId,kjbgQWAddress,isNewRecord,sourceUrl])
        except pymysql.err.IntegrityError:
            print("主键冲突！")
        conn.commit()  # 提交事务 update delete insert操作
    except pymysql.err.IntegrityError:
        print("error！")
    finally:
        close_conn(conn, cursor)
    return 1

if __name__ == '__main__':
    print()