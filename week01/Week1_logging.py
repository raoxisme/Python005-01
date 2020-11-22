#编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
import logging
import time
from pathlib import Path
import os

def print_log():
    logging.warning('warning message')

if os.path.exists( './var/log/python' ) != True:
    os.makedirs('./var/log/python') 


str_today = time.strftime("%Y%m%d",  time.localtime())

logging.basicConfig(filename= './var/log/python/' + str_today + '.log',
                    level=logging.WARN,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')

if __name__ == '__main__':
    print_log()