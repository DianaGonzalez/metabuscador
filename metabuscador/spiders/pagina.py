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

    # PAGUINAS INTERESANTES PERO SIN ALGUNO DE LOS ATRIBUTOS
    #    'http://allrecipes.com.ar/recetas/latinoamericana-recetas.aspx',
    #    'https://nypl.bibliocommons.com/list/show/87524369_nypl_mid_manhattan/123810792_muy_delicioso_la_cocina_latinoamericana',
    #    'http://www.mondolatino.eu/interesgeneral/cocina.php',

        'http://cocina.facilisimo.com/cocina-latinoamericana-recetas-con-maiz_1067896.html',
        'http://samanthacatering.com/blog/category/recetas/',


    ]

    def parse(self, response):

        #sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        #items = [] //meta[@name="description"/text()].extract()
       for sel in response.xpath('//ul/li'):  # estoy tomando esto mal
            item = MetabuscadorItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('//div[@class="post-text"]').extract()
            yield item



    def parse(self, response):

        #sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        #items = [] //meta[@name="description"/text()].extract()
       for sel in response.xpath('//ul/li'):  # estoy tomando esto mal
            item = MetabuscadorItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('//p').extract()
            yield item



    #def parse(self, response):

        #sel = Selector(response)
        #sites = sel.xpath('//ul[@class="directory-url"]/li')
        #items = [] //meta[@name="description"/text()].extract()
    #   for sel in response.xpath('//ul/li'):  # estoy tomando esto mal
    #        item = MetabuscadorItem()
    #        item['title'] = sel.xpath('a/text()').extract()
    #        item['link'] = sel.xpath('a/@href').extract()
    #        item['desc'] = sel.xpath('//p[@class="js-truncate"]').extract()
    #        yield item

