学习笔记

## Redis 
让Redis服务器被远程访问:  
默认情况下，Redis服务器不允许远程访问，只允许本机访问，所以我们需要设置打开远程访问的功能。

用vi打开Redis服务器的配置文件redis.conf
### windows安装  
https://www.cnblogs.com/liuqingzheng/p/9831331.html

### Ubuntu16.04安装Redis
https://www.cnblogs.com/zongfa/p/7808807.html

### python lib
pip3 install --upgrade redis -i https://pypi.douban.com/simple  
https://www.runoob.com/w3cnote/python-redis-intro.html


## 作业一：使用 Python+redis 实现高并发的计数器功能
需求描述:  
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。  
函数说明:  

counter 函数为统计视频播放次数的函数，每调用一次，播放次数 +1  
参数 video_id 每个视频的 id，全局唯一  
基于 redis 实现自增操作，确保线程安全  
期望执行结果：    
conuter(1001) # 返回 1  
conuter(1001) # 返回 2  
conuter(1002) # 返回 1    
conuter(1001) # 返回 3  
conuter(1002) # 返回 2  

代码文件：   
> python3 .\counter.py


## 作业二：在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
已知有如下函数：  
def sendsms(telephone_number: int, content: string, key=None)：
    # 短信发送逻辑, 作业中可以使用 print 来代替
    pass
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    pass
    print("发送成功")
期望执行结果：  

sendsms(12345654321, content=“hello”) # 发送成功  
sendsms(12345654321, content=“hello”) # 发送成功  
…  
sendsms(88887777666, content=“hello”) # 发送成功  
sendsms(12345654321, content=“hello”) # 1 分钟内发送次数超过 5 次, 请等待 1 分钟  
sendsms(88887777666, content=“hello”) # 发送成功  

tips:
flushall, keys 88887777666_*

代码文件： 
> python3 .\sendsms.py



## 作业三：请用自己的语言描述如下问题：

- 在你目前的工作场景中，哪个业务适合使用 rabbitmq？ 引入 rabbitmq 主要解决什么问题?（非相关工作可以以设计淘宝购物和结账功能为例来描述）  
企业跨系统集成，订阅源系统事件，如各种workflow。rabbitmq解决消息队列问题。

- 如何避免消息重复投递或重复消费？ 
重复投递： 消费端实现幂等性： 即消费端永远不会消费多次，即使收到了多条一样的消息。  

- 交换机 fanout、direct、topic 有什么区别？  
direct： 生产者/消费者 = 1：1
fanout: 生产者/消费者 = 1：N
topic: 生产者/消费者 消息按类型分发

- 架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？ 

（1）服务间异步通信： 
（2）顺序消费  
（3）定时任务  
（4）流量削峰  
（5）解耦  
（6）利用消息队列将高并发访问变为串行操作  
（7）异步下单  
（8）消息队列持久化  

优点：  
　　解耦、异步、削峰  
缺点：   
　　系统可用性降低、复杂度变高、一致性问题  