
import requests
headers={
# 'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Accept-Encoding':' gzip, deflate, br',
# 'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8',
# 'Cache-Control':' max-age=0',
# 'Connection':' keep-alive',
# 'Cookie: BIDUPSID=DD50BAD9CC4446BC23CB06E6C843FDE4; PSTM=1554882894; TIEBA_USERTYPE=217c8d3eae71a469d3a93606; bdshare_firstime=1555076065003; TIEBAUID=d4a19701f1d332e972fdb848; BDUSS=zhkMGdybThrWFhMSFhxcWpNdDZJZE1QQ1NhbThmbjZvWWZGTGg4Z3g1TS1QUTllRVFBQUFBJCQAAAAAAAAAAAEAAACqmHsdMzA0NTg0OTQ1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD6w510-sOddY; BAIDUID=1C8BEB35AD321C3CE6DE4A43CF1F3F56':'FG=1; STOKEN=12d76643a0a3c82f14c2f4158dfba34f9064f9c25f769f93a4b2991915020602; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; cflag=13%3A3; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1584712468,1584936169,1585127529,1585130345; 494639274_FRSVideoUploadTip=1; st_key_id=17; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=30971_1428_31118_21105_30906_30823_31085_26350; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1585132018; st_data=20299af7901f4eabcfea4203b7fd0e5e69b29092960186cf939ce1b420d59eaca4938b199be681a096a8addefdcf751f38fd14d7657c239e7153317fcd31be6d72646b82dd2b5151a0fd565b6d18d1c7c18790d696ec0fb591620ad760a9427dc37f6470469ec83c0610330221997cd592ea4f024dd532f30f738744aeca8a57; st_sign=79ffe811',
# 'Host':' tieba.baidu.com',
# 'Referer: https':'//tieba.baidu.com/index.html',
# 'Sec-Fetch-Mode':' navigate',
# 'Sec-Fetch-Site':' same-origin',
# 'Sec-Fetch-User':' ?1',
# 'Upgrade-Insecure-Requests':' 1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}
base_url = 'https://tieba.baidu.com/f'

for i in range(0,550,50):
     params = {
          'kw': '%E6%9D%8E%E6%AF%85',
          'ie': 'utf-8',
          'pn': i,
     }
     response = requests.get(url=base_url,headers=headers,params=params)
     print(response.url)
     with open('dadi'+str(i/50+1)+'.html','w',encoding='utf-8') as fp:
          fp.write(response.content.decode())
# 4.属性：
# 4.1 status_code   查看状态码
# print(response.status_code)  # 200  返回200代表成功
# print(response.encoding)
# 4.2 url   查看当前请求的URL
# print(response.url)

# 4.3 text   返回字符串类型的数据
# print(response.text)   # 页面源代码
# print(type(response.text))   # str

# 4.4 content   返回二进制类型(字节流)的数据
# print(response.content)
# print(type(response.content))   # <class 'bytes'>


# 解决乱码问题
# print(response.content.decode())

# 写入文件
# 格式：
# with open('sina.html','w',encoding='gbk') as fp:
#      fp.write(response.content.decode(gbk))
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
# with open('bilibili.html','wb') as fp:
#      fp.write(response.content)


# 写入字符串：
# with open(文件名,打开文件的方式,encoding='编码') as fp:
#     fp.write(response.content.decode() 或者 response.text)


