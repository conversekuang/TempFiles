



### OOP

传统的命令式语音有无数的重复性代码，函数的使用可以减少重复性工作，但是仍然不够。需要更加的抽象，也就是OOP的诞生。

- 类：具有相似性的事物的集合。具有向属性和函数的对象的集合。
- 对象：集合中的事物
- 属性：对象的某种静态特征
- 函数：对象的某种动态能力



```python
class Document():
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context # __ 开头的属性是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)

print(harry_potter_book.get_context_length())

print(harry_potter_book.__context)

########## 输出 ##########

init function called
Harry Potter
J. K. Rowling
77
10

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-b4d048d75003> in <module>()
     22 print(harry_potter_book.get_context_length())
     23 
---> 24 print(harry_potter_book.__context)

AttributeError: 'Document' object has no attribute '__context'

```

其中`__init__()`函数是初始化，两个下划线的属性是`__context`私有属性。私有属性只能通过类中定义的函数访问，通过getter和setter函数。



#### 成员函数，类函数，静态函数，

```python
class Document():
    
    WELCOME_STR = 'Welcome! The context for this book is {}.'
    
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
    
    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')
    
    # 成员函数
    def get_context_length(self):
        return len(self.__context)
    
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')


print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))

########## 输出 ##########

init function called
7
Welcome! The context for this book is indeed nothing.

```

- 类变量：该类的每个实例对象都可以访问的常量，也可以称作静态变量。
- 成员函数：就是常见的类中定义的函数

- 类函数：方法前面加上@classmethod声明。

  类函数的第一个参数是cls，必须传一个类进来。常用语实现不同的init构造函数。

```python
# 类函数
@classmethod
def create_empty_book(cls, title, author):
	return cls(title=title, author=author, context='nothing')
#因为；类函数传入cls，所以可以通过cls()来进行初始化。代码中相当于返回document()按参数初始化后的一个实例
```

- 静态函数：方法前面加上@staticmethod声明。

  

#### 继承

优势：减少重复代码，降低系统的复杂度。

- 构造函数：子类在生成对象时候需要**显示地在子类构造函数中调用父类的构造函数**。
- 重写：子类可以对父类中已经存在的函数进行重写

```python
class Spider():
    TOTAL = 0
    def __init__(self, *args, **kwargs):
        print ("Spider called")
        self.args = args
        self.TOTAL = 100

    def get_pipeline_length(self):
        raise Exception("need to be implemented")	#若父类方法需要子类重写可以引起异常，提醒子类来实现

class BigSpider(Spider):
    def __init__(self):
        super().__init__("a") 			#显示调用父类构造函数
        print("Big Spider called")

    def get_pipeline_length(self):		#重写父类方法。
        print(self.TOTAL)
```



#### 抽象类、抽象方法

与JAVA这点不一样，JAVA有abstract关键字对抽象类进行声明。而Python只能通过自行约束进行规范。

- 类本身没有什么用，不需要进行实例化，只是定义继承类中的一些基本元素。防止对该类进行实例化，需要将其设置为抽象类。有两种方式实现抽象类：

  1. 父类在方法中raise Exception()来提醒子类重写。

  2. 抽象类的实现需要继承abc包中的（Abstract Base Classes (ABCs)）ABCMeta。

     并且抽象方法需要@abstractmethod进行修饰

     子类必须对@abstractmethod进行修饰。

idea 提出 ---> 召开产品设计会（开发组、产品组） --->  产品需求文档（产品经理：PM）  --->  开发文档（项目经理：TL）。开发文档会定义模块功能和接口，每个模块之间如何协作，单元测试、集成测试，线上灰度测试、检测和日志等开发流程。--->  主要是对接口的定义。抽象类就是自上而下的设计风范，只需要少量代码描述清楚要做的事情，定义好接口，再由不同的开发人员去开发和对接。





https://mp.weixin.qq.com/s/Md8JYwDgOBci7cQMZ8uryw

```
class YuanRenXue:
"""A demo of class"""
    name = '猿人学'
def say_hi(self):
        print('Hello world!')

yrx = YuanRenXue()
yrx.say_hi
YuanRenXue.say_hi

yrx.say_hi   
# 等价于
YuanRenXue.say_hi(yrx)
```

`yrx.say_hi`与`YuanRenXue.say_hi`并不是一回事，它是一个方法对象，不是函数对象，通俗讲，前者是实例的方法，后者是类的函数。

