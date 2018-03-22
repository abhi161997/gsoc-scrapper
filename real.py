import requests
from bs4 import BeautifulSoup

link = "https://summerofcode.withgoogle.com/organizations/?sp-page=5"

r = requests.get(link)
soup = BeautifulSoup(r.content,"lxml")
print(soup)
sp = soup.findAll("div",{"class":"organization-card__container flex-xs-100 flex-sm-50 flex-33"})
print(len(sp))


class srapgsoc(scrapy.Spider):
    name = 'gsoc_spider'
    start_urls = ['https://summerofcode.withgoogle.com/organizations/?sp-page=5']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for org in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h2::text'
            DESCRIPTION_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            TECHNOLOGY_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            TOPIC_SELECTOR = 'h3 ::attr(src)'
            yield {
                'name': org.css(NAME_SELECTOR).extract_first(),
                'description': org.xpath(DESCRIPTION_SELECTOR).extract_first(),
                'technology': org.xpath(TECHNOLOGY_SELECTOR).extract_first(),
                'topic': org.css(TOPIC_SELECTOR).extract_first(),
            }

