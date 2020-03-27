import requests
base_url='https://fanyi.baidu.com/sug'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


kw=input('qingshuru:' )

data={
    'kw':kw,
}

response=requests.post(url=base_url,headers=headers,data=data)
print(response.json()['data'])
