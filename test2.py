from bs4 import BeautifulSoup
import requests

r = requests.get('http://python123.io/ws/demo.html')
print(r.status_code)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')  # hrml.parser是HTML解析器
# soup2 = BeautifulSoup('<p>demo</p>', 'html.parser')  # 可以直接对HTML代码进行解析
# soup3 = BeautifulSoup(open('D://demo.html'), 'html.parser')  # 也可以将一个HTML文件打开并解析

# print(soup.prettify())   # 友好的打印出所有HTML代码
# print(soup.a.string)  # 打印a标签的字符串
# print(soup.a.parent.name)  # 打印a标签上一级标签的名字
# print(soup.a.parent.parent.name)  # 打印a标签上一级标签的上一级标签的名字

# tag = soup.a
# print(tag.attrs)   # 打印出a标签的属性
# print(tag.attrs['class'])  #打印出a标签的class属性


"""
BeautifulSoup库解析器
        解析器                          使用方法                                    条件

    bs4的HTML解析器                   BeautifulSoup(mk, 'html.parser')          安装bs4库
    ixml的HTML解析器                  BeautifulSoup(mk, 'ixml')            pip install ixml 
    ixml的XML解析器                   BeautifulSoup(mk, 'xml')             pip install ixml
    html5lib的解析器                  BeautifulSoup(mk, 'html5lib')        pip install html5lib

BeautifulSoup类的基本元素
        基本元素                                说明
        tag             标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
        name            标签的名字，<p>...</p>的名字是'p',格式：<tag>.name
        attributes      标签的属性，字典形式组织，格式：<tag>.attrs
        navigablestring 标签内非属性字符串，<>...</>中的字符串，格式：<tag>.string
        comment         标签内字符串的注释部分，一种特殊的comment类型

标签树的下行遍历
    属性                        说明
    .contents              子节点的列表，将<tag>所有儿子节点存入列表，不止标签节点，字符串节点也包括
    .children              子节点的迭代类型，与.contents类似，用户循环遍历儿子节点
    .descendants           子孙节点的迭代类型，包含所有子孙节点，用户循环遍历

"""
# print(soup.body.contents)
# print(soup.body.contents[1])


# for child in soup.body.children:
#     print(child)

# print(soup.p.co)
'''
标签树的上行遍历
    属性                    说明
    .parent         节点的父亲标签
    .parents        节点先辈标签的迭代类型，用户循环遍历先辈节点
'''

'''
标签树的平行遍历，平行遍历指拥有同一个父标签
    属性                            说明    
    .next_sibling           返回按照HTML文本顺序的下一个平行节点的标签
    .previous_sibling       返回按照HTML文本顺序的上一个平行节点的标签
    .next_siblings          返回按照HTML文本顺序的后续所有平行节点的标签，是迭代类型
    .previous——siblings     返回按照HTML文本顺序的后续所有平行节点的标签，是迭代类型
'''

'''
如果让HTML更友好的输出
print(soup.prettify())   # 友好的打印出所有HTML代码
'''
'''
信息的标记
1. 标记后的信息可形成信息组织结构，增加了信息维度
2. 标记后的信息可用于通信、存储和展示
3. 标记的结构与信息一样具有重要价值
4. 标记后的信息更有利于程序理解与运用，也利于人理解

标记语言：
    1. XML, 类似HTML的标签，用标签标记
    2. JSON
        有类型的键值对key:value
            'name':'rain'
            'name':['rain', 'one']  可以一对多
            'name':{
                'oldname':'one',
                'newname':'rain'
            }值得部分可以嵌套使用
    3. YAML
        无类型的键值对key:Value
            和JSON相比去掉了引号和各种括号
            值的文字很多时用|来表示
            name:rain
            一对多时用-表达并列关系
            name: #注释，可以添加注释
            -oldname
            -newname
            嵌套时用缩进表示
            name:
                oldname:one 
                newname:rain 
    三种标记方式比较
    XML：最早的通用信息标记语言，可扩展性好，但繁琐
    JSON：信息有类型，适合程序处理，较XML简洁
    YAML: 信息无类型，文本信息比例最高，可读性好

    使用：
    XML: Internet上信息的交互与传递
    JSON: 移动应用云端和节点的信息通信，五注释
    YAML: 各类系统的配置文件，有注释易读
'''
'''
信息提取的一般方法：
    1. 完整的解析信息的标记形式，再提取关键信息
    XML JSON YAML
    需要标记解析器，例如：bs4库的标签树遍历
    优点：信息解析正确
    缺点：提取过程繁琐，速度慢

    2. 无视标记形式，直接搜索关键信息
    搜索
    对信息的文本查找函数即可
    优点：提取过程简洁，速度较快
    缺点：提取结构准确性与信息内容相关

    3. 融合方法：结合完整解析与搜索方法，提取关键信息
    XML JSON YAML 搜索
    需要标记解析器及文本查找函数

'''
# 找出HTML中的所有链接地址

for link in soup.find_all('a'):
    print(link.get('href'))

'''
<tag>.find_all(name, attrs, recursive, string, **kwargs)
    返回一个列表类型，存储查找的结果
    name: 对标签名称检索字符串, find_all(['a','b'])，检索a标签和b标签，如果检索的标签是True,将检索所有标签
    attrs: 对标签属性检索字符串
    recursive: 是否对子孙全部检索，默认为True
    string: 对标签内容进行检索
<tag>.() 可以代替<tag>.find_all
    扩展方法：
    方法                        说明（参数都和find_all一样）
    .find()                     搜索且只返回一个结果，字符串类型
    .find_parents()             在先辈节点中搜索，返回列表类型
    .find_parent()              在先辈节点中返回一个结果，返回字符串类型
    .find_next_siblings()       在后续平行节点中搜索，返回列表类型
    .find_next_sibling()        在后续平行节点搜索返回一个结果，字符串类型
    .find_previous_sibling()    在前续平行节点搜索返回一个结果，字符串类型
    .find_previous_siblings()   在后续平行节点搜索，返回列表类型
'''

            