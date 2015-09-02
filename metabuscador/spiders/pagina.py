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
    #    'http://www.dmoz.org/Computers/Programming/Languages/Python/',
    #    'http://www.colombia.com/gastronomia/',
    #    'http://hjkftzjfbdfg.heimat.eu/recet1.htm',  #-----------------------------> no toma nada
    #    'http://canalcocina.es/recetas/buscar/cocina/Cocina%20latinoamericana', #----------> algunos valores no salen desc en ninguno
        'http://allrecipes.com.ar/recetas/latinoamericana-recetas.aspx', #------>  igual que arriba
    ]

    def parse(self, response):

        #sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        #items = []
       for sel in response.xpath('//ul/li'):
            item = MetabuscadorItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item