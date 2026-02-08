from urllib.request import urlopen

url = "http://www.bing.com"
resp = urlopen(url)

with open("mybing.html",mode="w") as f: #若文件不存在：自动新建这个文件；若文件已存在：清空文件原有内容，重新写入
    f.write(resp.read().decode("utf-8")) #f的意思是文件简写，只在with中有效，后面通过f.xxx就能对文件执行「写 / 读」操作
print("over")