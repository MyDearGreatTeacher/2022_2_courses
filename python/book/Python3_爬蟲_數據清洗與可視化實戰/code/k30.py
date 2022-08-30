from pyecharts import Gauge

# 仪表盘
gauge = Gauge("大标题")
# scale_range设置仪表盘数据范围,angle_range设置角度范围
gauge.add("仪表盘顶部的标题", "仪表盘上的标题", 80.2, scale_range=[0, 250], angle_range=[225, -45])
gauge.render("./gauge.html")
