# 1.导入requests
import requests

# 2.定义基础URL
base_url = 'http://search.sina.com.cn/'
# 网址参数：
# ?后面的是参数，每一个参数的形式类似于字典,每个参数之间使用&符号进行连接

q = input('请输入想要查找的网页：')
# 自定义参数
params = {
'q': q,
'c': 'news',
'from': 'index'
}

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 3.发起请求
# 使用params，会自动的将字典中的参数，拼接到网址后面
response = requests.get(url=base_url,headers=headers,params=params)

print(response.url)

# print(response.text)



