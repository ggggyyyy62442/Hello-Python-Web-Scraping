#json.dumps() - 把 Python对象 → JSON字符串
#json.loads() - 把 JSON字符串 → Python对象
#ensure_ascii=False：处理中文时一定要加，不然变乱码
#带 s 的是处理字符串（string）不带 s 的是处理文件
#get and post

#urllib 的 .read() = requests 的 .get()
import requests

query = input("请输入搜索内容：")

url = f"https://www.sogou.com/web?query={query}" #f string 表示把某一个变量的值，直接嵌入到字符串中
dic= {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Cache-Control": "max-age=0",
}
#完整的 headers，模拟真实浏览器

resp = requests.get(url, headers=dic)

with open(f"query={query}.html",mode="w",encoding="utf-8") as f:
    f.write(resp.text)

print("over")


# 附录：How to check Python version

# import sys
# print("=== Python 信息 ===")
# print(f"Python 版本: {sys.version}")
# print(f"Python 路径: {sys.executable}")
# print(f"模块搜索路径:")
# for path in sys.path:
#     print(f"  {path}")


# How to check the installed version of requests

# print("\n=== 尝试导入 requests ===")
# try:
#     import requests
#     print(f"✅ requests 版本: {requests.__version__}")
#     print(f"✅ requests 路径: {requests.__file__}")
# except ImportError as e:
#     print(f"❌ 导入失败: {e}")
#     print("\n=== 解决方案 ===")
#     print("1. 在终端运行: pip install requests")
#     print("2. 或在 VS Code 中按 F1 → 'Python: Select Interpreter'")
#     print("3. 选择正确的 Python 版本")



# How to use len to get content length in html response

# import requests

# url = "https://www.sogou.com/web?query=bilibili"
# here can add headers if needed
# resp = requests.get(url, headers=headers)
# print(resp.status_code)  # 应该返回 200
# print(len(resp.text))    # len获取内容长度