import requests
import json

'''
有道翻译 http://fanyi.youdao.com/
西刺代理 http://www.xicidaili.com/
'''


# 使用有道翻译发送post请求来翻译文本
# XHR类型即通过XMLHttpRequest方法发送的请求,是用Ajax方式发送的请求
# 在使用有道翻译时,不按翻译键也会随着输入的内容而自动翻译,显然是在用Ajax方式交互
def get_translate_data(word=None):
    # 消息头中的请求网址,因为有道反爬机制,在网上找到解决方案去掉"translate"后的"_o"
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # post的请求实体,在chrome的Header里可以看到
    form_data = {'i': word,  # 这里是要翻译的单词
                 'from': 'AUTO',
                 'to': 'AUTO',
                 'smartresult': 'dict',
                 'client': 'fanyideskweb',
                 'salt': '1540867058355',
                 'sign': 'a45461db88c2a4dcec5882c5d9670a20',
                 'doctype': 'json',
                 'version': '2.1',
                 'keyfrom': 'fanyi.web',
                 'action': 'FY_BY_REALTIME',
                 'typoResult': 'false'}
    # 构造一个浏览器的请求头,伪装成浏览器访问,只要提供User-Agent(用户代理),这里伪装成了Chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
    # 代理池,可以到西刺代理里找HTTP和HTTPS的ip
    proxies = {
        'https': 'https://36.110.14.186:3128',
        'http:': 'http://58.53.128.83:3128'
    }
    # 发送post请求,获得响应.要传入请求实体,这里还传入了伪装的请求头和代理池
    response = requests.post(url, data=form_data, headers=headers, proxies=proxies)
    # 将json格式字符串转字典
    context = json.loads(response.text)
    # 打印翻译后的数据
    print(context['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    get_translate_data('我是个大傻逼')  # I'm a big silly force
