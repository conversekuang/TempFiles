### try-except



错误：

- 语法错误：书写代码过程中的语法错误，不符合python的编程规范。

- 逻辑错误：代码正常，但是实现结果与预期不符。

异常：

- 系统异常

  介绍一下完整的异常处理流程

```
try:
    pass
except expression as identifier:
    pass
else:
    pass
finally:
    pass
```

其中，try后跟着可能出现异常的语句，而except对异常的捕捉，可以罗列出具体的异常类型。若不清楚相应的异常类型，可以把异常类型写为Exception，作为所有异常的基类，均可以捕捉到。或者在具体异常之后直接写except：即可。如下的方式一和二中的表达。

其次，若无异常出现，则执行else中的语句。

最后，无论是否出现异常，finally语句总是执行的。



方式一

```python
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')
print('continue')
```

或者方式二

```python
try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error')
print('continue')
```



- 自定义异常

  个人认为主要出现在业务逻辑判断中，可以把它当做一个异常抛出进行处理。

  注意的是需要继承Exception作为父类。

```python
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常类型的初始化
        self.value = value
    def __str__(self): # 自定义异常类型的 string 表达形式
        return ("{} is invalid input".format(repr(self.value)))
    
try:
    raise MyInputError(1) # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))
```



#### 异常使用的场景：

- 在可能出现错误的、或者不成功的代码块中
- 不能滥用异常处理，对于流程控制的代码，如if能解决的，不需要try-catch块。





思考题：

哪种方式更好？

方式一：

```python
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
except (DBConnectionError, DBQueryDataError) as err:
    print('Error: {}'.format(err))
```

方式二：

```python
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    try:
        raw_data = DB.queryData('<viewer_id>')
    except DBQueryDataError as err:
         print('DB query data error: {}'.format(err))
except DBConnectionError as err:
     print('DB connection error: {}'.format(err))
```



**方式二更好**。因为更简洁，不需要嵌套，抛出的异常外城还是会捕捉。结果和方式一一样的。



![img](https://static001.geekbang.org/resource/image/48/6e/48c46d4a66e5c002ce392d79deee436e.png)

会看到这么一句话”When an exception has been assigned using as traget, it is cleared at the end of the except clause."相当于异常赋给一个变量，改变量会在except block 执行结束时被删除。

```python
e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    try:
        pass
    finally:
        del e
print(e)
NameError: name 'e' is not defined
```

所以最后print(e)会显示名称错误。

