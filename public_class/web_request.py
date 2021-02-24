#Web请求流程
# url:统一资源定位符。实际上就是用来表示资源的那台web服务器的位置上的一个地址
#     https://image.baidu.com/search/index?tn=baiduimage
#     url组成：
#         协议头:http://  https://
#         域名或主机：image.baidu.com
#         路径：/search/index
#         GET请求：?tn=baiduimage
#     http请求
#         当我们向网络获取资源
#         1、发生web服务器请求
#            URL告诉web服务器我们想要得到的资源的位置
#            header身份头用来表示请求的身份，cookie
#            post/get Data请求的数据
#         2、Web服务器的响应
#            Response header 资源头部
#            资源本身

# urllib和urllib2是Python内置的发起web请求的模块
# urllib2.request 向服务器发起请求
#     url地址
#     data 请求携带的数据
#     headers请求的头部
# urllib2.urlopen()可以将请求返回的内容转换成文件格式
#     urllib.urlretrieve()保存，将指定的地址资源保存到本地

# Xpath来源于Python lxml模块，是一种结构性匹配字符串的功能
# 字符串的匹配
#     Re是通过描述要匹配的内容的类型和数量来匹配内容的
#         优点：正则匹配精准度很高，但是难度也很大
#     Xpath是通过描述匹配内容在总内容中的结构进行匹配。
#         优点：结构匹配很容易且适合大规模的匹配。必须有规定的结构才可以使用
