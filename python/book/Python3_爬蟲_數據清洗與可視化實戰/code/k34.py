from pyecharts import Bar3D
import json

f = open("E:/Data/practice/bar3ds.json")
datas = json.load(f)

# x轴类目数据
x_axis = datas['x_axis']
# y轴类目数据
y_axis = datas['y_axis']
# 要展示的数据,应是存[x,y,z]的列表,这里似乎顺序有点问题,作者在传入时调整
data = datas['data']
# 颜色种类
range_color = datas['range_color']

# 3D柱形图
bar3d = Bar3D("3D柱形图", width=1200, height=600)
# grid3d_shading='realistic'渲染具有真实感的图
# is_visualmap设置是否使用视觉映射组件,这个开了才能用后面的(子设置)
# visual_range_color设置过渡颜色,visual_range指定视觉映射组件的最小值和最大值
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], grid3d_shading='realistic',
          is_visualmap=True, visual_range_color=range_color, visual_range=[0, 20])
bar3d.render("./bar3d.html")
