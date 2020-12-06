# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, DECIMAL,String, Date, DateTime, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
Base = declarative_base()

#一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

class User_table(Base):
    #用户 id、用户名 
    __tablename__ = 'q6_user'
    user_id = Column(Integer(), primary_key=True,autoincrement=True)
    user_name = Column(String(50), index=True)
    
    # 添加配置设置编码
    __table_args__ = {
        'mysql_charset':'utf8mb4',
        'mysql_collate':'utf8mb4_general_ci'
    }

class Asset_table(Base):
    #用户 id、用户名 
    __tablename__ = 'q6_asset'
    user_id = Column(Integer(), primary_key=True )
    asset = Column(DECIMAL(21,3), index=True)
    
class Transaction_table(Base):
    #用户 id、用户名 
    __tablename__ = 'q6_transaction'
    user_id_from = Column(Integer(), primary_key=True )
    user_id_to = Column(Integer(), primary_key=True )
    posted_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    amount = Column(DECIMAL(21,3), index=True)

# 实例一个引擎
dburl = "mysql+pymysql://remoteUser:testabcd@192.168.3.83:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加User数据
# user_demo = User_table(user_name=u'shark' )
# user_demo2 = User_table(user_name=u'zhang san' )
# user_demo3 = User_table(user_name=u'wang wu' )

# session.add(user_demo)
# session.add(user_demo2)
# session.add(user_demo3)
# session.flush()

# session.commit()

# 增加资产数据
# asset_demo = Asset_table(user_id=1, asset=10000.50 )
# asset_demo2 = Asset_table(user_id=2, asset=450.50 )
# asset_demo3 = Asset_table(user_id=3, asset=50.00 ) #余额小于转账金额100

# session.add(asset_demo)
# session.add(asset_demo2)
# session.add(asset_demo3)
# session.flush()

from_user = session.query(Asset_table).filter(Asset_table.user_id == 3).one() 

to_user = session.query(Asset_table).filter(Asset_table.user_id == 1).one() 

transfer_value = 100

if (from_user.asset >= transfer_value ):
    transaction_demo = Transaction_table(user_id_from=3, user_id_to=1, amount=transfer_value )
    asset_demo = Asset_table(user_id=from_user, asset= from_user.asset - transfer_value )
    asset_demo3 = Asset_table(user_id=to_user, asset= to_user.asset +  transfer_value)

    session.commit()
    print('交易成功')
else:
    print('余额不足')
    session.rollback()


