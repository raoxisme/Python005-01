## 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import math
import time
import random

def timer(func):
    def func_wrapper(*args,**kwargs):

        time_start = time.time()
        result = func(*args,**kwargs)
        time_end = time.time()

        time_delta = time_end - time_start
        print('function: {0} >> time cost: {1} s\n'.format(func.__name__, time_delta))

        return result
    return func_wrapper

@timer
def test():
    time.sleep( random.random() * 5)
    print("hello world!")

@timer
def test2( sleeptime, par1, par2):
    time.sleep( sleeptime)
    print( f"back from a {par1} sleep",  par2) 
    
if __name__ == "__main__":
    test()
    test2( random.random() * 10, 'good', par2 = '!')