import pandas as pd

# 中国旅游网的文章标题和链接数据
df = pd.read_csv("E:/Data/practice/getlinks.csv")
# print(df.head())

# 这里df.link即获取link这一列形成Series对象
# Series对象的str属性的extract()方法,将对Series对象中的每个项用指定的正则方式匹配并生成匹配后的DataFrame
# 没有匹配到的部分在生成的DF对象中将被设置成NaN
df1 = df.link.str.extract(r'(\d+)')  # 匹配数字
# print(df1.head())

# 匹配'.'任意字符'/'数字,因为是两部分所以生成的DF对象有两列
df2 = df.link.str.extract(r'(.*)/(\d)')
# print(df2.head())

# 在括号内最前面写'?P<列名>'可以为生成的DF对象添加列名
df3 = df.link.str.extract(r'(?P<URL>.*)/(?P<ID>\d+)')  # 匹配的内容和df2是一样的
# print(df3.head())

# 这时返回一个Series,而不是单列的DF
s4 = df.link.str.extract(r'(\d+)', expand=False)
# print(s4.head())
