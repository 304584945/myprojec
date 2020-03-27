# 1.导入requests
import requests
# 2.定义基础的URL
base_url = 'https://www.baidu.com/s'

# 快捷方法  第一行：(.*): (.*)   第二行：'$1': '$2',
# (.*): (.*)
# .代表匹配除了换行符'\n' 以外的所有单个字符
# *代表匹配前一个字符无数次（0次、1次、无数次）
# ()代表分组，标记一个子表达式的开始和结束的范围

wd = input('请输入想要查询的网页：')
# 自定义参数
params = {
'ie': 'utf-8',
'tn': 'baidu',
'wd': wd,
}

# 构建请求头,以后写代码，必须加上
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'BIDUPSID=C8C672385FB5F145533A95D32FF1207B; PSTM=1585104794; BAIDUID=C8C672385FB5F145DC4973E12E98353A:FG=1; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=5d15e2e7e5c9748506b70cc403136d57b860f537_1585111812_js; BD_HOME=1; H_PS_PSSID=30971_1447_31170_21100_31069_31055_30824_26350; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=ba79q%2FLazbn%2Bvzya%2BQxhNV6WIgbfsgATw%2BmKyGinSG3LI3VFc1jiw0q278Q; COOKIE_SESSION=58_0_4_6_0_6_0_0_4_5_2_2_0_0_0_0_0_0_1585125176%7C9%230_0_1585125176%7C1; BDSVRTM=533',
'Host': 'www.baidu.com',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

# 发起请求
response = requests.get(url=base_url,headers=headers,params=params)
print(response.encoding)

# 写入文件
with open(wd+'.html','w',encoding='ISO-8859-1') as fp:
    fp.write(response.content.decode('ISO-8859-1'))
# print(response.url)

