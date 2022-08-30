import json
from pyecharts import Bar
import copy

f = open("E:/Data/practice/pies.json")
data = json.load(f)

name = data['name']
sales = data['sales']
sales_volume = data['sales_volume']

'''
注,书上代码这里作者为柱形图设置了center,这是没意义的
'''

# 柱形图(普通)
bar = Bar("衣服清洗剂市场占比", width=800)
# mark_point=['average']即在平均值位置做标记
bar.add("成交量", name, sales_volume, mark_point=['average'])
# mark_point=['max', 'min']即在最大值和最小值位置做标记
bar.add("销售额", name, sales, mark_point=['max', 'min'])
bar.render('./bar.html')

# 条形图
bar_hori = Bar("衣服清洗剂市场占比", width=800)
bar_hori.add("销售额", name, sales, mark_point=['max', 'min'])
# 相比普通柱形图,只要在最后一次add里设置is_convert=True即可
bar_hori.add("成交量", name, sales_volume, is_convert=True)
bar_hori.render('./bar_hori.html')
