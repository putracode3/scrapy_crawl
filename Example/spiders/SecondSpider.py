#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:04:33 2018

@author: whitehat
"""

import scrapy

from Example.items import NewItem

class SecondSpider(scrapy.Spider):
    name = 'SecondSpider'
    allowed_domains = ['www.superdatasciencecom']
    start_urls = ['https://www.superdatascience.com/artificial-intelligence']
    
    def parse(self, response):
        item = NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        
        return item
        