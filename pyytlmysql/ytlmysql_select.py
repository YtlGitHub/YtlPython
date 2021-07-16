import pymysql


db_host = "10.127.56.173"
db_user = "root"
db_pass = "ytl"
db_name = "prototype_register"


# 打开数据库连接
db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')
cursor = db.cursor()  # 使用cursor获取操作游标

"""数据库查询操作
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall():接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
"""

# 查询工资大于1000的所有数据
sql = f"""
SELECT * FROM EMPLOYEE where income > 1000
"""
# 查询prototype_info这个数据表里面的数据
YTL_SQL = """
select id,id_name,de,brand,pv,os,IMEI,name,user_name from prototype_info
"""
# 你要加的条件
where = """
where user_name = '杨天龙' and pv = 11
"""

# 在指定的数据表里面查询数据：
try: 
    cursor.execute(YTL_SQL+where)  # 执行sql语句
    # 使用fetchall()方法获取所有数据列表
    data = cursor.fetchall()
    # print(f"所有数据列表:{data}")
    # 查询所有数据
    for row in data:
        print(row)
    print(f"总共{len(data)}台")

except pymysql.Error as e:
    print(f"错误：无法传送数据：{e}")

finally:
    if db:
        db.close()
        print("关闭数据库")