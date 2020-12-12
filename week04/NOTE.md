学习笔记
Django开发

安装
pip install --upgrade django==2.2.17 -i https://pypi.douban.com/simple
pip install --upgrade pymysql -i https://pypi.douban.com/simple

导入数据表dump文件.表结构：movie_title | short_evaluate | star
source t2.sql

$ python3 manage.py help --- 查看该工具的具体功能
$ python3 manage.py startapp index
$ python3 manage.py runserver

9. 使用ORM创建数据表： 记录了2个坑的解决办法. 解决方法见5c的readme
\Python39\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query
AttributeError: 'str' object has no attribute 'decode'

6. 将数据库和已经建好的表也转换成utf8mb4
更改数据库编码：
DATABASE caitu99 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

更改表编码：
ALTER TABLE TABLE_NAME CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

python3 manage.py runserver