# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import sys
from items import NationalCouncilMeetingItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class MongoDBPipeline:

    collection = 'nationalCouncilMeetings'

    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
        #     mongodb_uri=crawler.settings.get('MONGODB_URI'),
        #     mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        # todo: remove credentials from here!!
            mongodb_uri='mongodb://austrian-parliamentary-data-scraping-prod:wyhFcbvlCwveGi9KvxynEwCbLeg6pXzZEonFOUq6ljEu7UHx6R3ayA9IjDpYEP8trnIMRNTvAwuoACDb1DxoyA==@austrian-parliamentary-data-scraping-prod.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@austrian-parliamentary-data-scraping-prod@',
            mongodb_db='austrianParliamentaryDataScraping',
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # Start with a clean database
        self.db[self.collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(NationalCouncilMeetingItem(item))
        self.db[self.collection].insert_one(data)
        return item