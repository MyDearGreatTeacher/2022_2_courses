import requests
import json
import urllib.request
import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
json结构查看工具 http://jsoneditoronline.org/index.html
去哪网移动端度假 https://m.dujia.qunar.com/
'''

# 设置全局变量:两个Chrome浏览器驱动
driver = webdriver.Chrome()
driver_ = webdriver.Chrome()


# 建立要写入的csv文件,并将表头写进去
def init_csv():
    global f
    global writer
    # 要写入的文件位置
    csv_file = "E:/WorkSpace/PyCharm/xiaoduyao/qunar_routes.csv"
    # 以写入方式打开文件
    f = open(csv_file, 'w', newline='', encoding='utf-8')
    # 获取该文件的csv写入对象
    writer = csv.writer(f)
    # 先把表头写进去
    writer.writerow(['出发地', '目的地', '路线信息', '酒店信息'])


# 在第一个驱动对应的浏览器下拉了若干次,即使得页面上有了足够的产品后调用本函数
# 这里将自由行产品的详细信息整理并写入csv文件,其中会用到第二个驱动来点开详细页面
def dump_routes_csv(dep, arr):
    global driver
    global driver_
    global writer
    # 按css的class获取所有产品的列表
    routes = driver.find_elements_by_css_selector(".item g-flexbox list-item")
    # 对其中的每个产品
    for route in routes:
        try:
            # print("\nroute info:%s" % route.text)
            # 获取详情信息的url,从页面元素上可以看到在这个div的data-url属性中
            url = route.get_attribute("data-url")
            # 用另一个Chrome驱动,也就是在另一个Chrome里打开这个详情页
            driver_.get(url)
            time.sleep(random.uniform(2, 3))
            # TODO
        except Exception as e1:
            print(str(e1))


if __name__ == '__main__':
    init_csv()
    dep_cities = ['上海']  # 出发地
    # 对每个出发地
    for dep in dep_cities:
        # 先获取相应的目的地集合,相当于点击"搜索目的地、主题、景点"时发送的XHR请求
        url = "https://m.dujia.qunar.com/golfz/sight/arriveRecommend?dep=" + urllib.request.quote(
            dep) + "&exclude=&extensionImg=255,175"
        resp = requests.get(url).json()
        # 根据这里json的结构遍历其中的各个目的地
        for data_i in resp['data']:
            # 为演示方便.只爬取国内一栏的
            if data_i['title'] != '国内':
                continue
            for sbm_i in data_i['subModules']:
                # 为演示方便.只爬取华东地区的
                if sbm_i['title'] != '华东地区':
                    continue
                for items_i in sbm_i['items']:
                    # 为演示方便.只爬取到杭州的(其实就是获得了上海->杭州这么一个信息)
                    if items_i['query'] != '杭州':
                        continue
                    arrv = items_i['query']  # 这里在前面的演示限制条件下其实就只能是杭州
                    # 用Selenium驱动Chrome打开移动端自由行搜索结果页面,这里和书上的url不一样,可能是网站更新了的原因
                    url = "https://m.dujia.qunar.com/p/list?dep={}&query={}&it=dujia_hy_destination&et=#/page=home/planid=-1/linesubject=-1/mobfuncname={}".format(
                        urllib.request.quote(dep), urllib.request.quote(arrv),
                        urllib.request.quote("自由行,出发地参团,目的地参团")
                    )
                    # 浏览器访问该页面,则进入了从dep位置去arrv位置的产品页面
                    driver.get(url)
                    try:
                        # 在10s内,等待class=item g-flexbox list-item的元素加载完成,即所有产品的div加载完
                        WebDriverWait(driver, 10).until(
                            ec.presence_of_all_elements_located((By.CLASS_NAME, "item g-flexbox list-item")))
                    except Exception as e:
                        print(str(e))
                        raise  # 引发异常,类似于将异常抛出
                    print("dep:%s arrv: %s" % (dep, arrv))  # 当前在爬哪里到哪里的产品
                    # 连续下拉滚动条3次,获得更多的产品
                    for i in range(3):
                        time.sleep(random.uniform(2, 3))
                        print("page %d" % (i + 1))  # 下拉了几次了
                        # 模拟page down的键入实现下拉
                        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                    # 至此,已经下拉完毕,页面上有了足够的产品信息
                    # 将dep->arrv的产品写入csv文件中去
                    dump_routes_csv(dep, arrv)
