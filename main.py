'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/27 15:44
@Software: PyCharm
@File    : main.py
'''
import re
import requests

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 ('
                      'KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 '
                      'Core/1.70.3650.400 QQBrowser/10.4.3341.400',
    }
    response = requests.get(url,headers=headers)
    text = response.text
    # print(text)
    users = re.findall(r'<div class="author clearfix">.*?<h2>\s(.*?)\s</h2>',
                       text,re.S)
    # print(users)
    contents = []
    content_tages = re.findall(r'<div class="content">.*?<span>(.*?)</span>',
                              text,
                          re.S)
    for content in content_tages:
        info = re.sub(r'<.*?>','',content)
        # print(info.strip())
        # print("="*30)
        contents.append(info.strip())
    duanzis = []
    for value in zip(users,contents):
        user,content = value
        duanzi = {
            'user':user,
            'conntent':content
        }
        duanzis.append(duanzi)

    for duanzi in duanzis:
        print(duanzi)
        print('='*40)


def main():
    for i in range(1,14):
        url = "https://www.qiushibaike.com/text/page/%s/" %i
        print(url)
        parse_page(url)
        break

if __name__ == '__main__':
    main()