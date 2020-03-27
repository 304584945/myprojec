# 局部刷新：整个页面没有进行刷新，只有当前页面的几部分改变了
# 使用Ajax这个方法实现局部刷新

# post请求不会将参数放在地址栏里，会存放在form data里面

# 1.导入requests
import requests,json

# 2.定义基础url
base_url = 'https://fanyi.baidu.com/sug'

# 构建请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


    # 自定义单词
kw = input('请输入查询的单词：')

    # 自定义参数
data = {
        'kw': kw
    }

    # 3.进行访问
response = requests.post(url=base_url,headers=headers,data=data)
    # print(response.text)   # 解释看不懂，显示的是中文编码(\u4e00 - \u9fa5)
    # print(response.content.decode())   # 解释看不懂，显示的是中文编码(\u4e00 - \u9fa5)

    # Ajax加载的数据是json类型（字典形式的字符串）
    # {"errno":0,"data":[{"k":"python","v":"n. \u87d2; \u86ba\u86c7;"},{"k":"pythons","v":"n. \u87d2; \u86ba\u86c7;  python\u7684\u590d\u6570;"}]}
    # print(type(response.text))  # <class 'str'>

    # 有两种解决方法
    # 第一种：使用json模块，
    # 1.导入json模块
    # 2.使用loads()方法：将json的数据转换成python的字典类型
    # dic_response = json.loads(response.text)
    # print(dic_response)   # {'errno': 0, 'data': [{'k': 'python', 'v': 'n. 蟒; 蚺蛇;'}, {'k': 'pythons', 'v': 'n. 蟒; 蚺蛇;  python的复数;'}]}
    # print(type(dic_response))   # <class 'dict'>


    # 第二种方法：直接使用response.json()
dic_response = response.json()
print(dic_response)
print(dic_response['data'])
    # data_list = dic_response['data']
    # for data in data_list:
    #     print(data['k'],data['v'])


