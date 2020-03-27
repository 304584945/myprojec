#第一页 https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
#第二页 https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20
#第三页 https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=40&limit=20
#第n页  https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=(n-1)*20&limit=20

# 1.导入requests
import requests

# 2.定义基础URL
base_url = 'https://movie.douban.com/j/chart/top_list'
# 定义第一次请求URL
first_url = 'https://movie.douban.com/j/chart/top_list_count?type=24&interval_id=100%3A90'


# 构建参数
params = {
'type': '24',
'interval_id': '100:90',
'action': '',
'limit': '20'
}

# 构建请求头
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 请求first_url获取total值
first_response= requests.get(url=first_url,headers=headers)
# 获取total
total = first_response.json()['total']

# 一共有多少页？我们知道一页有20条数据
# total//20 + 1

for i in range(0,total//20+1):
    params['start'] = i*20
    # 3.发起请求
    response = requests.get(url=base_url,headers=headers,params=params)
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

        with open('doubanJJ.txt', 'a', encoding='utf-8') as fp:
            fp.write(str(dic) + '\n')



