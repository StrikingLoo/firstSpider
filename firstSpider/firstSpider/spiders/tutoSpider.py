import scrapy
class quotesSpider(scrapy.Spider):
	name = 'earthporn'
	start_urls = [
		'http://reddit.com/r/earthporn'
		]
	pageCount = 0 #pageCount
	def parse(self,response):
		final = ''
		for i in response.xpath('//a/@href'):
			if i.extract()[-4:]=='.jpg' or i.extract()[-4:]=='.png':
				final+='<img width=\'30%\' height=\'30%\' src=\''+ i.extract()+'\' > </img><br/> '
				print (i.extract()[2:]) 
		with open('.\links.html','a') as links:
			links.write(final)
		links.close()
		print('all is right')
		nextLink = response.css('span.next-button a::attr(href)')[0].extract()
		print(nextLink)
		self.pageCount += 1
		if self.pageCount<10: #this number can be changed to an arbitrary amount of pages.
			yield scrapy.Request(url = nextLink,callback = self.parse)
		
