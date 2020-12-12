学习笔记
Django开发

安装
pip install --upgrade django==2.2.17 -i https://pypi.douban.com/simple
pip install --upgrade pymysql -i https://pypi.douban.com/simple

$ python manage.py help --- 查看该工具的具体功能
$ python manage.py startapp index

9. 使用ORM创建数据表： 记录了2个坑的解决办法. 解决方法见5c的readme
\Python39\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query
AttributeError: 'str' object has no attribute 'decode'