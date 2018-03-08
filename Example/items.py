# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#tambahan
from scrapy.item import Item, Field


#tambahan
class DetikItem(scrapy.Item):
    headline = Field()
    main_headline = Field()
    date = Field()

class NewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # Main Fields
    headline = Field()
    main_headline = Field()
    
    # Separate Fields
    # url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    date = Field()
    
    # Location Fields
    # location = Field()

class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    
    
#bawaan
class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


