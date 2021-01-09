作业一：

## 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：  

list
tuple
str
dict
collections.deque

容器序列: list, tuple, dict, collections.deque --> 容器序列存在深拷贝、浅拷贝问题
扁平序列: str

可变序列: list, dict, collections.deque  
不可变序列: tuple, str  

## 作业二：
自定义一个 python 函数，实现 map() 函数的功能。
>> 见map.py

## 作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
>> timer.py