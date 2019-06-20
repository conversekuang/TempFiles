

## set 和dict

之前的tuple和list是有序的，而set集合与dict字典均是无序的，因此，不能通过下表索引方式进行操作。



字典（dict）：是一系列由键（key）和值（value）配对组成的元素的集合。在Python3.7之后，字典被确定是有序的，3.6版本之前是无序的。字典的适合查找，添加、删除操作，都能够在常数时间内完成。

集合（set）：是一系列无序的，唯一的元素组合。

dict字典中的key也可以是不同类型的，value也同样存储不同类型。set集合中可以存储不同类型的元素。均可以是混合类型。



**常用函数**：

```python
#set的常用函数
>>> dir({1,2})    
['...', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#dict的常用函数
>>> dir({1:2})    
['...', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```



#### **set**

- **创建**

```shell
>>> s1 = set([1,2,3])  #通过函数set初始化集合
>>> s1
set([1, 2, 3])

>>> s2 = {1,2,3}       #初始化
>>> s2
set([1, 2, 3])

>>> s1 == s2
True

>>> s3 = set()         #创建空集合,此时不能用{}进行初始化，否则被认为是dict类型
>>> s3
set([])
#以上是在python 2.7中的表示方式，但是在3.x版本中，显示的是{xxx}代替set([xx])表示方式。
```

- **查询**

<font color="red">集合不支持索引，因为集合的本质是哈希表，和列表不一样。</font>

因为set是集合，因此只能用  in  / not in 的方式来查询元素是否在集合中

```shell
>>> 3 in s1
True
>>> 4 not in s2
True
```

- **插入、删除**

```shell
>>> s1.add(100)             #插入元素
>>> s1.add(5)
>>> s1
set([1, 2, 3, 100, 5])    
>>> s1.pop()                #不是按照添加顺序进行的弹出的，因此该操作有风险
1
>>> s1
set([2, 3, 100, 5])         
>>> s1.remove(100)          #移除，对给定值进行删除
>>> s1
set([2, 3, 5])
```

- **排序**

```python
>>> s = {3, 4, 2, 1}
>>> sorted(s) 		# 对集合的元素进行升序排序
[1, 2, 3, 4]
```



#### **dict**

- **创建**

```shell
>>> d1 = {}          #初始化空字典
>>> d1
{}
>>> d2 = dict()      #初始化空字典
>>> d2
{}

#dict初始化
>>> d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
>>> d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
>>> d4 = dict(name='jason', age=20, gender='male') 
>>> d1 == d2 == d3 ==d4
>>> True
```

- **查询**
  - 通过索引键值的方式来访问字典，若键值不存在则会抛出异常。
  - 通过get(key, default)方法来获取键值。不存在默认返回None，可以设置其他默认返回值。

```shell
>>> d1['name']
'jason'
>>> d['location']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'location'

>>> d1.get('name')
'jason'
>>> print(d1.get('location'))
None
>>> print(a.get('location', 'no such'))
no such
```

- **插入、更新、删除**

```shell
>>>d = {'name': 'jason', 'age': 20}
>>>d['gender'] = 'male' 		# 增加元素对'gender': 'male'
>>>d['dob'] = '1999-02-01' 	# 增加元素对'dob': '1999-02-01'
>>>d
{'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}

>>>d['dob'] = '1998-01-01' # 更新键'dob'对应的值 
>>>d.pop('dob') # 删除键为'dob'的元素对
'1998-01-01'
>>>d
{'name': 'jason', 'age': 20, 'gender': 'male'}

#插入有序性：
1. double star
>>> d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
>>> d2 = {'hobby': 'swim', **d1}
>>> d2
{'hobby': 'swim', 'name': 'jason', 'age': 20, 'gender': 'male'}

2. update 函数：
>>> d3 = {'hobby': 'swim'}
>>> d3.update(d1)
>>> d3
{'hobby': 'swim', 'name': 'jason', 'age': 20, 'gender': 'male'}
```

- **排序**（按照键排序、按照值排序）

```python
>>>d = {'b': 1, 'a': 2, 'c': 10}

# 根据字典键的升序排序
>>>d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) 
>>>d_sorted_by_key
[('a', 2), ('b', 1), ('c', 10)]

# 根据字典值的升序排序
>>>d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) 
>>>d_sorted_by_value
[('b', 1), ('a', 2), ('c', 10)]
```

#### 场景

- 当有大量的重复数据，需要得到去重后的数据
  - 当数据只有一个字段，而且字段之间没有对应关系时，可以通过set进行去重。
  - 当数据有多个字段而且需要进行联动时，可以采用dict进行去重。

- dict查找的高效性，根据给定key可以快速进行查找其对应的value。

#### 工作原理

- 对于字典而言，这张表存储了哈希值，键，值：3个元素
- 对于集合而言，这张表存储只有单一的元素值。

```python
老版本的Python哈希结构：
--+-------------------------------+
  | 哈希值 (hash)  键 (key)  值 (value)
--+-------------------------------+
0 |    hash0      key0    value0
--+-------------------------------+
1 |    hash1      key1    value1
--+-------------------------------+
2 |    hash2      key2    value2
--+-------------------------------+
. |           ...
__+_______________________________+
```

由于该hash结构是over-located array。

```python
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}
```

这个字典的存储类似如下：

```
entries = [
['--', '--', '--']
[-230273521, 'dob', '1999-01-01'],
['--', '--', '--'],
['--', '--', '--'],
[1231236123, 'name', 'mike'],
['--', '--', '--'],
[9371539127, 'gender', 'male']
]
```

'---'代表该位置没有元素但是已经分配了空间，而当哈希表剩余空间小于1/3时，会重新分配更大的空间，所以哈希表中的元素越来越多时候，分配了内存但是没有元素的位置也越来越多。最后变得稀疏。

















