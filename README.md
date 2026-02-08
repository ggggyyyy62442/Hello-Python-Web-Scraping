# Hello-Python-Web-Scraping
A knowledge base documenting challenges and solutions from my Python web scraping learning journey that began on  2026. Includes code examples, problem summaries, and resources. Feedback and discussions are welcome!“hellopython爬虫入门中”是26年本人开始学python爬虫以来的遇到的问题总结和文件分享地，欢迎交流指导！

# Python Web Scraping Learning Journey（hellopython爬虫入门中）

**Started:** January 29, 2026  
**Purpose:** Problem summaries and resource sharing from my Python web scraping learning process  
**Status:** Ongoing learning - Welcome discussions and guidance!

This repository documents the challenges, solutions, and insights encountered while learning Python web scraping techniques.

## *test1.py* 20260129

Simply use the urllib.request library to create new files。
Write the content returned by search engines. 
Learn UTF-8.

简单调用urllin.request库，实现新建文件写入搜索引擎返回内容的效果，学习了解（utf-8)

## *request1.py* 20260202

Added specific headers to simply simulate a real browser
Implemented the effect of inputting keywords and automatically creating new files to write the returned keyword search HTML

加入了具体headers简单模拟真实浏览器，实现输入关键词，自动新建文件写入返回关键词搜索html 的效果
Also including:How to check Python version
How to check the installed version of requests library
How to use len to get content length

包括如何检查python版本，如何检查request库的安装版本，如何用len获取内容长度

## *baidufanyi.py* 20260203

Implementing a simple simulation of Baidu Translate for word translation. When
attempting sentence translation, encountered issues with being unable to locate the 
sign and token interfaces via F12, along with login failures and permission 
restrictions. Therefore, only word translation has been completed.

实现百度翻译单词翻译的简单模拟，在尝试句子翻译时，遇到无法通过f12找到接口的sign和token 登录失败没有权限的问题。所以只完成了单词翻译。

## *douban.py*  20260203

Using params to pass parameters for crawling the Douban movie rankings, simplifying URL expression.

使用params传递参数，爬取豆瓣电影排行榜，简化url表达

## *豆瓣电影top25.py* 20260205

Learning to use regular expressions to extract information from the source code of the Douban Movie Ranking, and creating a new CSV document to store the data.

学习使用正则表达式，在豆瓣电影排行榜抓取源代码中的信息，新建csv文档储存

## *电影天堂下载地址爬取.py* 20260207

Using regular expressions, it extracts links from the "2025 New Films" section to detailed movie pages. For each detail page, it performs secondary requests and parses the Chinese translated title, original title, release year, country of origin, genre, and download link. All extracted data is organized and written into the CSV file "电影天堂链接.csv" for subsequent data analysis or use.

通过 requests 模块访问电影天堂网站首页，使用正则表达式提取"2025新片精品"区域的电影详情页链接。对每个详情页进行二次请求，解析电影的中文译名、原片名、上映年份、产地、类别和下载链接。所有提取的数据被整理并写入 CSV 文件"电影天堂链接.csv"中，便于后续数据分析或使用。
