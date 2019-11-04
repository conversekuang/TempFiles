## Pycharm 用法总结



微信链接 <https://mp.weixin.qq.com/s/VOkacikFL3PvsdApMHgKFw>



1. Pycharm自带`ctrl+alt+L`自动PEP8，autoPEP8 更加彻底

2. localhistory中可以查看文件的历史，将误删的文件还原。单机右键`localhistory-> revert`

3. ideaVim 在Pycharm中使用vim来编辑代码。Auto Switch Input Source In IdeaVim Mode

   For MAC Only An plugin for auto switching input method while using IdeaVim plugin FOR MAC ONLY

4. 模板:

   - 初始化模板：代码模板settings 里面，创建python模板。在创建python文件时候自动创建

   - 编写代码模板：预设代码模板mac中是`command+J`。windows是`ctrl+J`，可以选择预设模板

5. 书签：

   `ctrl+F11` 打书签并可以命名

   `shift+F11`展开标签

   `F11` 可以匿名或者取消标签

   `ctrl+B`  深入查看源码



微信链接 <https://mp.weixin.qq.com/s/zW8hzcYHp3PalCBpzDotxw>



6. 调试技巧，无需重复请求与反复操作，可记录变量信息并不断调试。

   打断点且运行`run with debug`，在console界面点击`Show Python Prompt`，可以对变量进行调试。就像在`ipython`中交互命令行

   - 通过配置`Edit Configurations`里选择`show command line afterwards`

     （该配置没有找到）

7. 指定参数执行脚本：

   平时`run`，`shift+F10`。

   若带参数，可以配置`Edit Configurations`填写`script parameters`。也可以更换python解释器版本

8. 搜索过滤测试文件

   Find in Path搜索出现很多测试文件造成干扰，只要在 `File mask` 里填写 `!test*` 可以将这些test文件过滤掉。（按快捷键`Ctrl + Shift + F`或从从菜单`Edit-》Find-》Find in Path`进入全局查找界面）

   

9. 关闭灯泡提示( intention bulb)

   灯泡：为了凸显错误，自带矫正。缺点：错误有红波浪线，矫正效率低；遮挡代码影响视线

   红灯泡，一般都是语法问题，如果不处理会影响代码运行。

   黄灯泡，就只是一个提示，提示你代码不规范等，并不会影响程序的运行。

   settings 搜索 intention bulb可以关闭灯泡提示。

10. 关闭波浪线

    Pycharm 会实时地对变量名进行检查，若不是一个单词会出现波浪线，Python多单词会用下划线分割（其他语言是驼峰式命名）。

    若每个人命名习惯不一样，Pycharm会一堆提示可以关闭非语法级的波浪线。IDE窗口有人头像，选中Syntax级别就可以。



微信链接<https://mp.weixin.qq.com/s/-t9S_VlvkpXmc5s0ySs_JA>



11. 一键代码性能分析

    可以对代码中函数耗时进行分析。`run->Profile程序`，调用次数，程序运行时间以及百分比。有图和表两种方式

    

12. Git做版本控制器

    

13. Tab转空格

    推荐使用tab是4个空格。

    - 老文件：可以设置检查原文件缩进风格来决定tab到底是制表符还是空格。`settings->code style ->indents detection`里面，全选。
    - 新文件：`settings->code style -> Python ->Use tab character`，勾选则表示使用tab缩进。不勾选，IDE默认是4个空格

14. 一次注册，永久激活

    参见原文

    

15. 源码文档，快速预览

    函数开头的三个`"`文档是函数文档(DocString)，该函数的参数类型，说明，返回值以及例子。`ctrl+q`可快速预览docstring。

    `ctrl + shift + i`快捷键，可以不用跳转直接以浮窗形式显示该函数的源代码



微信  https://mp.weixin.qq.com/s/Hq3TPJa2T83FAnOPi5yFbw



16. 快速定位错误行

定位出现红色波浪的py文件，按`F2 或 shift+F2`可以快速定位错误行。

在settings中可以搜索key map可以找到快捷键功能

17. 快速查看最近的修改

Windows 是`Alt+shift+C` 可以快速查看最近修改的内容

18. 静态代码分析检查

文件夹 --> 右键 --> `Inspect Code` 即可开启静态检测

19. 精准定位

|    功能    | 快捷键                                                   |
| :--------: | :------------------------------------------------------- |
| 定位到文件 | Windows：Ctrl+Shift+N：，Mac：Command+ shift +N          |
|  定位到类  | Windows：Ctrl+N，Mac：Command+N                          |
| 定位到符号 | Windows：Ctrl+Alt+Shift+N，Mac：Option+Shift+Command+N： |
|  文件结构  | Windows：Ctrl+F12，Mac：Command+F12                      |
| 定位到某行 | Windows：Ctrl+G，Mac：Command+G                          |

20. TODO

为避免被别人打断思路，记录当前工作内容以及下一步要做的实现。

`# TODO: xxx，用FIXME来区分紧急程度`

Windows 是 `Alt+6`查看标记出来的TODO



微信 https://mp.weixin.qq.com/s/zj5IEC0rzBt9YzqgPOGCvw



21. 随处折叠

`ctrl和+`展开，`ctrl和-关闭`。

22. 重构操作

    变量名称的重新修改，如果全局替换可能会影响其他地方代码。Refactor中自动匹配作用域，批量名称的修改。`Shift+F6`。在一个函数中对名称进行批量修改

23. 复杂操作

    可以将一连串操作录制macro，然后将宏绑定快捷键，通过快捷键来执行一连串的复杂操作。

24. 取消折叠多行标签页

    Pycharm打开多个标签页时会用数字隐藏标签，为了都显示出来，可以`Windows-> Editor Tabs -> Tabs Placement -> show Table in Single Row `

25. 应用搜索，阅读源码

    代码的入口，流程，走向特别重要。要知道哪里调用了这个类。`Mac：Command+Option+F7 ，Windows：Ctrl+Alt+F7`。可以看到调用列表



​	微信   https://mp.weixin.qq.com/s/ysl6dIBrqLvEu54ELnUoug



26. 文件差异，轻松比对

    Pycharm中文件比对。 ` view-> compare with-> 目标文件`。

    可以选择按行差异，或者按变化差异。可以选择inspection的级别。

    并将代码进行整合，

27. 以列为单位的块编辑

    alt 用鼠标选择操作区域进行删除。类似于sublime中多游标的操作。

28. 智能补全

    小写开头不能匹配大写开头的函数，变量，或者类。修改`settings`中`code completion`中选择`match case`，取消打钩。

29. Pycharm眼睛保护色

    Pycharm 界面颜色配置：https://mp.weixin.qq.com/s/KdGasLFs4M_Tass6fqgwKQ

30. 调试远程服务器代码

    pdb  https://mp.weixin.qq.com/s/tDufSUBrBBNfMEr5_dxM0g

    远程调试。 https://mp.weixin.qq.com/s/ECWCJMQ6oEDaY1x1JfGfkg