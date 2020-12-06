# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, Date, DateTime, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
Base = declarative_base()

class User_table(Base):
    #用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
    __tablename__ = 'userorm'
    user_id = Column(Integer(), primary_key=True,autoincrement=True)
    user_name = Column(String(50), index=True)
    age = Column(Integer(), nullable=True)
    birthdate = Column(Date(), nullable=True)
    gender = Column(String(1), nullable=True)
    education = Column(String(1), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    
    # 添加配置设置编码
    __table_args__ = {
        'mysql_charset':'utf8mb4',
        'mysql_collate':'utf8mb4_general_ci'
    }

    def __repr__(self):
        return "User_table(user_id='{self.user_id}', " \
            "user_name={self.user_name}) ," \
            "age={self.age}) ," \
            "birthdate={self.birthdate}) ," \
            "gender={self.gender}) ," \
            "education={self.education}) ," \
            "created_on={self.created_on}) ," \
            "updated_on={self.updated_on})".format(self=self)


# Float 
# Decimal
# Boolean
# Text
# autoincrement 

# 业务逻辑
# 持久层
# 数据库层


# 实例一个引擎
dburl = "mysql+pymysql://remoteUser:testabcd@192.168.3.83:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
user_demo = User_table(user_name=u'shark', age=55, birthdate='1959-12-31',gender='M', education='4' )
user_demo2 = User_table(user_name=u'zhang san', age=20, birthdate='2000-12-31',gender='M', education='3')
user_demo3 = User_table(user_name=u'wang wu', age=33, birthdate='1998-12-31',gender='F', education='3')
print(user_demo)

# 增加多条数据
session.add(user_demo)
session.add(user_demo2)
session.add(user_demo3)
session.flush()

# 使用迭代代替all()
# result = session.query(Book_table).all()
# for result in session.query(Book_table):
#     print(result)

# result = session.query(Book_table).first()
# one() 
# scalar()

# 指定列数
# session.query(Book_table.book_name).first()

# 排序
from sqlalchemy import desc
# for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
#      print(result)

# 降序
# query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
# print([result.book_name for result in query])

# 聚合函数
# from sqlalchemy import func
# result = session.query(func.count(Book_table.book_name)).first()
# print(result)

# 条件
# print( session.query(Book_table).filter(Book_table.book_id < 20).first() )
print( session.query(User_table).filter(User_table.age > 35, User_table.age <60) )

# 连接词
# from sqlalchemy import and_, or_, not_
# filter(
#     or_(
#         Book_table.xxx.between(100, 1000),
#         Book_table.yyy.contains('book')
#     )
# )
session.commit()

