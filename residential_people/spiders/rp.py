# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import re
import scrapy

from ..base.base_residential_people import ResidentialPeopleSpider

class RpSpider(ResidentialPeopleSpider):
    name = 'rp'
    start_urls = [
    'https://www.residentialpeople.com/za/property-for-sale/cape-town/?limit=10&offset=0&latitude=-33.9248685&longitude=18.4240553&radius=53.45541417432696&_location=Cape%20Town,%20South%20Africa&_radius_expansion=0.402',
    'https://www.residentialpeople.com/za/property-for-rent/cape-town/?limit=10&offset=0&latitude=-33.9248685&longitude=18.4240553&radius=53.45541417432696&_location=Cape%20Town,%20South%20Africa&_radius_expansion=0.402'
    ]