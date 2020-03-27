# 1.导入requests
import requests

# 2.定义基础url
base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 3.发起请求
response = requests.get(url=base_url,headers=headers)

# 将json数据转换成python字典
dic_response = response.json()
dic = {}
for data in dic_response:
    # 获取排名
    rank = data['rank']
    # print(rank)
    # 获取影片类型
    type = data['types']
    # print(type)
    # 获取标题
    title = data['title']
    # 获取国家
    regions = data['regions']
    # 上映时间
    release_date = data['release_date']
    # 评分
    score = data['score']
    # 演员
    actors = data['actors']

    dic['rank'] = rank
    dic['type'] = type
    dic['title'] = title
    dic['regions'] = regions
    dic['release_date'] = release_date
    dic['score'] = score
    dic['actors'] = actors

    with open('douban.txt','a',encoding='utf-8') as fp:
        fp.write(str(dic)+'\n')







