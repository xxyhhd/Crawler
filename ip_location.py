import requests

url = 'http://ip138.com/ips138.asp'
url_2 = "http://ip138.com/ips138.asp?ip="

try:
    kv = {'ip': '8.8.8.8'}
    r = requests.get(url, params=kv)
    r_2 = requests.get(url_2 + '8.8.8.8')
    r.raise_for_status()
    print(r.request.url)
    print(len(r_2.text))
except:
    print('爬取失败')