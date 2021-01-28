# -*- coding: utf-8 -*-
import scrapy
from zol_SPJK.items import ZolSpjkItem
import urllib.request
import lxml.html
'''
【仅供中关村在线网使用，使用规则：爬取二级类，手动修改start_urls即可（选中要爬取的二级类的第一个品牌）】
【智能家居】
智能插座：http://detail.zol.com.cn/intelligentsocket/bull/
智能开关：http://detail.zol.com.cn/intelligentswitch/chuguan/
智能传感器：http://detail.zol.com.cn/intelligent-sensor/ouruibo/
智能机器人：http://detail.zol.com.cn/intelligent_robot/abilix/
智能音箱：http://detail.zol.com.cn/intelligentvoiceassistant/xiaomi/
智能灯光：http://detail.zol.com.cn/intelligentledlamp/adol/
智能摄像机：http://detail.zol.com.cn/smart-camera/yingshi/
智能门锁：http://detail.zol.com.cn/doorbell/loock/
智能电子猫眼：http://detail.zol.com.cn/electronic_eye/eques/
智能马桶盖：http://detail.zol.com.cn/toilet-seat/panasonic/
智能窗帘：http://detail.zol.com.cn/curtain/dooya/
智能晾衣杆：http://detail.zol.com.cn/intelligent-clothes-hanger/mrbond/
智能垃圾桶：http://detail.zol.com.cn/mintpass-rubbish/eko/
智能水杯：http://detail.zol.com.cn/intelligent-water-cup/sguai/
智能创意：http://detail.zol.com.cn/the-creative-intelligence/adol/
智能套装组合：http://detail.zol.com.cn/furnishingcontroller/wulian/
'''
class SpjkSpiderSpider2(scrapy.Spider):
	name = 'SPJK2_spider'
	allowed_domains = ['detail.zol.com.cn']
	start_urls = ['http://detail.zol.com.cn/drivingmachine/conqueror/']
	def parse(self, response):
		zol_list = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='pic-mode-box']/ul/li")
		for i_item in zol_list:
			zol_item = ZolSpjkItem()
			#zol_item['brand'] = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='param-filter']/div[@class='filter_brand']/div[@class='brand-hot brand-list']/a[@class='active']/text()").extract_first()
			zol_item['brand'] = response.xpath("//div[@id='J_ParamBrand']/a[@class='active']/text()").extract_first()
			#zol_item['brand'] = '小门瞳'  
			#zol_item['name'] = i_item.xpath(".//h3/a[contains(@title,'龙业')]/@title").extract_first()    	
			#zol_item['name'] = i_item.xpath(".//h3/a[not(contains(@title,'控制器'))and(not(contains(@title,'龙业')))]/@title").extract_first()
			zol_item['name'] = i_item.xpath(".//h3/a/@title").extract_first()
			#detail = find_element_by_xpath(".//h3/a/span[contains(text(),'电机']")
			#zol_item['typeMedium'] = response.xpath("//div[@class='wrapper clearfix']/div[@class='side']/dl/dd/ul/li[@class='active']/a/text()").extract_first()
			zol_item['typeMedium'] = '停车管理'
			zol_item['typeBig'] = '楼宇/办公自动化B/OAS'
			zol_item['typeSmall'] = '智能停车系统'
			#zol_item['typeSmall'] =i_item.xpath(".//h3/a/span/text()").extract_first()
			if zol_item['name'] != None:
			#if detail != None:
				yield zol_item

		#该中类、品牌下翻页
		next_link = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='page-box']/div[1]/a[@class='next']/@href").extract()
		if next_link:
			next_link = next_link[0]
			yield scrapy.Request("http://detail.zol.com.cn"+next_link,callback=self.parse)

		#对于不同品牌选择
		next_link_brand = response.xpath("//div[@id='J_ParamBrand']/a[@class='active']/following-sibling::a/@href").extract()
		if next_link_brand:
			next_link_brand = next_link_brand[0]
			yield scrapy.Request("http://detail.zol.com.cn"+next_link_brand,callback=self.parse)


	