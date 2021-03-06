#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:04:33 2018

@author: whitehat
"""

import scrapy

from scrapy.selector import Selector

class Detik(scrapy.Spider):

    name = 'Detik'
    # allowed_domains = ['www.news.detik.com'] #jika allowed_domains diaktifkan maka akan kena offsite di sub link
    start_urls = ['https://news.detik.com/jawatimur']

    # start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        rows = response.xpath('//div[@class="m_content"]/ul/li[not(@class)]').extract()
        for isi in rows:
            link_page = Selector(text=isi).xpath('//div[@class="desc_nhl"]/a/@href').extract_first()
            clean_date = Selector(text=isi).xpath('//div[@class="desc_nhl"]/span[@class="labdate f11"]/text()').extract_first()
            clean_date = clean_date.replace("DETIKNEWS | ", "")
            item = {
                'headline' : Selector(text=isi).xpath('//article/div[@class="desc_nhl"]/a[@data-category="WP Kanal Jawatimur"]/h2/text()').extract_first(),
                'main_headline' : Selector(text=isi).xpath('//div[@class="desc_nhl"]/text()[4]').extract_first().strip(),
                'date' : clean_date,
                'url' : link_page
            }

            request = scrapy.Request(link_page, callback=self.parse_page2)
            request.meta['item'] = item
            yield request

        # ------------Percobaan---------------
        # for title in response.css('h2.entry-title'):

        #     alamat = title.css('a ::attr(href)').extract_first()

        #     item =  {
        #         'title': title.css('a ::text').extract_first(),
        #         'link': alamat
        #         }

        #     request = scrapy.Request(alamat, callback=self.parse_page2)
        #     request.meta['item'] = item
        #     yield request 
        # ----------------------------------


        # untuk load next page old
        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page, self.parse)

    def parse_page2(self, response):

        # ------------Percobaan---------------
        # item = response.meta['item']
        # item['content'] = response.xpath('//div[@class="entry-content"]/text()').extract()
        # yield item
        # ----------------------------------

        item = response.meta['item']
        filter_text = response.xpath('normalize-space(//article/div/div[@class="detail_text"])').extract_first() 

        clean_table = response.xpath('//table//td//text()').extract()
        if clean_table:
            for remove_text in clean_table:
                filter_text = filter_text.replace(remove_text, "")

        clean_pic_top = response.xpath('//div[@class="pic_artikel pic_artikel_por"]/span/text()').extract()
        if clean_pic_top:
            for remove_pic in clean_pic_top:
                filter_text = filter_text.replace(remove_pic, "")

        item['content'] = filter_text
        yield item