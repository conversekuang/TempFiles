

### decorator装饰器

#### 函数的核心概念

- **函数是一等公民，函数也可以是对象赋给变量**

  ```python
  def func(message):
      print('Got a message: {}'.format(message))
      
  send_message = func			#函数赋给变量
  send_message('hello world')
  
  # 输出
  Got a message: hello world
  ```

  

- **函数当做参数传入另一个函数**

  ```python
  def get_message(message):
      return 'Got a message: ' + message
  
  
  def root_call(func, message):
      print(func(message))
      
  root_call(get_message, 'hello world')		#函数当做参数传入
  
  # 输出
  Got a message: hello world
  ```



- **函数嵌套**

  ```python
  def func(message):
      def get_message(message):				
          print('Got a message: {}'.format(message))
      return get_message(message)				#执行还是函数
  
  func('hello world')
  
  # 输出
  Got a message: hello world
  ```

  

- **函数的返回值可以是函数对象（闭包）**

  ```python
  def func_closure():
      def get_message(message):
          print('Got a message: {}'.format(message))
      return get_message
  
  send_message = func_closure()
  send_message('hello world')
  
  # 输出
  Got a message: hello world
  ```

  

#### 装饰器

在不修改原来函数的情况下，额外加入其它功能。而该功能可以被多次复用。

- **简单装饰器**

  ```python
  def my_decorator(func):
      def wrapper():
          print('wrapper of decorator')
          func()
      return wrapper
  
  def greet():
      print('hello world')
  
  greet = my_decorator(greet)
  greet()
  
  # 输出
  wrapper of decorator
  hello world
  
  #或者可以采用
  @my_decorator
  def greet():
      print('hello world')
  
  greet()
  ```

  **变量greet**指向了内部函数wrapper()，先执行内部函数wrapper先调用greet函数。

  @是Python的语法糖，@my_decorator在函数之前，相当于执行`greet = my_decorator(greet)`。

- **带参数的装饰器**

  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print('wrapper of decorator')		
          func(*args, **kwargs)
      return wrapper
  ```

  

- **带自定义参数的装饰器**

  ```python
  def decorator_param(times):
      def my_decorator(func):
          def wrapper(*args, **kwargs):
              print('wrapper of decorator')
              for i in range(times):			#引入自定义参数来操作原函数
                  func(*args, **kwargs)
          return wrapper
      return my_decorator
  ```

  

- 通过@functools.wrap可以保留原函数的元信息。（也就是将原函数的原信息，拷贝到装饰器函数里）。其中原函数就是greet。

  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print('wrapper of decorator')
          func(*args, **kwargs)
      return wrapper
      
  @my_decorator
  def greet(message):
      print(message)
  
  greet.__name__
  
  # 输出
  'wrapper'
  
  #############################################################
  
  import functools
  
  def my_decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          print('wrapper of decorator')
          func(*args, **kwargs)
      return wrapper
      
  @my_decorator
  def greet(message):
      print(message)
  
  greet.__name__
  
  # 输出
  'greet'
  ```

  

- **类装饰器**

  类装饰器主要一类`__call__()`，每当调用一个类的示例，`__call__()`就会执行一次。

  ```python
  class Count:
<<<<<<< HEAD
      def __init__(self, func):					#初始化传入修饰的函数
          self.func = func
          self.num_calls = 0
  
      def __call__(self, *args, **kwargs):		#带入函数
=======
      def __init__(self, func):
          self.func = func
          self.num_calls = 0
  
      def __call__(self, *args, **kwargs):
>>>>>>> 1ab7f222a82343eb0bad24e5ddf8985d2a07c262
          self.num_calls += 1
          print('num of calls is: {}'.format(self.num_calls))
          return self.func(*args, **kwargs)
  
  @Count
  def example():
      print("hello world")
  
  example()
  
  # 输出
  num of calls is: 1
  hello world
  
  example()
  
  # 输出
  num of calls is: 2
  hello world
  ```

  会将修饰的函数example通过初始化进行传入count类，在执行example时候，会调用`__call__()`执行，而example的执行就是通过`__call__()`内调用的。

  

- 装饰器嵌套

  ```
  @decorator1
  @decorator2
  @decorator3
  def func():
      ...
  ```

  先执行最外层，依次向内执行。

  

#### 装饰器应用

- **身份认证**：在执行某个功能时，用户进行判断是否登录。可以将登录验证做成wapper对每个功能函数进行修饰，简化了每个函数都需要验证的复杂度。

- **日志记录**：需要得到每个函数的执行时间，在装饰器内记录执行实际函数的时间，并求差。
- **参数合理性检查**：在机器学习需要输入大量参数，需要对其进行检查，否则出现参数不对而做的无用功。
<<<<<<< HEAD
- **缓存**：python3中 from functools import rlu_cache， 可以通过@lru_cahche来缓存函数的结果 lru_cache(maxsize=128, typed=False)。maxsize参数定义缓存大小，而typed定义的是不同类型是否认为是不同结果。

=======
- **缓存**：python3中 from functools import rlu_cache， 可以通过@lru_cahche来缓存函数的结果 lru_cache(maxsize=128, typed=False)。maxsize参数定义缓存大小，而typed定义的是不同类型是否认为是不同结果。
>>>>>>> 1ab7f222a82343eb0bad24e5ddf8985d2a07c262
