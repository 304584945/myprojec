# 1.导入requests
import requests

#2.定义url
base_url = 'https://www.baidu.com/more/'

# 3.发起请求,获取响应,get还是hold根据 request method 选择
response = requests.get(url=base_url)
print(response.status_code)#查看状态码
# text   获取页面文本内容
# print(response.text)

# content   获取页面的二进制内容
print(response.content)

# 可以使用response.content.decode()  解决乱码问题
print(response.content.decode())







