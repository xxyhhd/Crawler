import requests
r = requests.get('http://www.baidu.com')
# 输出r的类型，<class 'requests.models.Response'>
print(type(r))
# 输出HTML头信息
print(r.headers)
# 网页状态码
print(r.status_code)
# 从页面头部猜测的编码方式和页面内容的编码方式
print(r.encoding, r.apparent_encoding)
# 修改编码格式
r.encoding = 'utf-8'
# 输出内容
print(r.text)

# 简约框架
try:
    r = requests.get(url, timeout=30)
    r. raise_for_status()  # 如果返回的状态吗不是200，抛出异常
    r.encoding = r.apparent_encoding
    return r.text
except:
    return '产生异常'


"""
requests库的主要方法：
	    方法	                           说明
	requests.request()	构造一个请求，支撑以下各方法的基础方法
	requests.get()	    获取HTML页面的主要方法，对应HTTP的GET
	requests.head()	    获取HTML页面头信息的方法，对应HTML的HEAD
	requests.post()	    获取HTML页面提交post请求的方法，对应HTML的POST
	requests.put()	    获取HTML页面提交PUT请求的方法，对应HTML的PUT
	requests.patch()	获取HTML页面提交局部修改的方法，对应HTML的PATCH
	requests.delete()	获取HTML页面提交删除请求的方法，对应HTML的delete

"""


"""
requests.request(method, url, **kwargs)
    method:请求方式，对应get/post/put等七种，增加一个options
    url:获取页面的url链接
    **kwargs:控制访问的参数，共13个
        1. params:字典或字节序列，作为参数增加到url中，下面是例子
            kv = {'key1': 'value1', 'key2': 'value2'}
            b = requests.request('GET', 'http://python123.io.ws', params=kv)
            print(b.url)
            http://python123.io.ws/?key1=value1&key2=value2
        2. data
            kv = {'key1': 'value1', 'key2': 'value2'}
            b = requests.request('POST', 'http://python123.io.ws', data=kv)
            body = '主题'
            c = requests.request('POST', 'http://python123.io.ws', data=body)
        3. json: JSON格式的数据，作为request的内容
            kv = {'key1': 'value1'}
            b = requests.request('POST', 'http://python123.io.ws', json=kv)
        4. headers: 字典，HTTP定制头
            hd = {'user-agent': 'Chorm/10'}
            b = requests.request('POST', 'http://python123.io.ws', headers=hd)
        5. cookies: 字典或者CookieJar, request中的cookie
        6. auth: 元组，支持HTTP认证功能
        7. files：字典类型，传输文件
            fs = {'file': open('data.xls', 'rb')}
            b = requests.request('POST', 'http://python123.io.ws', files=fs)
        8. timeout: 设定超时时间，以秒为单位，如果设定时间内容没有返回数据，timeout异常
            b = requests.request('GET', 'http://python123.io.ws', timeout = 10)
        9. proxies： 字典类型，设定访问代理服务器，可以增加登录认证，隐藏原用户
            pxs = {'http': 'http://user:pass@10.10.10.1:1234'
            'https': 'https://10.10.10.1:4321' }
            b = requests.request('POST', 'http://python123.io.ws', proxies=pxs)
        10. allow_redirects: True/False, 默认True, 重定向开关
        11. stream: True/False, 默认True, 获取内容自动下载开关
        12. verify: True/False, 默认True, 认证SSL证书的开关
        13. cert: 保存本地SSL证书路径

requests.get(url, params=None, **kwargs)
    url: 获取页面的url链接
    params: url中的额外参数，字典或者字节流格式，可选
    **kwargs: 12个控制访问的参数，可选，与requests.request完全一样

requests.head(url, **kwargs)
    **kwargs: 13个控制访问的参数，可选，与requests.request完全一样

requests.post(url, data=None, json=None, **kwargs)
    url: 需要更新页面的url链接
    data: 字典、字节序或者文件，request的内容
    json：JSON格式的数据，request的内容
    **kwargs: 11个控制访问的参数，与requests.request一样

requests.put(url, data=None, **kwargs)
    url: 需要更新页面的url链接
    data: 字典、字节序或者文件，request的内容
    **kwargs: 12个控制访问的参数，与requests.request一样

requests.patch(url, data=None, **kwargs)
    url: 需要修改页面的url链接
    data: 字典、字节序或者文件，request的内容
    **kwargs: 12个控制访问的参数，与requests.request一样

requests.delete(url, **kwargs)
    **kwargs: 13个控制访问的参数，可选，与requests.request完全一样


"""

"""
Response对象的属性
    r.status_code           HTTP请求的返回状态，200代表成功
    r.text                  HTTP响应内容的字符串格式，即url对应的页面内容
    r.encoding              从HTTP header中猜测的响应内容编码方式，如果header中不存在charset字段，默认是ISO-8859-1编码方式
    r.apparent_encoding     从内容中分析出的响应内容的编码方式（备选编码方式）
    r.content               HTTP响应内容的二进制形式
"""

"""
requests库中的异常
    requests.ConnectionError        网络连接异常，如DNS查询失败，拒绝连接等
    requests.HTTPError              HTTP错误异常
    requests.URLRequired            URL缺少异常
    requests.TooManyRedirects       超过最大重定向次数，产生重定向异常
    requests.ConnectTimeout         连接远程服务器超时异常
    requests.Timeout                请求URL超时，产生超时异常
"""

"""
r.raise_for_status()  如果状态吗不是200，会抛出requests.HTTPError异常，配合try,except使用
"""

"""
HTTP协议
HTTP, Hypertext Transfer Protocol，超文本传输协议
HTTP是一个基于“请求与响应”模式的、无状态的应用层协议，无状态：用户的每次请求没有关联
HTTP协议采用URL作为定位网络资源的标识
URL格式：http://host[:port][path]
    host:合法的Internet主机域名或者IP地址
    port:端口号
    path：请求资源的路径
"""

"""
HTTP协议对资源的操作
    GET         请求获取URL位置的资源
    HEAD        请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
    POST        请求向URL位置的资源后附件新的数据
    PUT         请求向URL位置存储一个资源，覆盖原URL位置的资源
    PATCH       请求局部更新URL位置的资源，即改变该处资源的部分内容
    DELETE      请求删除URL位置存储的资源
    path和put的区别：
        假设url位置有一组数据userinfo,包括userid,username等20个，现在只需要更改username，其他不变
        patch方法，仅向url提交username局部更新请求
        put方法，必须将所有字段一并提交，未提交字段将会删除
"""

"""
网络爬虫的尺寸：
    1. 小规模，数据量小，爬取速度不敏感，爬取网页，玩转网页，可以使用requests库
    2. 中规模，数据规模较大，爬取速度敏感，爬取网站，爬取系列网站，用scrapy库
    3. 爬取全Internet全网，大规模，搜索引擎，定制开发
网络爬虫引发的问题：
    1. 对服务器的骚扰问题
    2. 法律风险
    3. 个人用户隐私泄露
"""

"""
限制网络爬虫的方法：
    1. 来源审查: 判断user-agent进行限制
        检查来访HTTP协议头的user-agent，只响应浏览器或者友好爬虫的访问
    2. 发布公告：robots协议
        告知爬虫者该网站的爬取策略，要求爬虫遵守，是君子协议，道德上的约束
        robots协议：robots exclusion standard 网络爬虫排除标准
        形式：在网站根目录下的robots.txt文件
        如果一个网站没有改文件，默认允许所有爬虫
"""