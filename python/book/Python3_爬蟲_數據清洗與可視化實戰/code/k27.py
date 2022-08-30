import json
from pyecharts import Funnel

f = open("E:/Data/practice/pies.json")
data = json.load(f)

name = data['name']
sales = data['sales']
sales_volume = data['sales_volume']

# 漏斗图.这里传入空字符串即可没有titile
funnel = Funnel("", width=800)
# label_pos='inside'指明标签的位置在图的内部,label_text_color='#fff'指明标签自己颜色为白色
funnel.add("成交量", name, sales_volume, is_label_show=True, label_pos='inside', label_text_color='#fff')
funnel.render("./funnel.html")