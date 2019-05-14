"""
在百度和360搜索引擎上搜索关键字
百度搜索引擎关键词接口：http:www.baidu.com/s?wd=keyword
360:http://www/so/com/s?q=keyword
"""
import requests

url = 'http://www.baidu.com/s'
keyword = {"wd": "python"}
try:
    c = requests.get(url, params=keyword)
    c.raise_for_status()
    print(c.request.url)
    print(c.text[0:1000])
except:
    print('爬取失败')
