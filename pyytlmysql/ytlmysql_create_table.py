import pymysql


db_host = "10.127.56.173"
db_user = "root"
db_pass = "ytl"
db_name = "prototype_register"

# 在指定的数据库里面创建数据表：
try:
    db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
    cursor = db.cursor()  # 使用cursor获取操作游标
    sql = """create table EMPLOYEE(
                FIRST_NAME  CHAR(20) NOT NULL,
                LAST_NAME  CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)
    """
    cursor.execute(sql)
    db.commit()  # 提交到数据库执行
except pymysql.Error as e:
    print(f"数据库连接失败：{e}")

finally:
    if db:
        db.close()
        print("关闭数据库")