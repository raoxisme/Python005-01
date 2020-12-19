import redis   # 导入redis 模块
import time

redis_HOST = '192.168.3.83' #'localhost'
WAIT_TIME = 60 #等待时间，测试设置为60秒

client = redis.Redis(host=redis_HOST, port=6379, decode_responses=True)  

def sendsms(telephone_number: int, content: str, key=None, wait_time = WAIT_TIME):
    # 短信发送逻辑, 作业中可以使用 print 来代替
    # pass
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    if len( client.keys( "%s_*" % telephone_number )) > 5:
        print('1 分钟后重试稍后')
        return
    
    
    currentTime = int(time.time())
    client.setex("%s_%s" % (telephone_number , currentTime), wait_time, currentTime)

    print("发送成功:" , content)

if __name__ == '__main__':
    sendsms(12345654321, content="phone 1, OK") # 发送成功  -1
    time.sleep(1)
    sendsms(12345654321, content="phone 1, OK") # 发送成功  -2
    time.sleep(1)
    sendsms(12345654321, content="phone 1, OK") # 发送成功  -3 
    time.sleep(1)
    sendsms(12345654321, content="phone 1, OK") # 发送成功  -4
    time.sleep(1)
    sendsms(12345654321, content="phone 1, OK") # 发送成功  -5
    time.sleep(1) 
    sendsms(88887777666, content="phone 2, OK") # 发送成功  -1
    sendsms(12345654321, content="phone 1, Fail") # 1 分钟内发送次数超过 5 次, 请等待 60 秒  发送失败  -1
    time.sleep(30) 
    sendsms(12345654321, content="phone 1, Fail") # 发送失败  -2
    time.sleep(30) 
    sendsms(12345654321, content="phone 1, OK") # 发送成功
