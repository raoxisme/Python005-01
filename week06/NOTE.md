学习笔记
## 作业
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
这个类可以使用如下形式为动物园增加一只猫：
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')

具体要求：
- 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
- 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
- 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
- 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

## 类
### 作用域：
• _name 人为约定不可修改   
• __name 私有属性   
• __name__ 魔术方法   
魔术方法：   
• 双下划线开头和结尾的方法，实现了类的特殊成员，这类称作魔术方法   
• 不是所有的双下划线开头和结尾的方法都是魔术方法   
• 魔术方法类似其他语言的接口   
私有属性是可以访问到的，Python 通过改名机制隐藏了变量名称   
• class.__dict__  

### 类方法：
三种方法：  
• 普通方法 至少一个 self 参数，表示该方法的对象  
• 类方法 至少一个 cls 参数，表示该方法的类  
• 静态方法 由类调用，无参数  
三种方法在内存中都归属于类  
  
### 特殊属性与方法
__init__()  
• __init__() 方法所做的工作是在类的对象创建好之后进行变量的初始化。  
• __init__() 方法不需要显式返回，默认为 None，否则会在运行时抛出 TypeError   

self  
• self 表示实例对象本身
• self 不是 Python 的关键字（cls也不是），可以将 self 替换成任何你喜欢的名称,如 this、obj 等，实际效果和 self 是一样的（不推荐）。  
• 在方法声明时，需要定义 self 作为第一个参数，调用方法的时候不用传入 self  

## 新式类
object 和 type 的关系  
• object 和 type 都属于 type 类 (class 'type')  
• type 类由 type 元类自身创建的。object 类是由元类 type 创建  
• object 的父类为空，没有继承任何类  
• type 的父类为 object 类 (class 'object')  
