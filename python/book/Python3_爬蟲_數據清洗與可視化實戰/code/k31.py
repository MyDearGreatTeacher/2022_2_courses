from pyecharts import Liquid

liquid = Liquid("水球图", title_pos='center')
# shape设置水球形状,可以自定义svg,is_liquid_animation开启动画,is_liquid_outline_show显示边框
liquid.add("水球", [0.8, 0.3], shape='roundRect', is_liquid_animation=True, is_liquid_outline_show=True)
liquid.render("./liquid.html")
