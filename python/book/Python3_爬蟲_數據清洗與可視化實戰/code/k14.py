import pandas as pd

# 读取杭州天气文件
df = pd.read_csv("E:/Data/practice/hz_weather.csv")

# 数据透视表
df1 = pd.pivot_table(df, index=['天气'], columns=['风向'], values=['最高气温'])

# 用isnull()获得缺失值位置为True,非缺失值位置为False的DataFrame
lack = df1.isnull()
# print(lack)

# 再调用any()就可以看到哪些列有缺失值
lack_col = lack.any()
# print(lack_col)  # 可以看到只有北风这一列完全没有缺失值

# 只显示存在缺失值的行列
df1_lack_only = df1[df1.isnull().values == True]
# print(df1_lack_only)

# 删除缺失的行
df1_del_lack_row = df1.dropna(axis=0)
# print(df1_del_lack_row)

# 删除缺失的列(一般不因为某列有缺失值就删除列, 因为列常代表某指标)
df1_del_lack_col = df1.dropna(axis=1)
# print(df1_del_lack_col)  # 只剩下北风

# 使用字符串代替缺失值
df1_fill_lcak1 = df1.fillna('missing')
# print(df1_fill_lcak1)

# 使用前一个数据(同列的上一个数据)替代缺失值,第一行的缺失值没法找到替代值
df1_fill_lack2 = df1.fillna(method='pad')
# print(df1_fill_lack2)

# 使用后一个数据(同列的下一个数据)替代缺失值,最后一行的缺失值没法找到替代值
# 参数limit=1限制每列最多只能替代掉一个NaN
df1_fill_lack3 = df1.fillna(method='bfill', limit=1)
# print(df1_fill_lack3)

# df对象的mean()方法会求每一列的平均值,也就是每个指标的平均值.下面使用平均数代替NaN
df1_fill_lack4 = df1.fillna(df1.mean())
# print(df1_fill_lack4)
