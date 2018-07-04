from scrapy.contrib.spiders import CrawlSpider, Rule
from wikispider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
    
                                    callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is: ' + title)
        item['title'] = title
        return item