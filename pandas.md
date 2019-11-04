



#### Series

- 初始化

1. 用list进行初始化:   Series([1,2,3])   index 默认是从0开始的数字
2. list与index:            Series([1,2,3]， index=['a','b','c'])  
3. dict进行初始化:     Series({'a':1,'b':2,'c':3}) 。则Series的index就是dict的key
4. dict与index进行初始化，Series({'a':1,'b':2,'c':3}, index=['b','c','d'])  显示index

```python
In [84]:  sdata = {'a':1,'b':3,'c':66}

In [85]: pd.Series(sdata,index=['b','c','d'])
Out[85]:
b     3.0
c    66.0
d     NaN
dtype: float64
```

- 检查NAN值( not a number)

  使用pd的方法：pd.isnull( Series实例) 或者 pd.notnull( Series实例)

  Series的方法：Series.isnull()  NA为True，其他为False；或 Series.notnull()

- Series自动对齐

  相同index的值会相加

  ```python
  In [89]: x = pd.Series({'a': 1, 'b': 3, 'c': 66},index=['b','c','d'])
  Out[90]:
  b     3.0
  c    66.0
  d     NaN
  dtype: float64
  
  In [91]: y = pd.Series([5,6,7],index=['b','d','c'])
  Out[92]:
  b    5
  d    6
  c    7
  dtype: int64
  
  In [100]: x+y
  Out[101]:
  b     8.0
  c    73.0
  d     NaN
  dtype: float64
  ```

- Series属性name与Series index 属性name

  ```python
  In [103]: x.name="new"
  In [104]: x.index.name="old"
  In [105]: x
  Out[105]:
  old
  b     3.0
  c    66.0
  d     NaN
  Name: new, dtype: float64
  ```

- 修改Series的index值

  ```python
  In [108]: x = pd.Series(sdata,index=['b','c','d'])
  In [109]: x.index=['one','two','three']
  In [110]: x
  Out[110]:
  one       3.0
  two      66.0
  three     NaN
  dtype: float64
  ```



#### DataFrame

- 初始化

  1. 通过等长列表或者Numpy数组组成。pd.DataFrame({'a':[1,3],'b':[4,6]}),key值为columns值。
  2. 带columns值

  ```
  In [111]: pd.DataFrame({'a':[1,3],'b':[4,6]}, columns=['b','a'])
  Out[111]:
     b  a
  0  4  1
  1  6  3
  ```

  3. 带colums值，以及index值

  ```python
  In [114]: m = pd.DataFrame({'a':[1,3],'b':[4,6]}, columns=['b','a'],index=['one','two'])
  In [114]:s
  Out[115]:
       b  a
  one  4  1
  two  6  3
  ```

  4. 嵌套字典

  ```python
  In [130]: data = {'a':{'one':1,'two':2},'b':{'one':1,'two':2}}
  In [131]: df = pd.DataFrame(data)
  In [132]: df
  Out[132]:
       a  b
  one  1  1
  two  2  2
  ```

  

- 属性

  1. m.columns 返回的是列值
  2. m.index      返回的是行值

  3. m['a']或者m.a           取出a列的所有值
  4. m.loc['two'] 或者 m.iloc['two']            取出two行的所有值

- 修改DataFrame

  1. 在原来的DataFrame上新增行或者列

     新增列:   m['c']=10，所有的index的’c‘列都是10

     新增列:	m['d'] = Series([11],index=['one'])

     新增行：m.loc['four']=[1,2,3]，增加index的话，则list长度与columns长度一致

  ```python
  In [117]: m.columns
  Out[117]: Index(['b', 'a'], dtype='object')
  
  In [118]: m.index
  Out[118]: Index(['one', 'two'], dtype='object')
  
  # 取列值
  In [119]: m.a
  Out[119]:
  one    1
  two    3
  Name: a, dtype: int64
  
  # 取行值
  In [121]: m.loc['two']
  Out[121]:
  b    6
  a    3
  Name: two, dtype: int64
  
  # 新增行
  In [127]: m.loc['four']=[1,2,3]
  In [128]: m
  Out[128]:
        b  a   c
  one   4  1  10
  two   6  3  10
  four  1  2   3
  
  # 新增列
  In [125]: m['c']=10
  In [126]: m
  Out[126]:
       b  a   c
  one  4  1  10
  two  6  3  10
  
  # 新增列
  In [134]: m['d'] = pd.Series([11],index=['one'])
  In [135]: m
  Out[135]:
        b  a   c     d
  one   4  1  10  11.0
  two   6  3  10   NaN
  four  1  2   3   NaN
  ```



#### 丢弃指定坐标轴上的项(删除行或列)

Series丢弃行数据，直接Series.drop(['one','two'])

DataFrame丢弃行数据 m.drop(['one','four'])

DataFrame丢弃列数据 m.drop(['a','d'], axis=1)

```python
In [148]: x
Out[148]:
one       3.0
two      66.0
three     NaN
dtype: float64

In [149]: x.drop(['one','two'])
Out[149]:
three   NaN
dtype: float64

In [143]: m
Out[143]:
      b  a   c     d
one   4  1  10  11.0
two   6  3  10   NaN
four  1  2   3   NaN

In [144]: m.drop(['one','four'])
Out[144]:
     b  a   c   d
two  6  3  10 NaN

In [145]: m.drop(['a','d'],axis=1)
Out[145]:
      b   c
one   4  10
two   6  10
four  1   3
```



#### Index索引对象

​	Index是不可修改的。返回的都是Index对象。

```
In [136]: m.columns
Out[136]: Index(['b', 'a', 'c', 'd'], dtype='object')

In [137]: m.index
Out[137]: Index(['one', 'two', 'four'], dtype='object')
```

​	修改columns或者index的索引

​	m.reindex(columns=['a','b','c','d'])

​	m.reindex(['one','two','three','four'])

```python
In [138]: m2= m.reindex(columns=['a','b','c','d'])
In [139]: m3 = m2.reindex(['one','two','three','four'])
In [140]: m3
Out[140]:
         a    b     c     d
one    1.0  4.0  10.0  11.0
two    3.0  6.0  10.0   NaN
three  NaN  NaN   NaN   NaN
four   2.0  1.0   3.0   NaN
```



