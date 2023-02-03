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

class NationalCouncilMeetingItem(scrapy.Item):
     name = scrapy.Field(output_processor = TakeFirst()) # 199. Sitzung
     date = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst()) # 01.02.2023
     legislativePeriod  = scrapy.Field(output_processor = TakeFirst()) # XXVII
     meetingType = scrapy.Field(output_processor = TakeFirst()) # NRSTIZ or ...
     dateOtherFormat = scrapy.Field(output_processor = TakeFirst()) # 20230201
     meetingNumber = scrapy.Field(output_processor = TakeFirst()) # 00199
     meetingDay = scrapy.Field(output_processor = TakeFirst()) # 1
     link = scrapy.Field(output_processor = TakeFirst())
 
     pass
