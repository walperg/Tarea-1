# -*- coding: utf-8 -*-
import scrapy


class Tarea1Spider(scrapy.Spider):
    name = 'tarea1'
    allowed_domains = ['http://example.webscraping.com/']
    start_urls = ['http://http://example.webscraping.com//']

    def parse(self, response):
        pass
