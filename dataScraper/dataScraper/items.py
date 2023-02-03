# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NationalCouncilMeetingItem(scrapy.Item):
    name = scrapy.Field() # 199. Sitzung
    date = scrapy.Field() # 01.02.2023
    legislativePeriod  = scrapy.Field() # XXVII
    meetingType = scrapy.Field() # NRSTIZ or ...
    dateOtherFormat = scrapy.Field() # 20230201
    meetingNumber = scrapy.Field() # 00199
    meetingDay = scrapy.Field() # 1
    link = scrapy.Field()

    pass
