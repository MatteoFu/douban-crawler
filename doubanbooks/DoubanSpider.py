from scrapy.selector import Selector
from scrapy.spider import Spider 
from douban.items import DoubanBookItem,DoubanSubjectItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lle

class DoubanSpider(CrawlSpider):
	name = "doubanbookcrawler"
	allowed_domains = ["douban.com"]
	start_urls = ["http://book.douban.com/tag/"]
	rules = [
	    Rule(lle(allow=("")),callback='parse_books'),
	    Rule(),
	    Rule()
]

	def parse_books(self,response):
		item = items()
		item['title'] = 
		item['tag'] = 
	return item
