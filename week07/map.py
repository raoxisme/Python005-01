## 自定义一个 python 函数，实现 map() 函数的功能。
class map:
    
    def __init__(self,func,*args):
        self.iterators = args
        self.func = func
 
    def __iter__(self):
        return self.generator()
 
    def generator(self):
        iterators, func= self.iterators, self.func
        try:
            i = 0
            while 1:
                yield func(*[j[i] for j in iterators])
                i += 1
        except IndexError:
            pass

if __name__ == "__main__":
    func = lambda x,y,z,w: x == y

    a = [1, 2, 44, 4, 5,  6, 7, 8, 9]
    b = [1, 2, 3,  4, 11, 6, 7, 8, 9]

    print(list(map(func,a,b,a,b)))
    print(list(map(func,a,a,a,a)))