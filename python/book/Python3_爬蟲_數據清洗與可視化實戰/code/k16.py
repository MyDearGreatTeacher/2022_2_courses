# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

# 符合格式的txt文件也可以直接当csv文件读入
df = pd.read_csv('E:/Data/practice/sale_data.txt')
# 创建图布局
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
# 取上海数据
df_ = df[df['位置'] == '上海']
# 函数boxplot用于绘制箱型图,绘制的指标是'成交量',坐标用前面matplotlib创建的坐标系
df_.boxplot(column='成交量', ax=ax)
plt.show()

# 查看上海的成交量情况,这里即提取为Series对象
s = df_['成交量']
print(s.describe())

# 这里规避A value is trying to be set on a copy of a slice from a DataFrame
df_ = df_.copy()
# 这里将大于上四分位数(Q3)的设定为异常值
# df_['isOutlier'] = s > s.quantile(0.75)
df_.loc[:, 'isOutlier'] = s > s.quantile(0.75)
# 查看上海成交量异常的数据
df_rst = df_[df_['isOutlier'] == True]
print(df_rst)
