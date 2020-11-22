VSCode: 插件
Rainbow Fart

虚拟环境：在系统同时维护多个python项目的环境，并灵活切换；或测试自己程序的不同版本；或生产/开发环境
创建 python3 -m venv venv1
激活 source venv1/bin/activate
- 退出 deactivate
- 查看第三方库版本 pip3 freeze > requirement.txt

环境迁移: 如开发环境引入了第三方库，导入到生产环境
- 查看python版本
- 查看pip版本
- pip install -r ./requirement.txt
- pip3 freeze查看是否和迁移前环境一致

基础数据类型
判断None是否相等： IS
其他，例如int是否相等： ==， ！=
帮助 help(deque)

模块：main.py 引用 short.py，不希望short.py的函数被执行，那么可以使用dander name变量__name__
if __name__ == '__main__':
    short_func();