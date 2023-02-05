# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dateutil.parser import parse
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime
from dataclasses import dataclass, field

def parseDate(dateString):
     dateTime = parse(dateString).replace(microsecond=0) # this replace shitty thing is needed for mongodb (js dates only, huh)
     return dateTime

def stripString(value):
     return value.strip()

class NationalCouncilMeetingItem(scrapy.Item):
     name = scrapy.Field(output_processor = TakeFirst()) # 199. Sitzung
     date = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst()) # 20230201
     legislativePeriod  = scrapy.Field(output_processor = TakeFirst()) # XXVII
     meetingType = scrapy.Field(output_processor = TakeFirst()) # NRSTIZ or ...
     meetingNumber = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 00199
     meetingDay = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 1
     link = scrapy.Field(output_processor = TakeFirst()) 
     pass


def parseHasSpeechedFinishProperty(value):
     if value == 'fertig':
          return True
     return False

def parseIsVoluntaryTimeLimitProperty(value):
     if value == '*':
          return True
     return False

def convertTimeStringToIntInSec(value):
     # value: (m)m:ss
     (minutes, seconds) = value.split(":")
     totalSeconds = int(seconds) + (int(minutes) * 60)
     return totalSeconds

def convertTimeLimitInMinToSec(value):
     # value: (m)m # tbh this should already be int, but to be sure cast it anyway
     totalSeconds = int(value) * 60
     return totalSeconds

def mergeMeetingDateWithSpeechTime(value, loader_context):
     # value: hh:mm (time in 24h format)
     meetingDate = loader_context.get('meetingDate')
     meetingDate = parse(meetingDate[0])
     (hour, minute) = value.split(":")
     speechDatetime = meetingDate.replace(hour=int(hour), minute=int(minute))
     return speechDatetime
     
class SpeechesMetaDataItem(scrapy.Item):
     nameOfSpeaker = scrapy.Field(output_processor = TakeFirst())
     nrOfSpeechInDebate = scrapy.Field(output_processor = TakeFirst())
     nrOfSpeechByThisPerson = scrapy.Field(output_processor = TakeFirst()) #personSpeechCountInDebate
     typeOfSpeech = scrapy.Field(output_processor = TakeFirst())
     startDateTime = scrapy.Field(input_processor= MapCompose(mergeMeetingDateWithSpeechTime),output_processor = TakeFirst())
     timeLimitInSec = scrapy.Field(input_processor= MapCompose(convertTimeLimitInMinToSec), output_processor = TakeFirst())
     isVoluntaryTimeLimit = scrapy.Field(input_processor= MapCompose(parseIsVoluntaryTimeLimitProperty), output_processor = TakeFirst())
     lengthOfSpeechInSec = scrapy.Field(input_processor= MapCompose(convertTimeStringToIntInSec), output_processor = TakeFirst())
     nationalCouncilMeetingTitle = scrapy.Field(output_processor = TakeFirst()) ## ?? really? better use int
     topic = scrapy.Field(output_processor = TakeFirst())
     hasSpeechFinished = scrapy.Field(input_processor= MapCompose(parseHasSpeechedFinishProperty), output_processor = TakeFirst())
     pass
