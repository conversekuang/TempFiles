

### Win10 安装tesserocr

验证码识别：

tesseract是hp公司研发，最后开源的识别技术。

tesserocr是python的一个 OCR 识别库，其实是对tesseract的一层python API封装，它的核心是tesseract。



因此需要先安装tesseract， 再安装tesserocr。

- 安装tesseract

github上

<https://github.com/tesseract-ocr/tesseract>

tesseract本身无windows的安装包，但是指定了一个第三方的windows安装包，

<https://digi.bib.uni-mannheim.de/tesseract/>

选择版本其中，dev对应的是开发版本，不带dev的是稳定版本。



- 安装tesserocr

**采坑**：

安装的时候采用pip3 install tesserocr。结果报错需要MVS c++ 14.0版本，通过<https://www.jianshu.com/p/7b24274c569a> 下载C++编译工具。

又报错找不到文件：

**Failed** **to** **extract** **tesseract** **version** **from** **executable****:** **[****WinError** **2****]** **系统找不到指定的文件。**

根据解决方法：

<https://www.biaodianfu.com/windows-install-tesserocr.html>

看到最好的方式是通过.whl文件进行安装



tesserocr的安装地址为：

<https://github.com/simonflueckiger/tesserocr-windows_build/releases>



pip3 install  xx.whl 安装成功

whl文件: (https://pan.baidu.com/s/1BTcPdVkyHJOAZIPIh2gJ2A)

运行代码：

```python
import tesserocr
from PIL import Image

image = Image.open('image.png')
result = tesserocr.image_to_text(image)
print(result)
```



上面主要写了tesseract的安装方式以及使用，下面主要用到的是训练方法。



### tesseract-ocr使用以及训练方法

https://blog.csdn.net/zhou_zhu/article/details/78004131



jTessBoxEditor训练工具: (https://pan.baidu.com/s/1BTcPdVkyHJOAZIPIh2gJ2A)



1.获取样本

2.合成样本图片

3.生成box文件  

​	`tesseract.exe gc.font.exp1.tif gc.font.exp1 batch.nochop makebox`

4.文字矫正

5.生成.tr文件，

​	`tesseract gc.font.exp1.tif  gc.font.exp1  nobatch box.train `

6.计算字符集，从生成的box文件中提取。

​	`unicharset_extractor gc.font.exp1.box`

7.生成字体特征文字，格式如下：

​	`<fontname> <italic> <bold> <fixed> <serif> <fraktur>  `

8.特征训练，继续在命令行输入

​	`mftraining -F font -U unicharset gc.font.exp1.tr `

9、聚集tesseract识别的训练文件，命令行输入

​	`cntraining gc.font.exp1.tr`

 10、最后，合并相关文件，生成字典文件

​	`combine_tessdata font. ` 



