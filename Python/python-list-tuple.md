## list 和 tuple

**本次补充新添加到blog中**

list是列表

tuple是元组



**常用函数**：

- 可以通过dir()来查看对象或者类的常用方法和属性

```python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
>>> dir(())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

- tuple和list都有的：

  list/tuple.index(item)  				item在list/tuple中第一次出现的下标

  list/tuple.count(item) 				 item在list/tuple中出现的次数统计

  reversed()  									list/tuple翻转

  sorted()       								   list/tuple排序，**生成新list/tuple**。（排序只能限于list中是同类型元素）

- 仅list有的函数

  list.reverse()      							 将list原地分别表示**原地**倒转列表

  list.sort()         							    将list原地分别表示**原地**排序（排序只能限于list中是同类型元素）

- sorted()或者arr.sort()：排序要么元素全是str，要么全是int。不能相混。

```python
a = ['a','1','0']
print (a.index('0'))
print (a.count('1'))
a.sort()
print (a)
a.reverse()
print (a)

#results
2
1
['0', '1', 'a']
['a', '1', '0']
```



**相互转换**：

L1 = list( t1 )   #元组转换列表

t1 = tuple(L1)  #列表转换元组



**异同**：

- **相同点**：.
  - list 和 tuple 都可以在同一个list或tuple中**存储任意类型有序集合**。
  - **允许重复**元素的出现
  - 因为是有序集合，可以通过**下标索引**进行查找元素
    -  a[1], 同样支持负数索引，表示从末尾开始访问a[-1]
  - 支持切片操作：
    - a[1:3], a[1:-2:2]从下标为1的数到倒数第2个数，步进为2。
  - 可以随意嵌套：
    - 列表嵌套列表：本质是列表，内部列表和外部列表的内容可以进行修改元素，插入，删除元素。也就是二维数组。
    - 列表嵌套元组：本质是列表，所以可以对列表中除元组外的其他元素可以修改插入、删除。但元组中的内容不可以改变。
    - 元组嵌套列表：本质是元组，元组中的任何元素不能进行改变，但是对于元素本身是列表的情况，可以对列表中的值进行修改。这是因为：列表对象是不变的，只是的列表中的内容进行变化。列表本来就是动态的。
    - 元组嵌套元组：本质元组，元组中的元素还是元组。所以这种情况下，不能进行任何改变。也就是不可变的二维数组。

>>> ```shell
>>> 
>>> #数组嵌套元组
>>> >>> a = [(1,2),(3,4)]
>>> >>> a
>>> [(1, 2), (3, 4)]
>>> 
>>> #修改a中元素
>>> >>> a.append('abc')
>>> >>> a
>>> [(1, 2), (3, 4), 'abc']
>>> 
>>> #数组a中元组
>>> >>> a[0][0]='x'
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> TypeError: 'tuple' object does not support item assignment
>>> 
>>> #元组b嵌套数组
>>> >>> b = ([1,2,3],"456")
>>> >>> b
>>> ([1, 2, 3], '456')
>>> 
>>> #修改元组b中数组
>>> >>> b[0].append(100)
>>> ([1, 2, 3, 100], '456')
>>> ```
>>

- **不同点**：
  - **list**
    - 是动态的，长度不固定，进行删除，插入，修改操作
    - 自动进行扩容
    - 适合存储动态数据
  - **tuple**
    - 静态的，长度固定。不能够修改元组内的数据，不能进行删除和插入操作
    - 无法扩容，会根据tuple大小进行分配空间
    - 适合存储静态数据和历史数据，不会进行修改删除等操作



```python
>>> a = []
>>> a.__sizeof__()
40
>>> b = ()
>>> b.__sizeof__()
24
```

从空列表和空元组的内存分配上来看，

