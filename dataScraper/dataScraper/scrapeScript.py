from spiders.NationalCouncilMeeting_spider import NationalCouncilMeetingSpider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# https://victorsanner.nl/azure/scraping/container/instances/docker/2022/04/25/cheap-and-easy-scraping-using-scrapy-docker-and-azure-container-instances.html

#this is where we start the scraper 
def scrape():
    process = CrawlerProcess(get_project_settings())
    process.crawl(NationalCouncilMeetingSpider)
    process.start() # the script will block here until the crawling is finished

scrape()