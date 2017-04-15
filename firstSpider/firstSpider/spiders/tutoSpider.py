import scrapy
import re
class quotesSpider(scrapy.Spider):
	name = 'earthporn'
	start_urls = [
		'http://reddit.com/r/earthporn'
		]
	count = 0
	def parse(self,response):
		'''page = response.url.split('/')[-2] #esto es por el formato de estos links
		filename = 'quotes-%s.html' % page
		with open(filename,'wb') as f: 
			f.write('asdasd')
		print ('done ' + filename)'''
		final = '<script>var a = 5;</script>'
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
		self.count += 1
		if self.count<10:
			yield scrapy.Request(url = nextLink,callback = self.parse)
		