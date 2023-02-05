import scrapy
import json
from pathlib import Path
from items import SpeechesMetaDataItem
from scrapy.loader import ItemLoader
from jmespath import search

class SpeechesMetaDataSpider(scrapy.Spider):
    name = "speechesMetaData"
    start_urls = ['https://www.parlament.gv.at/gegenstand/XXVII/NRSITZ/197?json=true']

    
    def parse(self, response):
        jsonAsPythonObject = json.loads(response.body)
        
        meetingDate = search('content[].info.sessiondate', jsonAsPythonObject)
        nationalCouncilMeetingTitle = search('content[].title', jsonAsPythonObject)
        print(nationalCouncilMeetingTitle)
        debates = search('content[].past_debates[]', jsonAsPythonObject)
        
        for singleDebate in debates:

            topic = search('text', singleDebate)

            speeches = search('speeches', singleDebate)
            for singleSpeech in speeches:
                isVoluntaryTimeLimit = singleSpeech[9] if singleSpeech[9] != None else 'unfreiwillig lol' # quick fix, there must be a better solution for null values
                l = ItemLoader(item=SpeechesMetaDataItem(), meetingDate = meetingDate, selector=singleSpeech)
                l.add_value('nameOfSpeaker', singleSpeech[2])
                l.add_value('nrOfSpeechInDebate', singleSpeech[0])
                l.add_value('nrOfSpeechByThisPerson', singleSpeech[4])
                l.add_value('typeOfSpeech', singleSpeech[5])
                l.add_value('startDateTime', singleSpeech[6])
                l.add_value('timeLimitInSec', singleSpeech[8])
                l.add_value('isVoluntaryTimeLimit', isVoluntaryTimeLimit)
                l.add_value('lengthOfSpeechInSec', singleSpeech[7])
                l.add_value('nationalCouncilMeetingTitle', nationalCouncilMeetingTitle)
                l.add_value('topic', topic)
                l.add_value('hasSpeechFinished', singleSpeech[1])
                yield l.load_item()
        

        #example json
        #  "speeches": [
        #                 [
        #                     1,
        #                     "fertig",
        #                     "Mag. Faika El-Nagashi (G)",
        #                     5651,
        #                     0,
        #                     "p",
        #                     "10:27",
        #                     "4:56",
        #                     4,
        #                     "*"
        #                 ],
        #                 [
        #                     2,
        #                     "fertig",
        #                     "Dietmar Keck (S)",
        #                     14840,
        #                     0,
        #                     "p",
        #                     "10:32",
        #                     "3:51",
        #                     3,
        #                     "*"
        #                 ]
        #               ]