import pymysql


def databases():
    db_host = "10.127.56.173"
    db_user = "ytluser"
    db_name = "prototype_register"
    return db_host, db_user, db_name


def tables():
    prototype_info = "prototype_info"
    return prototype_info


class YtlMysql():
    def ytl_login(self):
        a = input("请选择数据库连接，1.连接杨天龙的prototype_register库 2选择其他数据库连接 q.退出")
        while True:
            if a == "1":
                db_host = databases()[0]
                print(db_host)
                db_user = databases()[1]
                print(db_user)
                db_pass = input("请输入密码")
                for i in range(2):
                    if db_pass == "ytl":
                        pass
                        break
                    else:
                        db_pass = input("密码错误 重新输入")
                db_name = databases()[2]
                # 打开数据库连接
                self.db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')
                self.cursor = self.db.cursor()  # 使用cursor获取操作游标
                self.cursor.execute("select version()")  # 使用execute方法执行SQL语句
                # 使用fetchone()方法获取一条数据
                data = self.cursor.fetchone()
                print(f"database version:{data}")  # 显示数据库版本
                print(f"欢迎进入杨天龙的{db_name}")
                break
            elif a == "2":
                self.ytl_other_login()  # 登入其他数据库
                break
            elif a == "q":
                break
            else:
                a = input("输入有误，1.连接杨天龙的prototype_register库按 2选择其他数据库连接 q.退出")

    def ytl_other_login(self):
        for i in range(3):
            try:
                db_host = input("请输入IP地址：")
                db_user = input("请输入用户名：")
                db_pass = input("请输入密码：")
                db_name = input("请输入你要连接的数据库名：")
                self.db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name,charset='utf8')
                self.cursor = self.db.cursor()  # 使用cursor获取操作游标
                self.cursor.execute("select version()")  # 使用execute方法执行SQL语句
                data = self.cursor.fetchone()  # 使用fetchone()方法获取一条数据
                print(f"database version:{data}")
                print("连接成功")
                break
            except pymysql.Error as e:
                print(e)
        self.db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')

    def ytl_mysql_sys(self):
        b = input("请选择：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
        while True:
            if b == "1":
                self.ytl_create_database()
                b = input("创建退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "2":
                self.ytl_create_table()
                b = input("创建退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "3":
                self.ytl_insert()
                b = input("增加退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "4":
                self.ytl_delete()
                b = input("删除退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "5":
                self.ytl_update()
                b = input("修改退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "6":
                self.ytl_select()
                b = input("查找退出  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "7":
                self.ytl_show_databases()
                b = input("展示完成  其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "8":
                self.ytl_shoe_tables()
                b = input("展示完成 其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")
            elif b == "q":
                """退出"""
                break
            else:
                b = input("输入有误 其他操作：1.创建库 2.创建表 3.增加数据 4.删除数据 5.修改数据 6.查找数据 7.展示所有库 8.展示所有表 q.关闭数据库")

    def ytl_show_databases(self):
        print("展示所有库")
        ytl_sql = "show databases"
        # 在指定的数据表里面查询数据：
        try:
            self.cursor.execute(ytl_sql)  # 执行sql语句
            # 使用fetchall()方法获取所有数据列表
            data = self.cursor.fetchall()
            # print(f"所有数据列表:{data}")
            for row in data: # 查询所有数据
                print(row)
            print(f"总共{len(data)}个库")

        except pymysql.Error as e:
            print(f"错误：无法传送数据：{e}")

    def ytl_shoe_tables(self):
        print("展示所有表")
        ytl_sql = "show tables"
        # 在指定的数据表里面查询数据：
        try:
            self.cursor.execute(ytl_sql)  # 执行sql语句
            # 使用fetchall()方法获取所有数据列表
            data = self.cursor.fetchall()
            # print(f"所有数据列表:{data}")
            for row in data:  # 查询所有数据
                print(row)
            print(f"总共{len(data)}个表")

        except pymysql.Error as e:
            print(f"错误：无法传送数据：{e}")

    def ytl_create_database(self):
        print("创建库")
        db_name = input("请输入库名")
        ytl_sql = f"create database {db_name}"
        try:
            self.cursor.execute(ytl_sql)  # 执行sql语句
            self.db.commit()  # 提交到数据库执行
            print("创建库已成功")
        except pymysql.Error as e:
            print(f"错误：无法传送数据：{e}")

    def ytl_create_table(self):
        print("创建表")
        table_name = input("请输入表名")
        ytl_sql = f"create table {table_name}"
        try:
            self.cursor.execute(ytl_sql)  # 执行sql语句
            self.db.commit()
            print("创建表已成功")
        except pymysql.Error as e:
            print(f"错误：无法传送数据：{e}")

    def ytl_insert(self):
        print("增加数据")
        table_name = input("请输入表名")
        data = [(input("输入你要添加的数据"))]
        ytl_sql = f"insert into {table_name} values({data})"
        # 在指定的数据表里面查询数据：
        try:
            self.cursor.execute(ytl_sql)  # 执行sql语句
            self.db.commit()
        except pymysql.Error as e:
            print(f"错误：无法传送数据：{e}")

    def ytl_delete(self):
        print("删除库")
        a = input("1.删除库 2.删除表 3.删除数据 q.退出")
        while True:
            if a == "1":
                db_name = input("请输入库名")
                ytl_sql = f"drop database {db_name}"
                # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    self.db.commit()
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("1.删除库 2.删除表 q.退出")
            elif a == "2":
                print("删除表")
                table_name = input("请输入表名")
                ytl_sql = f"drop table {table_name}"
                # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    self.db.commit()
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("1.删除库 2.删除表 q.退出")
            elif a == "3":
                print("删除数据")
                table_name = input("请输入表名")
                delete_id = input("请输入你要删除的id号")
                ytl_sql = f"delete from {table_name} where id = {delete_id}"
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    self.db.commit()
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("1.删除库 2.删除表 q.退出")
            elif a == "q":
                break
            else:
                a = input("输入错误 1.删除库 2.删除表 q.退出")

    def ytl_update(self):
        a = input("1.默认修改user_name 2.自定义修改 q.退出")
        while True:
            if a == "1":
                list_value = input("输入修改新值")
                key_value = input("输入你要修改那一行的id号")
                ytl_sql = f"""
                                update prototype_info set user_name = '{list_value}' where id = {key_value};
                                """
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    self.db.commit()  # 提交到数据库执行
                    print('commit......')
                    break
                except pymysql.Error as e:
                    print(f"修改失败：{e}")
                    print('rollback')
                    self.db.rollback()  # 出现错误时回滚
                    a = input("修改错误 1.默认修改user_name 2.自定义修改 q.退出")
            elif a == "2":
                print("修改数据 1.默认修改user_name 2.自定义修改")
                prototype_info = input("输入表名")
                list_name = input("输入修改列名")
                list_value = input("输入修改新值")
                key_name = input("输入键名")
                key_value = input("输入键值")
                ytl_sql = f"""
                update {prototype_info} set {list_name} = {list_value} where {key_name} = {key_value};
                """
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    self.db.commit()  # 提交到数据库执行
                    print('commit......')
                except pymysql.Error as e:
                    print(f"修改失败：{e}")
                    print('rollback')
                    self.db.rollback()  # 出现错误时回滚
            elif a == "q":
                break
            else:
                a = input("输入有误 1.默认修改user_name 2.自定义修改 q.退出")

    def ytl_select(self):
        print("查找数据")
        """数据库查询操作
        Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
        fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        fetchall():接收全部的返回结果行.
        rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
        """
        a = input("1.默认查询prototype_info表里面的所有数据 2.查询其他表里面的所有数据 3.查询样机在谁名下 4.自定义查询 q.退出")
        while True:
            if a == "1":
                table = tables()  # 调用表名
                ytl_sql = f"select * from {table}"  # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    data = self.cursor.fetchall()  # 使用fetchall()方法获取所有数据列表
                    for row in data:  # 查询所有数据
                        print(row)
                    print(f"总共{len(data)}台")
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
            elif a == "2":
                table_name = input("输入表名")
                ytl_sql = f'select * from {table_name}'  # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    data = self.cursor.fetchall()  # 使用fetchall()方法获取所有数据列表
                    for row in data:  # 查询所有数据
                        print(row)
                    print(f"总共{len(data)}台")
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("输入有误 1.默认查询prototype_info表里面的所有数据 2.查询其他表里面的数据 3.自定义查询 q.退出")
            elif a == "3":
                table = tables()  # 调用表名
                ytl_sql = f'select id,id_name,name,user_name,borrow_time,still_time from {table}'  # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    data = self.cursor.fetchall()  # 使用fetchall()方法获取所有数据列表
                    for row in data:  # 查询所有数据
                        print(row)
                    print(f"总共{len(data)}台")
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("输入有误 1.默认查询prototype_info表里面的所有数据 2.查询其他表里面的数据 3.自定义查询 q.退出")
            elif a == "4":
                ytl_sql = input("输入自定义的sql语句")  # 在指定的数据表里面查询数据：
                try:
                    self.cursor.execute(ytl_sql)  # 执行sql语句
                    data = self.cursor.fetchall()  # 使用fetchall()方法获取所有数据列表
                    for row in data:  # 查询所有数据
                        print(row)
                    print(f"总共{len(data)}台")
                    break
                except pymysql.Error as e:
                    print(f"错误：无法传送数据：{e}")
                    a = input("输入有误 1.默认查询prototype_info表里面的所有数据 2.查询其他表里面的数据 3.自定义查询 q.退出")
            elif a == "q":
                break
            else:
                a = input("输入有误 1.默认查询prototype_info表里面的所有数据 2.查询其他表里面的数据 3.自定义查询 q.退出")

    def ytl_main(self):
        a = input("请先登入数据库 l.登入 q.退出")
        while True:
            if a == "l":
                self.ytl_login()
                self.ytl_mysql_sys()
                self.db.close()  # 关闭数据库
                print("数据库已关闭")
                break
            elif a == "q":
                print("退出")
                break
            else:
                a = input("输入有误 请重新输入 l登入 q退出")


if __name__ == '__main__':
    YtlMysql = YtlMysql()
    YtlMysql.ytl_main()