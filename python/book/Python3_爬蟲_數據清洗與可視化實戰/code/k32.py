from pyecharts import WordCloud
import pandas as pd

# 读取记录关键词和词频的文件
df_wd = pd.read_csv("E:/Data/practice/cp.csv", header=0)
# 生成关键词列表和词频列表
words = [i[0] for i in df_wd[['关键词']].values]
values = [i[0] for i in df_wd[['词频']].values]
# 词云
wc = WordCloud(width=1200, height=600)
# word_size_range设置词的大小范围,shape设置词云形状
wc.add("", words, values, word_size_range=[10, 120], shape='pentagon')
wc.render("./wordcloud.html")
