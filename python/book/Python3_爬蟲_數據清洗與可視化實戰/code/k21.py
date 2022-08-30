import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('E:/Data/practice/hz_weather.csv')
df = df[['日期', '最高气温', '最低气温']]
# print(df.head())

print(type(df.日期))  # <class 'pandas.core.series.Series'>
print(type(df.日期.values))  # <class 'numpy.ndarray'>

# 修改日期格式
# 注意,df.日期得到的是Series对象,df.日期.values得到的是ndarray多维数组
# pd.to_datetime()函数将输入解析成时间对象的格式并返回
# format参数指定解析的方式
# 当输入列表形式的值时,返回DatetimeIndex;当输入Series时,返回Series;当输入常量时,返回Timestamp
print(type(pd.to_datetime(df.日期.values, format="%Y-%m-%d")))  # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
print(type(pd.to_datetime(df.日期, format="%Y-%m-%d")))  # <class 'pandas.core.series.Series'>
df.日期 = pd.to_datetime(df.日期.values, format="%Y-%m-%d")
# print(df.head())

# 将日期设置为索引
df = df.set_index('日期')
# 取出第0个索引值对应的日期
print(df.index[0])  # 2017-01-01 00:00:00
# DatetimeIndex里存的是一个个的Timestamp,查看一下类型
print(type(df.index[0]))  # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
# print(df.info())

# 提取1月份的温度数据
df_jan = df[(df.index >= "2017-1-1") & (df.index < "2017-2-1")]
# 或用这种方式也可以
df_jan = df["2017-1-1":"2017-1-31"]
# print(df_jan.info())


# 只取到月份
df_m = df.to_period('M')
print(df_m.head())

# 利用上面的只取到月份,对level=0(即索引层级)做聚合就可以求月内的平均值等
s_m_mean = df_m.groupby(level=0).mean()
# print(s_m_mean.head())

# 绘制[最高温度]和[最低温度]两个指标随着索引[时间]变化的图
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
df.plot(ax=ax)
plt.show()
