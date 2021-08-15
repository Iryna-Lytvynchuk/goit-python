import scrapy
from test_spyder.items import QuotesToscrapeItem

class QuotesSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    base_url = 'http://quotes.toscrape.com/'

    def parse(self, response):
        node_list = response.xpath('//div[@class="quote"]')
        for node in node_list:
            quote = node.xpath('.//span[@class="text"]/text()').extract()[0][1:-1]
            author = node.xpath('.//small/text()').extract()[0]
            tags = node_list.xpath('.//div[@class="tags"]//a/text()').extract()[0]
            url = self.base_url + node.xpath('.//small/following-sibling::a/@href').extract()[0]
            yield scrapy.Request(url=url, meta={'quote': quote, 'author': author, 'tags': tags,'url':url},
                                 callback=self.parse_author, dont_filter=True)

        next_url = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').extract()[0]
        if next_url is not None:
            yield scrapy.Request(url=self.base_url + next_url, callback=self.parse)
        
    def parse_author(self,response):
        item = QuotesToscrapeItem()
        item['quote'] = response.meta['quote']
        item['author'] = response.meta['author']
        item['tags'] = response.meta['tags']
        item['url'] = response.meta['url']
        item['born_date'] = response.xpath('//span[@class="author-born-date"]/text()').extract()[0]
        item['born_location'] = response.xpath('//span[@class="author-born-location"]/text()').extract()[0][3:]
        item['description'] = response.xpath('//div[@class="author-description"]/text()').extract()[0].strip()
        yield item

