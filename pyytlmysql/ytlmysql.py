import pymysql


db_host = "10.127.56.173"
db_user = "root"
db_pass = "ytl"
db_name = "prototype_register"

# 判断是否连接上数据库，并查看数据库版本：
try:
    db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor获取操作游标
    cursor.execute("select version()")  # 使用execute方法执行SQL语句
    # 使用fetchone()方法获取一条数据
    data = cursor.fetchone()
    print(f"database version:{data}")
except pymysql.Error as e:
    print(f"数据库连接失败：{e}")

finally:
    if db:
        db.close()
        print("关闭数据库连接......")

