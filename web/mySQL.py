'''
MySQL是Web世界中使用最广泛的数据库服务器。
SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

$sudo apt-get install mysql-server mysql-client
 password: password


在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000

service mysqld restart
$ mysql -u root -p
mysql> show variables like '%char%';



由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
$ pip3 install mysql-connector-python --allow-external mysql-connector-python -i http://pypi.v2ex.com/simple



'''
import mysql.connector

conn=mysql.connector.connect(user='root',password='password',database='test')
cursor=conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

# 提交事务:执行INSERT等操作后要调用commit()提交事务；
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()


#由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
