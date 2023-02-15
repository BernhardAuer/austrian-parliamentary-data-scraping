# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dateutil.parser import parse
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime
from dataclasses import dataclass, field
from validTitlesList import validTitles
from jmespath import search

def parseDate(dateString):
     dateTime = parse(dateString).replace(microsecond=0) # this replace shitty thing is needed for mongodb (js dates only, huh)
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

def getTitlesAndPureName(value):
     parsedTitles = []
     for title in validTitles: # list order is important, eg. because of Mag. and Mag. (FH)
          if title + ' ' in value or value.endswith(title): # whitespace or end of line...
               parsedTitles.append(title)
               value = value.replace(title, '')
     return (parsedTitles, value)

def getName(value):
     (parsedTitles, name) = getTitlesAndPureName(value)
     return name

def extractTitles(value):
     (parsedTitles, name) = getTitlesAndPureName(value)
     return parsedTitles

def matchAndParseDataFromProtocol(value, loader_context):
     speechesInProtocol = loader_context.get('speechesInProtocol')
     url = search('[*][?contains(texta, \''+ value +'\')]', speechesInProtocol)[0] # todo: use i 
     return url

def parseVideoUrl(value, loader_context):
     speechData = matchAndParseDataFromProtocol(value, loader_context)
     videoUrl = search('[*].video', speechData)
     return videoUrl 

def parseSpeechUrl(value, loader_context):
     speechData = matchAndParseDataFromProtocol(value, loader_context)
     url = search('[*].filename', speechData)
     return url 

def parseSpeechTimeFromProtocol(value, loader_context):
     speechData = matchAndParseDataFromProtocol(value, loader_context)
     time = search('[*].time', speechData)
     return time 

class SpeechesMetaDataItem(scrapy.Item):
     titleBeforeName = scrapy.Field(input_processor = MapCompose(extractTitles, stripString)) # todo: "parlaments"titel wie BM usw.
     nameOfSpeaker = scrapy.Field(input_processor = MapCompose(getName, stripString), output_processor = TakeFirst())
     titlePrecedingName = scrapy.Field(input_processor = MapCompose(extractTitles, stripString))
     politicalPartie = scrapy.Field(output_processor = TakeFirst())
     nrOfSpeechByThisPerson = scrapy.Field(output_processor = TakeFirst()) #personSpeechCountInDebate
     typeOfSpeech = scrapy.Field(output_processor = TakeFirst())
     startDateTime = scrapy.Field(input_processor= MapCompose(mergeMeetingDateWithSpeechTime),output_processor = TakeFirst())
     timeLimitInSec = scrapy.Field(input_processor= MapCompose(convertTimeLimitInMinToSec), output_processor = TakeFirst())
     isVoluntaryTimeLimit = scrapy.Field(input_processor= MapCompose(parseIsVoluntaryTimeLimitProperty), output_processor = TakeFirst())
     lengthOfSpeechInSec = scrapy.Field(input_processor= MapCompose(convertTimeStringToIntInSec), output_processor = TakeFirst())
     hasSpeechFinished = scrapy.Field(input_processor= MapCompose(parseHasSpeechedFinishProperty), output_processor = TakeFirst())
     nationalCouncilMeetingTitle = scrapy.Field(output_processor = TakeFirst()) ## ?? really? better use int
     topic = scrapy.Field(output_processor = TakeFirst())
     speechNrInDebate = scrapy.Field(output_processor = TakeFirst())
     externalPersonId = scrapy.Field(output_processor = TakeFirst())
     parsingDatetime = scrapy.Field(output_processor = TakeFirst())
     meetingNr = scrapy.Field(output_processor = TakeFirst())
     legislature = scrapy.Field(output_processor = TakeFirst())
     meetingType = scrapy.Field(output_processor = TakeFirst())
     lastEditBySource = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst())
     meetingDate = scrapy.Field(output_processor = TakeFirst())
     topNr = scrapy.Field(output_processor = TakeFirst())
     typeOfDebate = scrapy.Field(output_processor = TakeFirst())
     videoUrl = scrapy.Field(input_processor = MapCompose(getName, stripString, parseVideoUrl), output_processor = TakeFirst())
     speechUrl= scrapy.Field(input_processor = MapCompose(getName, stripString, parseSpeechUrl), output_processor = TakeFirst())
     speechTimeProtocol = scrapy.Field(input_processor = MapCompose(getName, stripString, parseSpeechTimeFromProtocol), output_processor = TakeFirst())
     pass
