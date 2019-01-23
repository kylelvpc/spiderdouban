#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import lxml
import sys
import io
from AnotherProject import ConnectDB


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
request = urllib.request
url = "http://www.dianping.com/shenzhen/ch10/g110"  # 这个网站被禁止直接访问，需要User-Agent
url1 = "https://sz.meituan.com/meishi/pn1/"
url2 = "https://movie.douban.com/top250"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}




conn=ConnectDB.ConnectDatabase()
#print(conn)


while url2:
    request = urllib.request.Request(url2, headers=headers)
    response = urllib.request.urlopen(request)
    dat1 = response.read().decode("utf-8")
    soup = BeautifulSoup(dat1, "lxml")
    for each in soup.find_all('div', class_='info'):
        img_url = each.previous_sibling.previous_sibling.a.img['src']                   # 链接
        title = each.find('div', class_='hd').get_text(strip=True).replace('\xa0', '')  # 标题
        actor = list(each.find('p', class_='').strings)[0].strip().replace('\xa0', '')  # 导演演员
        type_ = list(each.find('p', class_='').strings)[1].strip().replace('\xa0', '')  # 类型
        score = each.find('div', class_='star').get_text('/', strip=True)  # 评分及人数
      #  quote_ = each.find('span', class_='inq').string  # 一句话总结
        if each.find('span', class_='inq'):  # 注意有部电影没有总结，也就没有<span class="inq">标签这里用if检测一下防止None使用string方法报错
             quote_ = each.find('span', class_='inq').string
        else:
             quote_ = '没有总结哦'
        # print([img_url, title, actor, type_, score, quote])  #
        # 组装成mysql语句，再插入。
        replace_data = (img_url, title, actor, type_, score, quote_)
        replace_sql = "insert into dianying(img_url, title,actor,type_,score, quote_) \
                        values(%s,%s,%s,%s,%s,%s)"
        conn.addData(replace_sql, replace_data)  # 这里注意cursor.excute的用法
        # print("插入数据成功")
        # 这里需要检查是否有重复的数据，如果有的话就需要删除或者掠过。
        try:
            url2 = 'https://movie.douban.com/top250' + soup.find('span', class_='next').a['href']
        except TypeError:
            url2=None







