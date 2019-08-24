# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
from scrapy.exceptions import DropItem

class DangdangPipeline(object):
    def __init__(self):
        self.title_seen = set()
        # 先创建文件路径
        file_dir = r"C:\bookinfo\pic"
        # 判断文件路径是否存在，如果不存在，则创建
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

    def process_item(self, item, spider):
        if item['title'][0] in self.title_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.title_seen.add(item['title'][0])

            print('商品名：' + item['title'][0])
            print('商品评论数：' + item['num'][0])
            print('商品价格：' + item['price'][1])
            print('商品地址：' + item['link'])
            print('出版社：' + item['cbs'][0])

            with open(r"C:\bookinfo\info.txt", "a", encoding='utf-8') as f:
                f.write('\n' + '商品名：' + item['title'][0] + '\n商品评论数：' + item['num'][0] + '\n商品价格：' + item['price'][
                    1] + '\n商品地址：' + item['link'] + '\n出版社：' + item['cbs'][0] + '\n')
            filename = r"C:\bookinfo\pic\\"+ item['pic'][0].split("/")[-1]
            with open(filename, "wb") as ff:
                ff.write(requests.get(item['pic'][0]).content)
            return item
