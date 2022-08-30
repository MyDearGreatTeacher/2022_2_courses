import json
from pyecharts import Line

f = open("E:/Data/practice/lines.json")
data = json.load(f)
# 时间(月份)
date = data['date']
# 成交量
sale1 = data['sales1']
# 销售额
sale2 = data['sales2']

# 折线图(普通)
line1 = Line("洗衣液月售出情况")
# 设置标记点标记符号为菱形,设置标记点文本颜色#40ff27(暖绿)
line1.add("成交量", date, sale1, mark_point=['average', 'max', 'min'], mark_point_symbol='diamond',
          mark_point_textcolor='#40ff27')
# 设置折线为光滑曲线,设置标记线在最大值处和平均值处,设置标记符号为箭头,设置标记符号大小
line1.add("销售额", date, sale2, mark_point=['max'], is_smooth=True, mark_line=['max', 'average'],
          mark_point_symbol='arrow', mark_point_symbolsize=40)
line1.render("./line1.html")

# 折线图(堆叠)
line2 = Line("洗衣液月售出情况")
# 设置is_stack=True即成为了堆叠的图,即同样设置堆叠的图的值会堆高(而不是它原有的值)
# 在这个例子里,成交量和销售额完全是两种不同的数据,堆叠其实意义不明
# 而且一般都是柱状图做堆叠,很少有用折线图做堆叠的吧,作者这个例子不太好
line2.add("成交量", date, sale1, is_stack=True, is_label_show=True)
line2.add("销售额", date, sale2, is_stack=True, is_label_show=True)
line2.render("./line2.html")

# 阶梯折线
line3 = Line("洗衣液月售出情况")
# 设置is_step=True即可
line3.add("成交量", date, sale1, is_step=True, is_label_show=True)
line3.add("销售额", date, sale2, is_step=True, is_label_show=True)
line3.render("./line3.html")

# 面积折线图
line4 = Line("洗衣液月售出情况")
# 设置is_fill=True即可形成面积折线图,area_opacity设置填充区域透明度
line4.add("成交量", date, sale1, is_fill=True, area_opacity=0.4)
line4.add("销售额", date, sale2, is_fill=True, area_opacity=0.2)
line4.render("./line4.html")


