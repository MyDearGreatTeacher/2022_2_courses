from pyecharts import Bar, Line, Overlap
import json

f = open("E:/Data/practice/overlaps.json")
data = json.load(f)
date = data['date']
sales1 = data['sales1']
sales2 = data['sales2']

# 柱状图.在这个画布上指定了大标题,可以让其他画布不再指定,最终就使用这个标题
bar = Bar("Line-Bar")
bar.add("柱状", date, sales1, is_label_show=True)

# 折线图
line = Line("")
line.add("折线", date, sales2, is_label_show=True)

# 合并
overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.render("./overlap.html")
