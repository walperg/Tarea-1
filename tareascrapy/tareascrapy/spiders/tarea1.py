# -*- coding: utf-8 -*-
import scrapy
from tareascrapy.items import clase_articles, clase_body

class Tarea1Spider(scrapy.Spider):
    name = 'tarea1'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    
    
    custom_settings={
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'file:C://Tarea 1//webspider.json'
    }

    def parse(self, response):
        host=self.allowed_domains[0]
        contador=0
        for link in response.css(".featured_article_metadata > a"):
            contador=contador+1
            title = link.attrib.get("title")
            link= f"https://{host}{link.attrib.get('href')}"
            
            if(contador>25):
                break    
            ##yield clase_articles(
              ##   title = link.attrib.get("title"),
                ## link= f"https://{host}{link.attrib.get('href')}"
                 ##                )
            yield response.follow(link,callback=self.parse_detail, meta={'link' : link,'title':title})
    def parse_detail(self,response):
        items = clase_articles()
        item = clase_body()

        items["link"] = response.css["link"]
        item["title"] = response.css["title"]
        item["paragraph"] = list()

        for text in response.css(".mw-content-text > p").extract():
            item["paragraph"].append(text)
        
        items["body"] = item
        return items

            

