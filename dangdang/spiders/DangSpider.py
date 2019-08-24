# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from dangdang.items import DangdangItem

class DangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ["http://category.dangdang.com/pg{}-cp01.05.16.00.00.00.html".format(i) for i in range(1, 3)]

    def parse(self, response):
        url_list = response.xpath('//a[@name="itemlist-title"]/@href').extract()
        for url in url_list:
            yield Request(url, callback=self.parse_name)

    def parse_name(self, response):
        items = DangdangItem()
        items['title'] = response.xpath('//*[@id="product_info"]/div[1]/h1/@title').extract()
        items['num'] = response.xpath('//*[@id="comm_num_down"]/text()').extract()
        items['link'] = response.url
        items['price'] = response.xpath('//*[@id="dd-price"]/text()').extract()
        items['cbs'] = response.xpath('//*[@id="product_info"]/div[2]/span[2]/a/text()').extract()
        items['pic'] = response.xpath('//*[@id="largePic"]/@src').extract()
        yield items
