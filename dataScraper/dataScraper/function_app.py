from spiders.NationalCouncilMeeting_spider import NationalCouncilMeetingSpider
from pipelines import MongoDBPipeline

from pymongo import MongoClient

import scrapy
import azure.functions
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# https://victorsanner.nl/azure/scraping/container/instances/docker/2022/04/25/cheap-and-easy-scraping-using-scrapy-docker-and-azure-container-instances.html

settings = get_project_settings()

#this is where we start the scraper 
@app.function_name(name="HttpTrigger1")
def main():
    process = CrawlerProcess(settings)
    process.crawl(NationalCouncilMeetingSpider)
    process.start() # the script will block here until the crawling is finished
#test