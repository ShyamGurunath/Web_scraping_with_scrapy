# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join

def remove(value):
    return value.replace(u"\u201d","").replace(u"\u201c","")

def remove_n(value):
    return value.replace("\n ","")

class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor=MapCompose(str.strip,remove),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(str.strip,remove_n),
        output_processor = TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(',')
    )