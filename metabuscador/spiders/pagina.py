from symbol import yield_expr
from pip._vendor.html5lib.constants import headingElements
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils import response
from metabuscador.items import MetabuscadorItem
from scrapy.selector import Selector
from scrapy.spiders import Spider


class PaginaSpider(CrawlSpider):
    name = "pagina"
    #allowed_domains = ["pagina.com"]
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/',
    ]

    def parse(self, response):

        #sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        #items = []
         for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
             url = response.urljoin(href.extract())
             yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = MetabuscadorItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
                #re('-\s[^\n]*\\r')
            #print link,title,desc
            #items.append(item)
            yield item
        #return items
            next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url,callback=self.parse_dir_contents)


#        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
#            url = response.urljoin(href.extract())
#            yield scrapy.Request(url, callback=self.parse_dir_contents)

#    def parse_dir_contents(self, response):
#        for sel in response.xpath('//ul/li'):
#            item = MetabuscadorItem()
#            item['link'] = sel.xpath('a/@href').extract()
#            yield item