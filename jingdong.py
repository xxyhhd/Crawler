import requests
url = 'https://item.jd.com/100001928617.html'
try:
    hd = {'user-agent': 'Chorm/10'}
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)  # 输出当前请求的header信息
    # print(r.text[:1000])
except:
    print('爬取失败')