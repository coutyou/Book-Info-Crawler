# BookInfoCrawler
using scrapy to get the information of the books on Dangdang
## 开发环境
* python 3.6
* scrapy 1.5.0
* win10
## 运行方式
### 1.命令行
* 命令行切换到下载的文件夹目录
* 运行命令scrapy crawl dangdang
### 2.IDE
* 运行start.py
## 补充说明
* 爬取的数据默认保存至C:\\bookinfo文件夹中
* 默认爬取1-2页的内容可到pipelines.py中修改
* 爬取的内容为商品名、商品评论数、商品价格、商品地址、出版社、商品图片
