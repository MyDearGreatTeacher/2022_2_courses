import pandas as pd

# (1)从csv文件中读取数据生成DataFrame对象.按','分割,编码为utf-8,0号行作为列名
df = pd.read_csv("E:/Data/practice/taobao_data.csv", delimiter=',', encoding='utf-8', header=0)
# print(type(df))  # <class 'pandas.core.frame.DataFrame'>

# (2)将(刚刚读出的)df对象中的数据写到另一个csv文件中.columns指定要写的是哪些列,禁止写入索引,保存表头信息
df.to_csv("E:/Data/practice/test_in.csv", columns=['宝贝', '价格'], index=False, header=True)

# (3)取前3行(得到的还是DataFrame对象)
rows = df[0:3]
# print(rows)

# (4)取指定的某些列
cols = df[['宝贝', '成交量', '位置']]
# print(cols.head())  # 至多前5行

# (5)取前4行中的某些列.第一个维度指定行,在第二个维度上选取指定的列
print(df.ix[0:3, ['成交量', '价格']])  # 注意这里是0:3,另外ix方法已经被弃用
# 或(使用loc按label索引)
print(df.loc[0:3, ['成交量', '价格']])  # 这里0:3可以替换成df.index[0:4]
# 或(使用iloc按index索引)
print(df.iloc[0:4, df.columns.get_indexer(['成交量', '价格'])])  # 这里是0:4

# (6)从已有的列中计算新的列,并直接将其写入到df对象中
df['销售额'] = df['价格'] * df['成交量']
# print(df.head())

# (7)根据条件过滤行
result = df[(df['价格'] < 100) & (df['成交量'] > 10000)]
# print(result.head())

# (8)按照某个字段排序
df1 = df.set_index("价格").sort_index()
# print(df1.head())

# (9)按照多个字段排序
# 默认level是0,这里即先"位置"再"价格"
df2 = df.set_index(['位置', '价格']).sort_index()
# print(df2.head())
# level设置为1时,这里即先"价格"再"位置"
df2 = df2.sort_index(level=1)
# print(df2.head())

# (10)数据整理操作
# 先删除label为'宝贝'和'卖家'的列,然后按位置分组,计算组内的均值,再按成交量进行排序(降序)
df_mean = df.drop(['宝贝', '卖家'], axis=1).groupby("位置").mean().sort_values("成交量", ascending=False)
# print(df_mean)
# 先删除label为'宝贝'和'卖家'的列,然后按位置分组,计算组内的加和,再按成交量进行排序(降序)
df_sum = df.drop(['宝贝', '卖家'], axis=1).groupby("位置").sum().sort_values("成交量", ascending=False)
# print(df_sum)

# (11)查看表的数据信息和描述性统计信息
print(df.info())
print(df.describe())
