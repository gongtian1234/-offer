# 实现Singleton模式
## 设计一个类，只能生成该类的一个实例

############################################方法一：模块单例############################################
'''
python中的模块module在程序中只被加载一次，本身就是单例的。可以直接写一个模块，将你需要
的方法和属性，写在模块中当做函数和模块作用域的全局变量即可，根本不需要写类。 
'''
# foo1.py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()

# foo.py
from foo1 import singleton
singleton.foo()

############################################方法二：静态变量方法############################################
'''
实现__new__方法,然后将类的一个实例绑定到类变量_instance上
如果cls._instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls._instance不是None, 直接返回_instance
'''

class Singleton1(object):
    def __new__(cls, *args, **kwargs):    # *arg会把多余传入的参数转为数组，**kwargs会把a=1这种的转为字典
        if not hasattr(cls, '_instance'):
            orig = super(Singleton1, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton1):
    a = 1

one = MyClass()
two = MyClass()
print(id(one))    # 943663826424
print(id(two))    # 943663826424
print(one==two)    # True

############################################方法三: 使用装饰器############################################



def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MyClass3(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass3()
two = MyClass3()
two.x = 3
print(one.x)    # 3
print(id(one))    # 249905912128
print(id(two))    # 249905912128

