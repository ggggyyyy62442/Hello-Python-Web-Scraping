import requests
import re
import csv


url = "https://dytt8.com/"
dic = {
    "your UA"
}

resp = requests.get(url,headers=dic)
resp.encoding = "gb2312" #设置编码格式，解决乱码问题
child_herf_lst = []

obj1 = re.compile(r"2025新片精品.*?<ul>(?P<url>.*?)</ul>", re.S)
re1 = obj1.finditer(resp.text)
obj2 = re.compile(r"最新电影下载</a>]<a href='(?P<detail_url>.*?)'>", re.S)

obj3 = re.compile(r" />◎译　　名　(?P<name>.*?)<br />◎片　　名　(?P<original_name>.*?)<br />◎年　　代　(?P<year>\d{4})<br />◎产　　地　(?P<nation>.*?)<br />◎类　　别　(?P<category>.*?)<br />"
                  r'.*?target="_blank" href="(?P<download_url>.*?)"><strong style'
                  ,re.S)

for it in re1:   
     ul = (it.group("url"))
     
     re2 = obj2.finditer(ul)
     for it2 in re2:        
          print(it2.group("detail_url")) 
          child_herf = url + it2.group("detail_url") #拼接成完整的链接
          child_herf_lst.append(child_herf) ## 使用append添加元素

with open("电影天堂链接.csv",mode="w") as f:
    cs = csv.writer(f)
    cs.writerow(["译名","片名","年代","产地","类别","下载链接"])


    for herf in child_herf_lst:
        resp2 = requests.get(herf,headers=dic)
        resp2.encoding = "gb2312"
        
        re3 = obj3.finditer(resp2.text)
        for it3 in re3:
                # 提取数据
            name = it3.group("name").strip()
            original_name = it3.group("original_name").strip()
            year = it3.group("year").strip()
            nation = it3.group("nation").strip()
            category = it3.group("category").strip()
            download_url = it3.group("download_url").strip()
                
                # 写入CSV
            cs.writerow([name, original_name, year, nation, category, download_url])

        resp2.close()

# 拿到链接后，继续爬取电影详情页的链接：html中，herf就是超链接
# print(resp.text)

resp.close()