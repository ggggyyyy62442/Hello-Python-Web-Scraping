import requests

url = "https://fanyi.baidu.com/sug"
# url = "https://fanyi.baidu.com/ait/text/translate"

a = input("请输入要翻译的单词：")
dat = {
    "kw": a
}

dic = {
    "Referer": "https://fanyi.baidu.com/",
    "Origin": "https://fanyi.baidu.com",
    "User-Agent": "your UA"
}

res = requests.post(url, data=dat, headers=dic)
print("状态码:", res.status_code)
print(res.json())

# 对于headers，不是必须全部都写上，只要包含必要的就行，比如 User-Agent，Referer，Origin 等等。
# 百度翻译的sug接口只可以翻译单词，如果是翻译句子的话需要用别的接口
