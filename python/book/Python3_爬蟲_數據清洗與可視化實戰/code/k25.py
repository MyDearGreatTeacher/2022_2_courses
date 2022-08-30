import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/Data/practice/taobao_data.csv")
# 求不同位置的产品的数值字段(价格,成交量)的均值,然后按成交量降序
df_mean = df.groupby("位置").mean().sort_values("成交量", ascending=False)
print(df_mean.head())

# 设置绘图风格
plt.style.use('ggplot')
# 绘制绘图层
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Series.plot()函数用Series中的项在mpl的坐标系上进行绘图,kind='barh'指定绘制的是横向条形图
df_mean['价格'].plot(kind='barh', ax=ax1)
# 设置横向坐标轴上的文字,在横向条形图中也就代表指标的意义
ax1.set_xlabel('各省份的平均价格')

# 绘制右边的图,各个省份平均的成交量
df_mean['成交量'].plot(kind='barh', ax=ax2)
ax2.set_xlabel('各省份的平均成交量')

# 自动调整和显示
fig.tight_layout()
plt.show()

# --------------------------------------------------

# 绘制各省份成交量的折线图,柱状图,箱型图,饼图
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
s = df_mean['成交量']
s.plot(kind='line', ax=axes[0][0], title="折线图")
s.plot(kind='bar', ax=axes[0][1], title='柱状图')
s.plot(kind='box', ax=axes[1][0], title='箱型图')
s.plot(kind='pie', ax=axes[1][1], title='饼图')
fig.tight_layout()
plt.show()

# --------------------------------------------------

# 绘制价格与成交量的散点图
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
# 传入两个等长的序列(这里是Series)用来表示点的两个维度坐标
ax.scatter(df['价格'], df['成交量'])
ax.set_xlabel('价格')
ax.set_ylabel('成交量')
plt.show()
