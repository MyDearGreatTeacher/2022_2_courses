from bs4 import BeautifulSoup
import requests
import re

'''
中国旅游网 /www.cntour.cn
'''

url = 'http://www.cntour.cn/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')  # 使用LXML的HTML解析器
print(type(soup))  # <class 'bs4.BeautifulSoup'>
# 空格不能少,不然会解析错误;注意,即便是取单条,nth-child改为nth-of-type
# 这部分用于选择的字符串在chrome中右键检查,然后复制selector
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(type(data))  # <class 'list'>
# 把数据提取出来
for item in data:
    # print(type(item))  # <class 'bs4.element.Tag'>
    result = {
        'title': item.get_text(),  # 提取标签的正文
        'link': item.get('href'),  # 提取标签的href属性L(链接字符串)
        'ID': re.findall('\d+', item.get('href'))  # 用正则从链接字符串中匹配数字部分
    }
    print(result)
