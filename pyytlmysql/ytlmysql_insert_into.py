import pymysql


db_host = "10.127.56.173"
db_user = "root"
db_pass = "ytl"
db_name = "prototype_register"


db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
cursor = db.cursor()  # 使用cursor获取操作游标

data = [
    (1,	'user', 'name', age,'地址'),
    (2,	'user', 'name', age,'地址'),
    (3,	'user', 'name', age,'地址'),
    (4,	'user', 'name', age,'地址'),
]
data1 = [(1,	'user', 'name', age,'地址')]

export_data = [
                (1,	'user', 'name', age,'地址'),
                (2,	'user', 'name', age,'地址'),
                (3,	'user', 'name', age,'地址'),
                (4,	'user', 'name', age,'地址'),
]

sql = """
insert into prototype_info(id_name,de,brand,pv,os,m_name,IMEI,name,user_name,borrow_time,still_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
sql1 = """
insert into prototype_info(id_name,de,brand,pv,os,m_name,IMEI,name,user_name,borrow_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
export_sql = """
insert into prototype_export(pc,de,brand,pv,os,m_name,IMEI) values(%s,%s,%s,%s,%s,%s,%s)
"""
# 在指定的数据表里面插入数据：
try:
    cursor.executemany(export_sql, export_data)  # 执行sql语句
    db.commit()  # 提交到数据库执行
    print('commit......')
    # 使用fetchone()方法获取一条数据
    data = cursor.fetchone()
    print(f"数据:{data}")
except pymysql.Error as e:
    print(f"插入失败：{e}")
    print('rollback')
    db.rollback()  # 出现错误时回滚

finally:
    if db:
        db.close()
        print("关闭数据库")

