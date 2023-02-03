import logging
import azure.functions as func

from spiders.NationalCouncilMeeting_spider import NationalCouncilMeetingSpider
from pipelines import MongoDBPipeline

from pymongo import MongoClient

import scrapy
import azure.functions
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
#from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

# https://victorsanner.nl/azure/scraping/container/instances/docker/2022/04/25/cheap-and-easy-scraping-using-scrapy-docker-and-azure-container-instances.html
# https://doc.scrapy.org/en/latest/topics/practices.html#run-from-script


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    # process = CrawlerProcess(settings)
    # process.crawl(NationalCouncilMeetingSpider)
    # process.start() # the script will block here until the crawling is finished

    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner(get_project_settings())

    d = runner.crawl(NationalCouncilMeetingSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished
    
    return func.HttpResponse(f"Hello. This HTTP function executed successfully.")

