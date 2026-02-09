import requests

url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": 11,
    "interval_id": "100:90",
    "action": "start",
    "start": 0,
    "limit": 20
}
# 使用params传递参数
dic = {
    "User-Agent": "your UA"
}

response = requests.get(url=url, headers=dic, params=param)

with open ("doubanlist.html", mode="w") as f:
    f.write(response.text)

print("Status Code:", response.status_code)
# print("Response Body:", response.json())
response.close()
