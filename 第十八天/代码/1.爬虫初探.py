# 1.导入requests
import requests

# 2.定义基础的URL（可以省略）
base_url = 'https://www.baidu.com/more/'

# 3.发起请求
# requests具体的请求方式根据网站的request method来决定
response = requests.get(url=base_url)

# 4.属性：
# 4.1 status_code   查看状态码
# print(response.status_code)  # 200  返回200代表成功

# 4.2 url   查看当前请求的URL
# print(response.url)

# 4.3 text   返回字符串类型的数据
# print(response.text)   # 页面源代码
# print(type(response.text))   # str

# 4.4 content   返回二进制类型(字节流)的数据
# print(response.content)
# print(type(response.content))   # <class 'bytes'>

# 4.5 encoding   返回的页面编码
# print(response.encoding)

# 解决乱码问题
# print(response.content.decode())

# 写入文件
# with open('BaiDuAllProducts.html','w',encoding='ISO-8859-1') as fp:
#     fp.write(response.content.decode('ISO-8859-1'))


# 写入文件
# 格式：
# with open('文件名','打开文件的方式',encoding='utf-8') as fp:
#      fp.write(response.content.decode())
# 注意：
# 1.文件名需要写到文件后缀
# 2.如果打开的文件不存在，会先创建这个文件，再打开它
# 3.打开文件的方式：
# w(写,如果以w打开文件,再往文件里面写内容，之前的内容会被覆盖掉)
# r(读,只读，不能写)
# a(追加,可以写内容，而且，之前文件中存在的内容不会被新内容覆盖掉，会把新内容加到之前的内容后面)
# wb(以二进制写的方式，打开文件) 比如：爬取图片等等
# 4.encoding='编码'  :设置编码    当你写入二进制文件时，不要加
# 5.fp只是一个名字，只要符合变量命名即可
# 6.fp.write()   往文件中写内容，当在写入二进制类型的时候，只能够使用response.content


# 总结：
# 写入二进制文件：
# with open(文件名,'wb') as fp:
#     fp.write(response.content)


# 写入字符串：
# with open(文件名,打开文件的方式,encoding='编码') as fp:
#     fp.write(response.content.decode('编码') 或者 response.text)


