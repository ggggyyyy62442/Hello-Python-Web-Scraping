import requests
import re
import csv

url = "https://movie.douban.com/top250"


dic = {
    "User-Agent":   "your UA"
}
resp = requests.get(url, headers=dic)

page = resp.text

o = re.compile(
    r'<div class="info">[\s\S]*?'
    r'<span class="title">(?P<title>[^<]+)</span>[\s\S]*?'  # 使用[\s\S]*?而不是.*?
    r'导演:\s*(?P<director>[^<&]+)(?:\s*&nbsp;|\s*<br>)[\s\S]*?'
    # r'<div class="info">.*?<div class="hd">.*?<span class="title">(?P<title>.*?)</span>'
    # r'</span>.*?导演:(?P<director>.*?)&nbsp;'
    r'<br>\s*(?P<year>\d{4})\s*&nbsp;/&nbsp;[\s\S]*?'
    r'<span class="rating_num"[^>]*>(?P<rate>[\d.]+)</span>',
    re.S)



result = o.finditer(page)
with open("豆瓣top250.csv",mode="w") as f:
    cs = csv.writer(f)

    cs.writerow(["标题", "导演", "年份", "评分"])
    count = 0
    for it in result:
        count += 1
        print("正在写入第%d条数据" % count)

        title = it.group("title").strip()
        director = it.group("director").strip()
        year = it.group("year").strip()
        rate = it.group("rate").strip()
    # print("名字：",it.group("title").strip())
    # print("导演：",it.group("director").strip())
    # print("年份：",it.group("year").strip())
        di = it.groupdict()
  #strip() 去掉空格和换行符 
        cs.writerow(di.values())
        print(f"第{count}部：{title}")

resp.close()

print("over")
