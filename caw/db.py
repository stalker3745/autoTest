'''
操作数据库
      连接数据库----执行sql语句-----断开连接
      pip install pymysql
'''
import pymysql


def connect(db_info):
    conn = pymysql.connect(host=db_info['ip'], user=db_info['user'], password=db_info['pwd'],
                 database=db_info['dbname'], port=db_info['port'],
                 charset='utf8')
    return conn

def execute(conn, sql):
    c = conn.cursor()  # 获取游标，游标是用来处理数据的。连接看做一条路，游标可以看做跑在路上的车
    c.execute(sql) # 执行sql语句
    print(f"执行sql语句：{sql}成功")
    r = c.fetchall()  # 获取查询的结果
    conn.commit() # 提交
    c.close()  # 关闭游标
    return r  #返回结果

def disconnect(conn):
    conn.close()

# 屏蔽了sql语句；脚本调用简单
def delete_user(db_info, phone):
    c = connect(db_info)
    execute(c, f"delete from member where mobilephone='{phone}'")
    disconnect(c)

# 根据手机号码查询余额
def get_amount(db_info, phone):
    c = connect(db_info)
    r = execute(c, f"select leaveamount from member where mobilephone='{phone}'")
    disconnect(c)
    if len(r) !=0:    # 元组的长度不为0
        return r[0][0]
    else:
        return 0

def get_userPhone(db_info, phone):
    c = connect(db_info)
    return execute(c, f"select * from zd_user where user_phone='{phone}'")

def get_zd_form_entitydata(db_info, appid):
    c = connect(db_info)
    return execute(c, f"SELECT count(*) from zd_form_entitydata WHERE app_id={appid} and is_deleted=0")


def updata_formentity(db_info, appid):
    c = connect(db_info)
    execute(c, f"UPDATE zd_form_entitydata SET is_deleted=1,gmt_modified=NOW()  WHERE app_id={appid}")
    disconnect(c)

# 测试代码，用完可以删除
if __name__ == '__main__':
    db_info = {"ip": "47.97.254.131", "port": 3506, "user": "zhidian_test", "pwd": "zhidian#022", "dbname": "project_construction_test"}
    # delete_user(db_info, "18012345678")
    c = connect(db_info)
    # print(c)
    # You have an error in your sql syntax  sql语句有语法错误
    b = execute(c, "select * from zd_user where user_phone='15529310001'")
    print(b)   # ((Decimal('500010.00'),),)
    # if len(b) !=0:
    #     print(b[0])  # (Decimal('30.00'),)
    #     print(b[0][0]) # 30.00
    # b = execute(c, "select * from member where mobilephone='18012345678'")
    # print(b)
    # disconnect(c)