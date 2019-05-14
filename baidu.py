import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}

request = urllib.request.Request(url=url, headers=headers)
reponse = urllib.request.urlopen(request)
print(reponse.getcode())
