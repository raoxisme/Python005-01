## 作业注意事项
作业一：
使用 REST API 实现一个 Order（订单）类，并使用 json 展示数据，要求如下：

/orders 列出所有 order
/orders/{id} 列出具体的一个订单
/orders/create 只接受 Post 请求创建一个订单
/orders/{id}/cancel 接受 Get 请求，取消一个订单。 （提示： sql update）
选做：/orders 列出所有 order 带分页功能

>> Orders model 枚举属性status，可用值 1-New, 2-Cancelled ;撤销以后不可以再改为New； 通过HTTP PATCH提交请求

作业二：
基于 Django REST framework 实现用户接入控制功能

说明：
对作业一的 /orders/create 接口实现用户接入控制功能。
可以使用 SessionAuthentication 或 TokenAuthentication 实现。
选做：使用 Json-Web-Token（JWT）认证方式实现

>> permission功能实现为：除登录控制外，设置枚举属性-用户组：普通用户（1-Customer：创建和查看修改自己的），订单执行人（2-OrderExecutor: 查看所有人的；不能修改）

### 安装
No module named 'rest_framework’
安装：  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework

其他安装组件
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  django-filter
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  django-notifications-hq
-->不要 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  notifications
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  coreapi pyyaml

### 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'microblog_dbv5',
        'USER': 'remoteUser',
        'PASSWORD': 'testestabcdtpass',
        'HOST': '192.168.3.83', 
        'PORT': '3306',
    }
}

初始化： 
1.python3 .\manage.py makemigrations
2.python3 .\manage.py migrate

### 创建super user
python manage.py createsuperuser
user: admin@xyz.com
pwd: abcd1234

### 项目文件夹 microcrm_v1 启动服务
python3 .\manage.py runserver

### API 测试
安装： pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  httpie   

测试url:   
http GET http://127.0.0.1:8000/api/v1/orders/
http GET http://127.0.0.1:8000/api/v1/orders/1

Basic Authenticate:
- http -a customer:12345 POST http://127.0.0.1:8000/api/v1/orders/ body="order1111" title="test" 
- http -a customer:12345 POST http://127.0.0.1:8000/api/v1/orders/1/cancel

JWT Logon:
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple djangorestframework-jwt

- http -a customer:12345 POST http://127.0.0.1:8000/login/ username="customer" password="12345"   
记录下response中的token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjEwODg1OTQ2LCJlbWFpbCI6ImFiZEB4eXouY29tIn0.nZEiKbZzYfD4JOdah-yOcntX3yaawhii_Fm_4yLuC_U

http  POST http://127.0.0.1:8000/api/v1/orders/ body="order1111" title="test" Authorization:"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImN1c3RvbWVyIiwiZXhwIjoxNjEwODg1OTQ2LCJlbWFpbCI6ImFiZEB4eXouY29tIn0.nZEiKbZzYfD4JOdah-yOcntX3yaawhii_Fm_4yLuC_U"