import pymysql


db_host = "10.127.56.173"
db_user = "root"
db_pass = "ytl"
db_name = "prototype_register"


db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
cursor = db.cursor()  # 使用cursor获取操作游标
sql = f"""
update prototype_info set user_name = '钱磊' where id = 3;
"""

# 在指定的数据表里面插入数据：
try:
    cursor.execute(sql)  # 执行sql语句
    db.commit()  # 提交到数据库执行
    print('commit......')
except pymysql.Error as e:
    print(f"修改失败：{e}")
    print('rollback')
    db.rollback()  # 出现错误时回滚

finally:
    if db:
        db.close()
        print("关闭数据库")