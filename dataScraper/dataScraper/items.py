# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dateutil.parser import parse
from itemloaders.processors import MapCompose, TakeFirst

def parseDate(dateString):
     dateTime = parse(dateString)
     return dateTime

def stripString(value):
     return value.strip()

class NationalCouncilMeetingItem(scrapy.Item):
     name = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst()) # 199. Sitzung
     date = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst()) # 20230201
     legislativePeriod  = scrapy.Field(output_processor = TakeFirst()) # XXVII
     meetingType = scrapy.Field(output_processor = TakeFirst()) # NRSTIZ or ...
     meetingNumber = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 00199
     meetingDay = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 1
     link = scrapy.Field(output_processor = TakeFirst())
 
     pass
