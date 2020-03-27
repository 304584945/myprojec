# 1.导入requests
import requests

# 分页规律
# 第一页：https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
# 第二页：https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50
# 第三页：https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100
# 第四页：https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=150
# 第n页： https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=(n-1)*50

# 2.定义基础URL
base_url = 'https://tieba.baidu.com/f'
# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 定义自定义查询
kw = input('请输入想要查看的贴吧名：')

# 定义参数
params = {
'kw': kw,
'ie': 'utf-8',
}

for i in range(1,6):
    # 拼接新的url
    params['pn'] = (i-1)*50
    # 3.发起请求
    response = requests.get(url=base_url,headers=headers,params=params)
    print(response.url)

    # 4.写入文件
    with open('{}{}.html'.format(kw,i),'w',encoding='utf-8') as fp:
        fp.write(response.text)









