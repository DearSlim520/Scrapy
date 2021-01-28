# -*- coding: utf-8 -*-
import scrapy
from zol_SPJK.items import ZolSpjkItem
import urllib.request
import lxml.html
'''
【仅供中关村在线网使用，使用规则：爬取二级类，手动修改start_urls即可（选中要爬取的二级类的第一个品牌）】
【typeSmall的地方视频监控和楼宇自动化都是第一句，服务器第二句】
【视频监控】
监控摄像机：http://detail.zol.com.cn/camera_equipment/quanruiweishi/
硬盘录像机：http://detail.zol.com.cn/image_record/honeywell/
视频服务器：http://detail.zol.com.cn/video_server/haikangweishi/
监控采集卡：http://detail.zol.com.cn/monitoring_card/haikangweishi/
光端机：http://detail.zol.com.cn/transmission_equipmenterandreceiver/zjhjtx/
监视器：http://detail.zol.com.cn/display_control/samsung/
画面分割器：http://detail.zol.com.cn/screen_splitter/robot/
视频分配器：http://detail.zol.com.cn/video_distributor/aten/
编解码器：http://detail.zol.com.cn/codec/haikangweishi/
中央控制系统：http://detail.zol.com.cn/centralcontrol_system/omron/
电视墙操作台：http://detail.zol.com.cn/tvwall_console/weiteng/
监控硬盘：http://detail.zol.com.cn/tvwall_console/weiteng/
监控周边：http://detail.zol.com.cn/peripherals/haikangweishi/
【楼宇自动化（考勤门禁）】
考勤机：http://detail.zol.com.cn/kaoqinmenjinshoufei/zksoftware/
门禁一体机：http://detail.zol.com.cn/access_onemachine/zksoftware/
消费机：http://detail.zol.com.cn/charging_machine/comet/
门禁控制器：http://detail.zol.com.cn/access_controller/wiegand/
门禁系统：http://detail.zol.com.cn/accesscontrol_system/see-world/
楼宇对讲：http://detail.zol.com.cn/building_intercom/meeyi/
巡更机：http://detail.zol.com.cn/patrol_system/landwell/
【服务器】
服务器：http://detail.zol.com.cn/server/dellemc/
【办公自动化系统】
打印机：http://detail.zol.com.cn/printer/hp/s18/
	   http://detail.zol.com.cn/printer/hp/s19/
	   http://detail.zol.com.cn/printer/hp/s20/
扫描仪：http://detail.zol.com.cn/scanner/eloam/
复印机：http://detail.zol.com.cn/copier/xerox/s3686/
	   http://detail.zol.com.cn/copier/xerox/s3688/
打印服务器：http://detail.zol.com.cn/print_server/hardlink/
'''
class SpjkSpiderSpider(scrapy.Spider):
	name = 'SPJK_spider'
	allowed_domains = ['detail.zol.com.cn']
	start_urls = ['http://detail.zol.com.cn/building_intercom/zhuiwzhuiw/']
	def parse(self, response):
		zol_list = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='list-box']/div")
		for i_item in zol_list:
			zol_item = ZolSpjkItem()
			#zol_item['brand'] = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='param-filter']/div[@class='filter_brand']/div[@class='brand-hot brand-list']/a[@class='active']/text()").extract_first()
			zol_item['brand'] = response.xpath("//div[@id='J_ParamBrand']/a[@class='active']/text()").extract_first()        	
			zol_item['name'] = i_item.xpath(".//div[@class='pro-intro']/h3/a/text()").extract_first()
			zol_item['typeMedium'] = '通讯设备'
			#zol_item['typeMedium'] = response.xpath("//div[@class='wrapper clearfix']/div[@class='side']/dl/dd/ul/li[@class='active']/a/text()").extract_first()
			zol_item['typeBig'] = '楼宇/办公自动化B/OAS'
			zol_item['typeSmall'] ='楼宇对讲系统'
			#zol_item['typeSmall'] = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='param-filter']/div[@class='filter-item']/div[@class='param-value-list']/a/text()").extract_first()   #未检验
			#zol_item['typeSmall'] = i_item.xpath(".//div[@class='pro-intro']/ul/li[1][contains(@title,'全向麦克风')]/@title").extract_first()      #搜索关键词（灰色描述）
			#zol_item['typeSmall'] = response.xpath("//div[@class = 'list-box']/div[contains(@class, 'list-item clearfix')]/div[@class='pro-intro']/ul/li/@title").extract_first()  #仅限服务器
			content = response.xpath("//div[@class='list-box']/div[2]/div[@class='pro-intro']/ul/li/@title").extract()
			
			if zol_item['name'] != None:
				#zol_item['typeSmall'] = '会议专用全向麦克风'
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
		

	