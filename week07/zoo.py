# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
from abc import ABCMeta, abstractmethod
#类型
SPEC_MEAT = 1
SPEC_NONMEAT = 2

#体型
SHAPE_SMALL = 1
SHAPE_MEDIUM = 2
SHAPE_BIG = 3 

#性格
NATURE_FEROCIOUS = 1
NATURE_NOT_FEROCIOUS = 2

class Animal(object):
    """Class Animal"""

    is_ferocious_animal = False

    @abstractmethod
    def __init__(self, spec_int, shape_int, nature_int):
        """Animal __str__"""
        self._spec = spec_int
        self._shape = shape_int
        self._nature = nature_int

        if self._shape >= SHAPE_MEDIUM and self._spec == SPEC_MEAT and self._nature == NATURE_FEROCIOUS:
            self.is_ferocious_animal = True

    def __str__(self):
        """__str__"""
        return "nature: {} spec: {} shape {}".format(self._nature, self._spec, self._shape)

    def __getattribute__(self,item):
        if item == 'is_ferocious_animal' and self._shape >= SHAPE_MEDIUM and self._spec == SPEC_MEAT and self._nature == NATURE_FEROCIOUS:
            self.is_ferocious_animal = True
        return super().__getattribute__(item)

class HouseCat(Animal):
    """Class HouseCat"""
    voice = 'mmu'
    is_pet = True
    name = ''

    def __init__(self, shape_int, name_str):
        """HouseCat __str__"""
        self.name = name_str
        super().__init__(SPEC_MEAT, shape_int, NATURE_NOT_FEROCIOUS )

    def __str__(self):
        """__str__"""
        return "nature: {} spec: {} shape {} voice: {}".format(self._nature, self._spec, self._shape, self.voice)

class Dog(Animal):
    """Class Dog"""

    voice = 'wang'
    is_pet = True
    name = ''

    def __init__(self, shape_int, name_str):
        """HouseCat __str__"""
        self.name = name_str
        super().__init__(SPEC_MEAT, shape_int, NATURE_FEROCIOUS )

    def __str__(self):
        """__str__"""
        return "nature: {} spec: {} shape {} voice: {}".format(self._nature, self._spec, self._shape, self.voice)

class Zoo(object):
    animals = []
    def __init__(self, name):
        self.name = name

    @classmethod
    def add_animal(self, animal):
        for i in self.animals:
            if id(animal) == id(i):
                print( animal, ' in zoo already')
                return
                
        print( animal, ' added to zoo')
        self.animals.append(animal)

if __name__ == "__main__":
    dog_a = Dog(SHAPE_BIG, 'Adam')
    cat_a = HouseCat(SHAPE_SMALL, 'Gua')

    Zoo.add_animal(dog_a)
    Zoo.add_animal(cat_a)

    print( cat_a )
    print( dog_a )
    print( cat_a.is_ferocious_animal )
    print( dog_a.is_ferocious_animal )

    
    Zoo.add_animal(dog_a) #测试重复加入

    dog_b = Dog(SHAPE_BIG, 'Baji')
    Zoo.add_animal(dog_b) #测试重复加入