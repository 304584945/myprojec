# 1.导入requests
import requests
# 2.定义基础的URL
base_url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&rsv_t=5118Nbl%2Bv99QB9horeYRZVJ27mFiucAyvpGTahTAejCsDVBLEeHh3rKX87Y&rsv_enter=0&rsv_dl=tb&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&prefixsug=python&rsp=3&inputT=5284&rsv_sug4=8131&rsv_sug=2'

# 构建请求头,以后写代码，必须加上
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 3.发起请求
response = requests.get(url=base_url,headers=headers)
print(response.request.headers)
# print(response.text)
# with open('BaiDuSouSuo.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)
# print(response.request.headers)   # 查看默认请求头

# with open('sousuo.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)







