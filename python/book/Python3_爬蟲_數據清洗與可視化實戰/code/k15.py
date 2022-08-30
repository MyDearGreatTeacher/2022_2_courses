# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

# 读取杭州天气数据
df = pd.read_csv("E:/Data/practice/hz_weather.csv")

# 创建图的布局,位于1行1列,宽度为8,高度为5,这两个指标*dpi=像素值,dpi默认为80(保存图像时为100)
# 返回的fig是绘图窗口,ax是坐标系
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
# hist函数绘制柱状图,第一个参数传入数值序列(这里是Series),这里即是最低气温.bins指定有多少个柱子
ax.hist(df['最低气温'], bins=20)
# 显示图
plt.show()

# 取最低气温一列,得到的是Series对象
s = df['最低气温']
# 计算到miu的距离(还没取绝对值)
zscore = s - s.mean()
# 标准差sigma
sigma = s.std()
# 添加一列,记录是否是异常值,如果>3倍sigma就认为是异常值
df['isOutlier'] = zscore.abs() > 3 * sigma
# 计算异常值数目,也就是这一列中值为True的数目
print(df['isOutlier'].value_counts())
