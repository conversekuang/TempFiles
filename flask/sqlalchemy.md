



基本的sqlalchemy映射列类型.配置选项和关系选项

https://blog.csdn.net/lin06051180/article/details/76440629





SQLAlchemy 反射已有表

https://segmentfault.com/a/1190000007835255

https://blog.csdn.net/xie_0723/article/details/84901502







https://blog.csdn.net/weixin_41935140/article/details/90606330

在Python中，常用的ORM框架是SQLAlchemy。在ORM操作中，每个数据库表都有对应的class，数据库表的行与相应的对象建立关联，互相转换。而实际应用中，我们常常操作那些已经存储数据的数据库表，如果一一建立class及对应关系，会很麻烦，所以我们如何直接获取对象并操作呢？



```python
"""sqlalchemy 操作oracle数据库示例"""
 
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import Session
 
metadata = MetaData()
# echo 参数用于标记是否输出日志信息
engine = create_engine( 'oracle+cx_oracle://user:password@addr/sid', echo = True)
session = Session(engine)
 
# 获取指定数据库表对象
ex_table = Table('数据库中表名', metadata, autoload=True, autoload_with=engine)
 
# 插入数据
ret = session.execute(ex_table.insert(), {"字段名": "值","":""...})
session.commit()
 
# 查询数据返回第一条
res = session.query(ex_table).first()
print(res)
```







Session 和 sessionmaker的区别

*class* `sqlalchemy.orm.session.``sessionmaker`(*bind=None*, *class_=<class 'sqlalchemy.orm.session.Session'>*, *autoflush=True*, *autocommit=False*, *expire_on_commit=True*, *info=None*, ***kw*)[¶](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.session.sessionmaker)



*class* `sqlalchemy.orm.session.``Session`(*bind=None*, *autoflush=True*, *expire_on_commit=True*, *_enable_transaction_accounting=True*, *autocommit=False*, *twophase=False*, *weak_identity_map=None*, *binds=None*, *extension=None*, *enable_baked_queries=True*, *info=None*, *query_cls=None*)



sessionmaker是Session工厂：这个 [`sessionmaker`](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.session.sessionmaker) 工厂产生新的 [`Session`](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.session.Session) 当调用对象时，根据此处建立的配置参数创建它们。使用的时候还需要进一步的实例化。

Session 





三种执行execute的方式

1. engine.execute()

2. conn = engine.connect()

   con.execute()

3. session.execute()



engine.execute()  方式查看源码其实就是通过connection来执行的，相当于Connection.execute

参考文章：

- [github中关于三种方式的回答](https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference)

- [关于engine, connect, session](http://sunnyingit.github.io/book/section_python/SQLalchemy-engine.html)



session中execute与query方法的使用:

`execute`(*clause*, *params=None*, *mapper=None*, *bind=None*, ***kw*)[¶](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.session.Session.execute)

`query`(**entities*, ***kwargs*)[¶](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.session.Session.query)

```python
# 数据库中已有的表但是创建对应的class文件太麻烦，可以通过映射的方法加载已有表生成对应的Table类，
# 通过ex_table.columns.column 来指定相应的字段
engine = create_engine("mysql+pymysql://root:password@localhost/busline", encoding='utf-8', echo=True)
session = Session()
ex_table = Table('yzbusline', metadata, autoload=True)
# 这个existing_table 就是Table类，后面的用法一样

res = session.execute(ex_table.select().where(ex_table.columns.busNumber == '辅63')).fetchall()
# 利用execute方法

res = session.query(ex_table).filter(ex_table.columns.busNumber == '辅63').all()
# 利用query方法

print(res)
```





以下三种方式等价：

Query.with_session()

- 当一个查询语句需要用在多个session中时，Query固定时候，可以指定多个session中去执行

some_session.query(User, Address)

- 在某个session上执行query语句

Query([User, Address], session=some_session)

- 查询语句直接指定某个session

```python
from sqlalchemy.orm import Query
query = Query([MyClass]).filter(MyClass.id == 5)
result = query.with_session(my_session).one()
```



sqlalchemy的  **orm样式/经典样式**  **创建表/反射存在的表**

https://blog.csdn.net/lilied001/article/details/81430260









