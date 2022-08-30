import json
from pyecharts import Pie

# 从json文件中读取衣服清洗剂数据至dict中
f = open("E:/Data/practice/pies.json")
data = json.load(f)

# 各类衣服清洗剂的名称
name = data['name']
# 对应的销售额
sales = data['sales']
# 对应的市场占比
sales_volume = data['sales_volume']

# 初始化饼图,设置标题,标题位置居左侧
# width和height表示画布的宽高,默认是800px和400px
pie = Pie("衣服或清洗剂市场占比", title_pos='left', width=800)
# 添加一张图,标题为"成交量"(这里的标题在鼠标放在图上时显示),center指定饼图的圆心坐标(默认用百分比,相对于较小边的一半)
# radius指定[内半径,外半径],rosetype指定是否是南丁格尔图(默认radius就是,还有area就圆心角相同)
pie.add("成交量", name, sales_volume, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
# 这里指定的rosetype='area'就不通过圆心角展示百分比,只通过半径展示大小
# 这里is_random=True指随机排列颜色列表,is_legend_show=False不显示顶端的图例,is_label_show=True显示图形上的文本标签
pie.add("销售额", name, sales, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False,
        is_label_show=True)
# pie.show_config() # 打印输出图表的所有配置项
pie.render("./rose.html")  # 生成本地的HTML文件
