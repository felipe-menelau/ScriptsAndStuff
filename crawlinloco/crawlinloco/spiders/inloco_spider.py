import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest

class inlocoSpider (scrapy.Spider):
	
	name = "inloco"
	login_page = "https://accounts.inlocomedia.com/en/login"
	star_url = 	["https://accounts.inlocomedia.com/en/admin/statistics/publishers"]
	
	def init_request(self):
		self.log("isso funciona")
		return Request(url=self.login_page, callback=self.login)
	
	def login(self, response):
		return FormRequest.from_response(response,
						formdata={'email': 'felipe.menelau@inlocomedia.com', 'password': 'this_is_sparta_743'},
						callback=self.check_login_response)
	
	def check_login_response(self, response):
		if "Campanhas" in response.body:
			self.log("Login bem sucedido")
			self.initialized()
		else:
			self.log("Nope")
			
	