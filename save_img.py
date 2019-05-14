# 保存网页上的图片到本地

import requests
import os

url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=530090170,1803130651&fm=27&gp=0.jpg'
path = './' + url.split('/')[-1]  # 保留之前的名字
try:
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('保存成功')
    else:
        print('文件已存在')
except:
    '保存失败'