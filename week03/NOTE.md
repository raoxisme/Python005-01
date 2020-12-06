学习笔记

### 作业
#### 1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。

- 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
- 将增加远程用户的 SQL 语句作为作业内容提交

> 回答
mysql>CREATE DATABASE 'testdb' /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */   
mysql>grant all privileges on *.* to 'remoteUser'@'%' identified by 'abcd1234' with grant option;   
mysql>flush privileges;   
$>service mysql restart   

ubuntu 16.04安装mysql参考：https://blog.csdn.net/itxiaolong3/article/details/77905923   
win10链接虚拟机的mysql: https://blog.csdn.net/rongxiangbo/article/details/78085136   
     （初始：NAT，变为bridge）

vim /etc/my.cnf    
show variables like '%character%';   
create database db1;   
show create database db1;   

#### 2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

- 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
- 将 ORM、插入、查询语句作为作业内容提交

> 回答
代码：Q2_orm_insert_select.py

#### 3. 为以下 sql 语句标注执行顺序：

- `SELECT DISTINCT player_id, player_name, count(*) as num` #5
- `FROM player JOIN team ON player.team_id = team.team_id`  #1
- `WHERE height > 1.80` #2
- `GROUP BY player.team_id`  #3
- `HAVING num > 2` #4
- `ORDER BY num DESC` #6
- `LIMIT 2` #7



#### 4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

Table1  
id name  
1 table1_table2   
2 table1   

Table2   
id name   
1 table1_table2   
3 table2   

举例: INNER JOIN
`SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;`

INNER JOIN 查询结果：
|  Table1.id   | Table1.name  | Table2.id | Table2.name  |
|  ---  | ---  | --- | ---  |
|  1  |  table1_table2  | 1 | table1_table2  |

LEFT JOIN 查询结果：
|  Table1.id   | Table1.name  | Table2.id | Table2.name  |
|  ---  | ---  | --- | ---  |
|  1  |  table1_table2  | 1 | table1_table2  |
|  1   | table1_table2  |   |   |


RIGHT JOIN 查询结果：
|  Table1.id   | Table1.name  | Table2.id | Table2.name  |
|  ---  | ---  | --- | ---  |
|  1  |  table1_table2  | 1 | table1_table2  |
|      |    | 3  |  table2 |

#### 5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。

> 回答
不会增加查询速度。索引通常加到常用where条件。

#### 6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

- 请合理设计三张表的字段类型和表结构
- 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。