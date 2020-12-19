import redis   # 导入redis 模块

redis_HOST = '192.168.3.83' #'localhost'

client = redis.Redis(host=redis_HOST, port=6379, decode_responses=True)  

def counter(video_id):
    # client.set('video_id', 'runoob')  # 设置 name 对应的值

    client.incr(video_id)

    current_cnt = client.get(video_id)

    print(current_cnt)

if __name__ == '__main__':
    counter(1001) # 返回 1  
    counter(1001) # 返回 2  
    counter(1002) # 返回 1    
    counter(1001) # 返回 3  
    counter(1002) # 返回 2  