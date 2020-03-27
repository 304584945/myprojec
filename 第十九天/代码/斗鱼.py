

# 1.导入requests
import requests

# 2.定义基础URL
base_url = 'https://www.douyu.com/gapi/rkc/directory/2_19/'
# 定义第一次请求URL
first_url = 'https://apmconfig.douyucdn.cn/big/apm/front/config/report?client_sys=web'

# 构建请求头
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


first_response= requests.get(url=first_url,headers=headers)

data = first_response.json()['data']
httpThreshold=int(data['httpThreshold'])


for i in range(1,httpThreshold//120+1):

    # 3.发起请求
    response = requests.get(url=base_url+str(i),headers=headers)
    # 将json数据转换成python字典
    dic_response = response.json()
    dic = {}
    data=dic_response['data']
    rl=data['rl']
    rll=rl[0]
    print(rll)
    for rll in rl:
        # 获取房间号
        rid = rll['rid']

        # 获取房间名称
        rn = rll['rn']

        # 主播id
        uid =rll['uid']
        # 主播名字
        nn = rll['nn']

        c2name = rll['c2name']

        dic['rid'] = rid
        dic['rn'] = rn
        dic['uid'] = uid
        dic['nn'] = nn
        dic['c2name'] = c2name
        with open('douyuzhibo.txt', 'a', encoding='utf-8') as fp:
            fp.write(str(dic) + '\n')

