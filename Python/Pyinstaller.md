Pyinstaller 打包文件生成exe时出现问题



在程序打包将.py文件转换成exe的时候，会出现闪退的现象。

在IDE与sublime中完全可以正常执行。可以在命令行中运行时，可以直接查看报错信息。只要在命令行中运行没有错误，即可双击exe。



1. 路径问题

```python
# 有问题的
def write_to_file():
	name = input("name:")
	with open("content.txt", 'w') as f:
		for filename in os.listdir(os.path.abspath(__file__)):
			f.write(filename+'\n')
            
# 报错
Traceback (most recent call last):
  File "get1.py", line 15, in <module>
    write_to_file()
  File "get1.py", line 11, in write_to_file
    for filename in os.listdir(os.path.dirname(__file__)):
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: ''
```

不建议使用`os.path.abspath(__file__)`的方式，而采用`os.path.dirname(os.path.abspath(__file__))`的方式代替。

```python
# 能正常打包的            
def write_to_file():
	name = input("name:")
	with open("content.txt", 'w') as f:
		for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
			f.write(filename+'\n')
```



<https://blog.csdn.net/qq562029186/article/details/81479939>

2. 多线程可以直接打包

   可直接调试。

3. 带icon标志的exe文件

pyinstaller -D E:\Python_project\IDE\nanhu_pdf_download\main.py -i E:\Python_project\IDE\nanhu_pdf_download\icon.ico





Pyinstaller是3.5

https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing





#### pyinstaller的库导入和多进程打包问题

https://blog.csdn.net/xiong_big/article/details/54614231



https://github.com/pyinstaller/pyinstaller/wiki  手册

https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing pyinstaller的相关问题

https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support `multiprocessing.freeze_support`()的介绍

windows中多进程需要加上这个`multiprocessing.freeze_support`()。否则会不断生成新的进程导致内存耗尽。但是在linux或者unix中加不加这个没有影响。

concurrent.futures.ProcessPoolExecutor() 中也是利用到multi.processing 模块，所以需要再一开始加该函数。