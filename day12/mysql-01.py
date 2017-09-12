# Author:Bob

import pymysql

# 创建连接,相当于创建了一个socket
conn = pymysql.connect(host="192.168.42.30", port=3306, user="root", password="123", db="test")
# 创建游标,相当于在socket上创建了一个实例
cursor = conn.cursor()

# 执行sql,并且返回受影响的行数
sql = 'select * from goods'
effect_row = cursor.execute(sql)
#github上修改测试
print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
