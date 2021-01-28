# -*- coding: utf-8 -*-
import scrapy
from zol_SPJK.items import ZolSpjkItem
import urllib.request
import lxml.html

class hqbpcspider(scrapy.Spider):
	name = 'hqbpc'
	allowed_domains = ['product.hqbpc.com']
	start_urls = ['http://product.hqbpc.com/server_index/products_brand1573_1.html']
	def parse(self, response):
		zol_list = response.xpath("//div[@id='body_center']/div[@class='clear_div i_n_right']/div[@class='clear_div i_center']/div[@class='clear_div blue_border i_left']/div[1]/span")
		for i_item in zol_list:
			zol_item = ZolSpjkItem()
			zol_item['brand'] = response.xpath("//div[@id='body_center']/div[1]/div[1]/div/dl[1]/dd/a[@class='search_light']/text()").extract_first() 
			zol_item['name'] = i_item.xpath(".//dl[1]/dd[1]/a/text()").extract_first() 
			zol_item['typeBig'] = '服务器'
			if zol_item['name'] != None:
				yield zol_item

		#该中类、品牌下翻页
		next_link = response.xpath("//div[@class='clear_div down_page']/dl/dd/div[@class='page']/a[text()='Next']/@href").extract()
		if next_link:
			next_link = next_link[0]
			yield scrapy.Request(next_link,callback=self.parse)
'''
		#对于不同品牌选择
		next_link_brand = response.xpath("//div[@class='clear_div yellow_border i_class_nav_c']/dl[@class='clear_div i_class_nav']/dd/a[@class='search_light']/following-sibling::a/@href").extract()
		print("==================")
		print(response.xpath("//div[@class='clear_div yellow_border i_class_nav_c']/dl[@class='clear_div i_class_nav']/dd/a[@class='search_light']/following-sibling::a/text()").extract())
		print(next_link_brand)
		if next_link_brand:
			next_link_brand = next_link_brand[0]
			yield scrapy.Request(next_link_brand,callback=self.parse)
'''