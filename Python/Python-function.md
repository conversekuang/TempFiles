



### function



#### 函数

注意：

- Python函数的参数可以设置默认值，有参数传入可以覆盖；无参数传入可以采用默认值。

- Python对参数类型并没有要求，只交给具体的代码去判断。因此，实际中可以加入数据类型的判断。

  

#### 嵌套

嵌套的优点：

- 除了outer函数可以调用inner函数之外，其他函数无法调用inner函数。具有保护隐私的作用。
- 合理使用嵌套能够提高运行效率。



#### 变量的作用域

- 局部变量：只在函数内有效，一旦执行完就进行回收，无法访问

- 全局变量：在整个文件的层次之上

若局部变量与全局变量的变量名称一致，若无global 声明，函数内变量仍然是局部变量。若想在函数中使用全局变量需要通过global进行声明。

```python
MAX = 0
def func():
    MAX = 0
    MAX += 2
    print("MAX = {}".format(MAX))
func()
print("MAX = {}".format(MAX))

#results 
MAX = 2
MAX = 0

MAX = 0
def func():
    global MAX
    MAX += 2
    print("MAX = {}".format(MAX))
func()
print("MAX = {}".format(MAX))

#results 
MAX = 2
MAX = 2
```



- 当嵌套时，inner函数需要使用outer函数中的变量，可以采用nonlocal关键字的声明方式对变量进行声明，此时inner函数可以对outer函数中的变量进行修改。
- inner函数使用全局变量同样需要通过global声明
- outer函数中global MAX后，inner通过noncal MAX并不能获取全局变量。会报错：MAX未声明。nonlocal只能用于outer函数中使用的变量。

```python
MAX = 0
def outer():
    global MAX
    max = 1
    MAX += 3
    print("MAX value = {}".format(MAX))
    def inner():
        nonlocal max
        max += 2
        print("max value = {}".format(max))
    inner()
```



而当变量指向的是可变对象的时候，如[], {}时候，可以不需要global进行声明，直接在函数内使用。

