# 1.导入requests
import requests

# 分页规律
# 第一页：https://voice.hupu.com/nba/1
# 第二页：https://voice.hupu.com/nba/2
# 第三页：https://voice.hupu.com/nba/3
# 第n页：https://voice.hupu.com/nba/n

# 2.定义基础URL
base_url = 'https://voice.hupu.com/nba/{}'

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

for i in range(1,11):
    new_url = base_url.format(i)
    print(new_url)

    # 3.发起请求
    response = requests.get(url=new_url,headers=headers)

    # 4.写入文件
    with open('hupu'+str(i)+'.html','w',encoding='utf-8') as fp:
        fp.write(response.text)


