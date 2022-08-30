import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/Data/practice/qunar_free_trip.csv")
# 查看数据的组织结构
# print(df.head())

# 查看数据信息,从中可以看到没有缺失值(全是non-null)
print(df.info())

# 查看重复值,先转成bool的Series再用值的统计函数查看
print(df.duplicated().value_counts())

# 移除重复值,然后再确认一下
df = df.drop_duplicates()
print(df.duplicated().value_counts())

# 查看描述性统计信息
print(df.describe())

# 绘制价格分布的直方图/箱型图
# 注意这里的细节,一行两列2个图,所以会返回两个坐标系,这里在变量ax->axes上体现了出来
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# 第一个坐标系上绘制直方图
axes[0].hist(df['价格'], bins=20)
# 第二个坐标系上绘制箱型图
df.boxplot(column='价格', ax=axes[1])
# 自动调整绘图区的大小及间距,使所有的绘图区及其标题、坐标轴标签等都可以不重叠的完整显示在画布上
fig.tight_layout()
plt.show()

# 用均方差法找出价格异常值,标准差能反映一个数据集的离散程度
s = df['价格']
# 序列中的价格和平均价格的差距
zscore = s - s.mean()
# 这里用3.5倍sigma
df['isOutlier'] = zscore.abs() > 3.5 * s.std()
# 输出异常的样本
df_out = df[df['isOutlier'] == True]
# print(df_out)
