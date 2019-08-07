



### flask引入静态资源（坑）

flask当有静态目录有多级时候，如何定位正确。



flask在`__init__()`时候，会自动默认static的路径。且不支持向上寻找。所以需要手动修改参数static_folder参数到最顶层，该文件的层级是相对于.py计算的，这样才能以此向下查找到各文件。



url_for()

<https://www.cnblogs.com/bayueman/p/6612104.html>



1. 在 Flask 中, HTML 的相对路径逻辑完全失效, 只能按照 Flask 的逻辑来走。
2. Flask 的逻辑是以 Flask.__init__() 中的 static_folder 参数为准。
3. static_folder 的路径是 相对于 启动文件 (本例中的 myproject/A/launch.py) 设置的. 也就是说默认情况下, 只有 myproject/A/static/ (本项目中未创建) 为虚拟资源的目录入口的. 所以这里我把 static_folder 设为 “…/” 就是为了能够让 Flask 以 myproject/ 为虚拟资源的入口。
4. 由于 static_folder 不允许向上查找路径 (这也就是为什么 HTML 中的 “…/…/…/” 居然都指向同一个值的原因), 也就是说 “…/…/…/…” 之类的父级路径符号, 都会被删除掉 — 可以变相地认为, 一旦 static_folder 设置了一个目录, 则该目录的所有上级目录的资源都将无法访问。

<https://blog.csdn.net/Likianta/article/details/89363973>









url_for 



<http://www.bubuko.com/infodetail-3099598.html>







url_for() ：只负责生成URL，如需跳转需要redirect

1. 在py脚本中，通过传入函数名来获得返回对应逻辑的url，

2. 在html文件中还可以用作加载静态文件，如

<link rel="stylesheet" href="{{url_for('static',filename='css/index.css')}}">

<https://blog.csdn.net/qq_39974381/article/details/80841140>





文件目录结构

```shell
IDE
|--new1
|	|--newstatic
|		|--hello.js
|--src
|	|--starter.py	
|--static
|	|--img
|	|--js
|		|--q.js
|--templates
|	|--login.html
```

- 若static_folder中设置入口为static文件夹，在模板html中既可以使用url_for( )，也可以使用xx/xx方式。

```python
app = Flask(__name__,
            static_folder='../static')  #若不加../，则默认在与starter.py文件的同一目录中寻找static
```

html引入静态资源

```html
<html>
   <head>
       <!--第一种方法用url_for()-->
      <script type = "text/javascript"
      src = "{{ url_for('static', filename='js/q.js') }} " ></script>
       <!--第二种方法用路径-->
      	<!--
		<script type = "text/javascript"
      	src = "/static/js/q.js" ></script>
		或者url可以写成
		src = "static/js/q.js" ></script>	
		-->
       
   	</head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

- 若static_folder中可以设置为任意名称的文件夹，则在模板html中只能使用src = “ /xx/x”。（目前实验尚不能得到url_for()中除static外其他的endpoint。。不知道为啥，那我就是想静态资源不交static文件夹难道不行咩？）

```python
app = Flask(__name__,
            static_folder='../new1')
```

html引入静态资源

```html
<html>
   <head>
      <script type = "text/javascript"
      src = "new1/newstatic/hello.js" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

static_folder默认是跟.py启动文件在同一目录下，若需要更改static_folder则加上（../）选择到需要的目录。