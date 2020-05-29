import scrapy
import re


class ResidentialPeopleSpider(scrapy.Spider):

    def parse(self, response):
        # follow links to property pages
        for href in response.xpath('//*[@class="link link--minimal"]/@href').getall():
            yield response.follow(href, self.parse_property)

        # follow pagination links
        page_nums = response.xpath('//*[@class="listings-pagination-select"]/select/option/@value').re(r'\d+')
        page_nums[0] = ''

        sale_url = 'https://www.residentialpeople.com/za/property-for-sale/cape-town/?limit=10&offset={code}0&latitude=-33.9248685&longitude=18.4240553&radius=53.45541417432696&_location=Cape%20Town,%20South%20Africa&_radius_expansion=0.402'
        for code in page_nums[0:2]:
            yield scrapy.Request(sale_url.format(code=code))

        rent_url = 'https://www.residentialpeople.com/za/property-for-rent/cape-town/?limit=10&offset={code}0&latitude=-33.9248685&longitude=18.4240553&radius=53.45541417432696&_location=Cape%20Town,%20South%20Africa&_radius_expansion=0.402'
        for code in page_nums[0:2]:
            yield scrapy.Request(rent_url.format(code=code))


    def parse_property(self, response):
        title = response.css('h1::text').get()
        bedrooms = response.xpath('//*[@class="property-details-description-tag property-details__rooms"]/text()').getall()[0]
        bathrooms = response.xpath('//*[@class="property-details-description-tag property-details__rooms"]/text()').getall()[1]
        property_type = response.css('div.property-details-description__tags span::text').getall()[-1]

        floor_size = response.xpath('//*[@class="property-details-header-size"]/span[2]/text()').extract_first()
        if floor_size:
            # Floor size is dirty, we want only the number
            try:
                floor_size = float(''.join(re.findall(r'\d+', floor_size)))
            except ValueError:
                pass




        data = {
            'title': title,
            'offering': 'buy' if 'rent' not in response.css('h1::text').get() else 'rent',
            'price': ''.join(response.xpath('//*[@class="property-details-header-price"]/div/text()').re(r'\d+')),
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'latitude': response.css('script').re_first(r'"latitude":([\-\d.]+)'),
            'longitude': response.css('script').re_first(r'"longitude":([\-\d.]+)'),
            'floor_size': floor_size,
            'property_type': property_type,
            'url': response._get_url(),
            'images': response.xpath('//*[@class="image-gallery-slide"]/div/img/@src').extract()
        }

        for key, val in data.items():
            if val is not None and isinstance(val, str):
                data[key] = val.strip()

        return data
    