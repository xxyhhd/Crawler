import re
'''
正则表达式常用操作符
    操作符              说明                                        实例
    .               表示匹配除换行符意外的所有字符
    []              字符集，对单个字符给出取值范围              [abc]表示a,b,c; [a-z]表示a-z单个字符
    [^]             非字符集，对给出的字符排除范围
    *               前一个字符0次或无限次扩展                   abc*表示ab,abc,abc,abcc,abcccc
    +               前一个字符一次或者无限次扩展
    ？              前一个字符0次或者1次扩展
    |               左右表达式任选一个                          abc|def 表示abc或者def
    {m}             扩展前一个字符m次                           ab{2}c表示abbc
    {m,n}           扩展前一个字符m至n次（包括n）
    ^               匹配字符串开头                              ^abc表示abc在一个字符串的开头
    $               匹配字符串结尾                              abc$表示abc在一个字符串的结尾
    ()              分组标记，内部只能用|操作符                  (abc)表示abc,(abc|def)表示abc,def
    \d              数字，等价[0-9]
    \w              单词字符，匹配任意英文单词和数字和_下划线

    IP地址
    由0-99，100-199，200-249，250-255组合而成
    （([1-9]\d?|1\d{2}|2[0-4][0-9]|25[0-5]).){3}（[1-9]\d?|1\d{2}|2[0-4][0-9]|25[0-5])

'''
'''
re库采用raw string类型表示正则表达式，表示为：r'str'
例如：r'我是字符串'
raw string是原生字符串，是不包含转义字符的字符串
也可以用string类型，但是更繁琐，需要用'\'进行转义

re库主要功能函数：
import re
    re.search()             在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
    re.match()              从一个字符的开始位置起匹配正则表达式，返回match对象
    re.findall()            搜索字符串，以列表类型返回全部能匹配的字符串
    re.split()              将一个字符串按正则表达式结果进行分割，返回列表
    re.finditer()           搜索字符串，返回一个匹配结果的迭代对象，每个迭代对象都是match对象
    re.sub()                在一个字符串中替换所有匹配正则表达式的字符串，返回替换后的字符串

        match对象的属性：
            .string     待匹配的文本
            .re         匹配时使用的pattern对象，正则表达式
            .pos        正则表达式搜索文本的开始位置
            .endpos     正则表达式搜索文本的结束位置
        match对象的方法：
            .group(0)   获得匹配后的字符串
            .start      匹配字符串在原始字符串的开始位置
            .end        匹配字符串在原始字符串的结束位置
            .span()     返回（.start(),.end()）,元组类型

    re.search(pattern, string, flags=0)
        pattern : 正则表达式
        string ：待匹配字符串
        flags：正则表达式使用时的控制标记
            re.I: 忽略正则表达式的大小写，[a-z]能匹配大写字母
            re.M: 正则表达式的^匹配字符串的开头，加上re.M之后匹配字符串每一行的开始
            re.S: 正则表达式中的.匹配所有字符，默认匹配除换行符以为的所有字符，加上re.S之后匹配所有
    re.match()同search
    findall同
    re.split(pattern, string, maxsplit=0, flags=0)
    多了一个maxsplit, 最大分割次数，剩余部分作为一个整体输出
    re.finditer同search
    re.sub(pattern, repl, string, count=0, flags=0)
    repl是替换之后的字符串
    '''
str1 = 'BIT 100081'
str2 = '100081 BIT'

match1 = re.search(r'[1-9]\d{5}', str1)  #返回match对象
if match1:
    print(match1.group(0))
    print(match1.string, match1.re, match1.pos, match1.endpos)

match2 = re.match(r'[1-9]\d{5}', str2)  # 返回match对象
if match2:
    print(match2.group(0))

match3 = re.findall(r'[1-9]\d{5}', str2)  # 返回列表
print(match3)

match4 = re.split(r'\d', str2, maxsplit=3)  # 返回列表
print(match4)

'''
上面的输出
100081
BIT 100081 re.compile('[1-9]\\d{5}') 0 10
100081
['100081']
['', '', '', '081 BIT']
'''

for x in re.finditer(r'\d', str2):
    if x:
        print(x.group(0))
'''
1
0
0
0
8
1
'''

match5 = re.sub(r'\b', 'a', str2, count=6,)
print(match5)
# a100081a aBIT

'''
以上方法是函数性用法，一次性操作
rst = re.search(r'\d', str2)

面向对象用法,编译后的多次操作，需要用同一个正则表达式匹配多次时，
    re.compile(pattern, flags=0), 把正则表达式编译成一个对象
    pat = re.compile(r'\d')
    rst = pat.search('str2')
'''

贪婪匹配和非贪婪匹配
    贪婪匹配，在RE库，贪婪匹配默认匹配最长的字符串
    re.search(r'py.*n', 'pyqnwenrrnwwsn')
    原字符串有很多子字符串符合正则表达式，贪婪匹配下返回最长的字串
        re.search(r'py.*？n', 'pyqnwenrrnwwsn')，匹配最短子串

    最小匹配操作符
    *？         前一个字符0次或无限次扩展，最小匹配
    +？         前一个字符一次或无数次扩展，最小匹配
    ？？        前一个字符0次或1次匹配，最小匹配
    {m,n}       扩展前一个字符m至n次（含n）,最小匹配

