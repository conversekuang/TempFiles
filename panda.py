# -*- coding: utf-8 -*-
# @Author: dell
# @Date:   2019-04-28 09:22:29
# @Last Modified by:   dell
# @Last Modified time: 2019-04-29 16:58:28

#bar
# from pyecharts import Bar

# x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
# y1 = [5, 20, 36, 10, 75]
# y2 = [10, 25, 8, 60, 20]

# bar = Bar(title = "产品月销量",width = 600,height = 420)
# bar.add(name = "商家A", x_axis = x, y_axis = y1)
# bar.add(name = "商家B", x_axis = x, y_axis = y2,is_xaxis_boundarygap =True)
# # 导出绘图html文件，可直接用浏览器打开
# bar.render('bar.html')


#line
# from pyecharts import Line
# x = ['2019-{:0>2d}'.format(s) for s in range(1,13)]
# # print(x)
# y1 = [5,10,26,30,35,30,20,26,40,46,40,50]
# y2 = [8,20,24,36,40,36,40,45,50,53,48,58]

# line = Line(title = "月销售总额",width = 600,height = 420)
# line.add(name="A",x_axis = x, y_axis=y1, line_width= 3, line='yellow')
# line.add(name="B",x_axis = x, y_axis=y2, yaxis_min = 0, yaxis_max=100, 
# 	is_xaxis_boundarygap = False,is_datazoom_show =True,line_width= 3, line='cyan')

# line.render('a.html')
# #表示时间的方法，format匹配方式学习。


#scatter
# from pyecharts import Scatter
# import pandas as pd

# dfboy = pd.DataFrame()
# dfboy['weight'] = [56,67,65,70,57,60,80,85,76,64]
# dfboy['height'] = [162,170,168,172,168,172,180,176,178,170]

# dfgirl = pd.DataFrame()
# dfgirl['weight'] = [50,62,60,70,57,45,62,65,70,56]
# dfgirl['height'] = [155,162,165,170,166,158,160,170,172,165]

# scatter = Scatter(title = "体格数据",subtitle = '身高cm',width = 600,height = 420)
# scatter.add(name = "boy", x_axis = dfboy['weight'], y_axis = dfboy['height'])
# scatter.add(name = "girl", x_axis = dfgirl['weight'], y_axis = dfgirl['height'],
#            yaxis_min = 130,yaxis_max = 200,xaxis_min = 30,xaxis_max = 100)

# scatter.render('a.html')
# #如何显示横纵坐标需要考虑？

# from pyecharts import Scatter
# import pandas as pd 

# def custom_formatter(params):
#     return (params.value[3] + ':' +
#              str(params.value[0]) +','
#              +str(params.value[1]) + ','
#              +str(params.value[2]))

# df = pd.DataFrame()
# df['country'] = ["中国",'美国','德国','法国','英国','日本','俄罗斯','印度','澳大利亚','加拿大']
# df['life-expectancy'] = [76.9,79.1,81.1,81.9,81.4,83.5,73.13,66.8,81.8,81.7]
# df['capita-gdp'] = [13334,53354,44053,37599,38225,36162,23038,5903,44056,43294]
# df['population'] = [1376048943,321773631,80688545,64395345,64715810,126573481,143456918,
#                     1311050527,23968973,35939927]

# scatter = Scatter(title='发展水平', width= 600 ,height = 420)
# scatter.add(name='',
# 			x_axis = df['capita-gdp'],
# 			y_axis = df['life-expectancy'],
# 			extra_data = df['population'].values.tolist(),
# 			extra_name = df['country'].values.tolist(),
# 			tooltip_formatter=custom_formatter,
# 			is_visualmap=True, 
#             visual_orient="vertical",
#             visual_type = 'color',  #可以是size或者color
#             visual_dimension=2,
#             visual_range=[20000000, 1500000000],
#            )
# scatter.render('a.html')


import pandas as pd

df = pd.read_csv(u'NightBus总和.csv')
for d in df:
	if d['Col_num'] > 5:
		print d['小区']