# 1.导入etree
from lxml import etree

str = 	'<html>' \
            '<bookstore>' \
                '<book>' \
                    '<title lang="eng">哈利波特</title>' \
                    '<price>29.99</price>' \
                '</book>' \
                '<book>' \
                    '<title lang="eng">Learning XML</title>' \
                    '<price>39.95</price>' \
                '</book>' \
            '</bookstore>' \

# 1.HTML()   将字符串转换成HTML格式的额数据，并且会将缺失的标签补充全
html = etree.HTML(str)
# print(html)
# 2.tostring()   查看转换之后的内容,返回二进制类型的数据
# 如果想要查看字符串类型，解码即可
# 如果想要显示中文，需要先编码再解码
content = etree.tostring(html,encoding='utf-8')
print(content.decode())





