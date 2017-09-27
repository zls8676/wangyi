#! /uer/bin/env python

import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import os
import urllib
import time
import re


def save(filename,contents):
    fh = open(filename,'a+')
    fh.write(contents)
    fh.close()


def setHead(session,headers):
    session.headers.update(headers)
    return session

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RecursionError:
        return None

def setCookie(session,dict):
    cookies = requests.utils.cookiejar_from_dict(dict,cookiejar=None,overwrite=True)
    session.cookies = cookies
    return session


def getPage(session,url):
    return session.get(url)


# def parse_one_page(html):
#     pattern = re.compile('<div "m_photoset_title">(.*?) </div>')
#     items = re.findall(pattern,html)
#     return items


def main():
    url = "http://3g.163.com"

    s = requests.session()

    h = {   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36"


    }

    cookie_dict = {"Cookie":"__s_=1; _ntes_nnid=6e735bbbb9740d136d59da93befe8425,1505138071684; _ntes_nuid=6e735bbbb9740d136d59da93befe8425; usertrack=c+xxC1m3T2lgVUtnCTbiAg==; _ga=GA1.2.147778635.1505185647; __gads=ID=cf82ad3852c53a9d:T=1505485578:S=ALNI_MYy8Zrj8ru2O5iaorLCdaKcFQtG6Q; UM_distinctid=15e85eeec1a2e9-04ecd7e75469b5-2a044871-15f900-15e85eeec1b376; vjuids=-c452c7ffe.15e85eeefc6.0.5d7c83140d931; Province=010; City=010; NNSSPID=d013ce3c26944982957e684ea9b35219; vjlast=1505485582.1506407927.13; ne_analysis_trace_id=1506409210339; vinfo_n_f_l_n3=e9fa7f7a30979079.1.1.1505485582297.1505485594824.1506409212437; s_n_f_l_n3=e9fa7f7a309790791506407926850; Hm_lvt_b2d0b085a122275dd543c6d39d92bc62=1506409158; Hm_lpvt_b2d0b085a122275dd543c6d39d92bc62=1506409478"

    }

    s = setHead(s,h)
    s = setCookie(s,cookie_dict)

    r = getPage(s,'http://3g.163.com')
    # print(r.text)
    save('index.html',r.text)

    # time.sleep(2)
    # for i in range(2,4):

    r2  = getPage(s,'http://temp.163.com/special/00804KVA/cm_yaowen_03.js')
    # soup = BeautifulSoup(r2,'html.parser')
    # print(r2.text)
    # print(r2.text)
    # save('xinwen.txt',r2.text)
    re2 = re.compile('.*?"docurl":"(.*?)"',re.S)
    re3 = re2.findall(r2.text)
    n = 1
    for item  in re3:
        time.sleep(5)
        count = getPage(s,item)
        # save('qb.txt',count.text)
        # count.encoding = 'utf8'
        # print(count.text)
        count1 = etree.HTML(count.text)
        title1 = count1.xpath("//div[@class='post_content_main']/h1/text()")
        time1 = count1.xpath("//div[@class='post_time_source']/text()")
        content = count1.xpath("//div[@class='post_text']/p/text()")
        result = str(title1 + time1 + content)
        result1 = result.strip()
        save('qb2.txt',result1+'\n')
        print(n)
        n +=1
        # yield {
        #     'title':title1[-1],
        #     'time':time1[-1],
        #     'countent':content[-1]
        # }
        # print(qu)
        # pattern = re.compile('<div>.*?<h1 class>(.*?).*?</h1></div>',re.S)
        # title = re.findall(pattern,count)
        # print(title)

    # print(re3)
    # for item in re3:

        # print(item)
    # save('index2.txt',r.text)


if __name__ == '__main__':
    main()
else:
    print("import")
# //div[@class="post_content_main"]/h1/text()　＃标题
#//div[@class="post_time_source"]/text()　＃时间
# //div[@class="post_text"]/p/text()  #内容