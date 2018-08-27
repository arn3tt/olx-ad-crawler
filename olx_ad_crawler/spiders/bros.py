# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['google.com']
    start_urls = ['http://www.google.com/']

    def get_title(ad_element):
    	return ad_element.css('.OLXad-list-title::text').extract()[0].strip()

    def get_mileage(ad_element):
    	return int(ad_element.css('.detail-specific::text').extract()[0].strip().split()[0].replace(".", ""))

    def get_price(ad_element):
    	return response.css('.section_OLXad-list').css('ul').css('li a')[0].css('.OLXad-list-price::text').extract()[0].strip().split()[1]

    def parse(self, response):
    	ad_elements = response.css('.section_OLXad-list').css('ul').css('li a')
    	for ad_element in ad_elements:
    		title = get_title(ad_element)
    		mileage = get_mileage(ad_element)
    		price = get_mileage(ad_element)

        pass
