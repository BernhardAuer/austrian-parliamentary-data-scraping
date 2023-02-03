from pathlib import Path

import scrapy
import json
from dataScraper.items import NationalCouncilMeetingItem


class NationalCouncilMeetingSpider(scrapy.Spider):
    name = "nationalCouncilMeeting"
    search_url = 'https://www.parlament.gv.at/Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_007&listeId=11070&showAll=true&export=true'

    def start_requests(self):
            return [scrapy.FormRequest(self.search_url,
                                    formdata={},
                                    method="POST",
                                    callback=self.test)]

    def parse(self, response):
        yield scrapy.Request(self.search_url, callback=self.test, method="POST")

    
    def test(self, response):
        results = json.loads(response.body)
        item = NationalCouncilMeetingItem()

        for meeting in results['rows']:
            try:
                item['name'] = meeting[1]
                item['date'] = meeting[0]
            except:
                continue
            yield item