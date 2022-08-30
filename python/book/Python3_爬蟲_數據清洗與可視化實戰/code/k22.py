import pandas as pd

# 各国人口数据文件
df_pop = pd.read_csv("E:/Data/practice/european_cities.csv")
# print(df_pop.head())

# 查看字段的数据类型.用这种方式查看到的object(文本)就是str类型
print(df_pop.dtypes)

# 这里表明两种写法是一样的,都返回这一列的Series对象
print(df_pop['Population'] is df_pop.Population)  # True

# 对人口字段,删除逗号并转为int:这里apply()函数传入一个函数,将对Series中的每个项调用该函数
df_pop['Population'] = df_pop.Population.apply(lambda x: int(x.replace(",", "")))
# print(df_pop.head())

# 读取State列的前三个数据看一下
ary = df_pop['State'].values[:3]
print(ary)  # [' United Kingdom' ' Germany' ' Spain']

# 去掉State字段中数据两端的空格
df_pop['State'] = df_pop.State.apply(lambda x: x.strip())
# print(df_pop.head())
