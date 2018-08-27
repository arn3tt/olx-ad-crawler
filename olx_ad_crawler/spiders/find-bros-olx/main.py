import scrapy
from scrapy.crawler import CrawlerProcess

class Ad:

    def __init__(self):
        self.mileage = None;
        self.title = None;
        self.price = None;
        self.posted = None;
        self.localization = None;

class Response:

    def __init__(self):
        self.has_next_page = False
        self.ads = []

def get_newest_registered_ad():
    # TODO
    return Ad()

def insert_ad(ad)
    pass

def crawl(url):
    # TODO
    return Response()

'''
Inserts the ads in the given URL that are newest than newest_known_ad
Returns True if the next page should be crawled
'''
def insert_new_ads(url, newest_known_ad):
    already_known = lambda ad : ad.posted <= newest_known_ad.posted
    response = crawl(url)
    new_ads = filter(already_known, response.ads)

    for ad in new_ads:
        insert_ad(ad)

    return len(new_ads) == len(response.ads) and response.has_next_page

def get_url_for_specific_page(url, page_number):
    if page_number < 2:
        return url
    else:
        if "?" in url:
            return url + ("&o=%d" % page_number)
        else:
            return url + ("?o=%d" % page_number)


BASE_URL = "https://pb.olx.com.br/autos-e-pecas/motos?ot=1&pe=9600&q=bros&rs=33"

newest_known_ad = get_newest_registered_ad()

current_page = 1
while True:
    url = get_url_for_specific_page(BASE_URL, current_page)
    if not insert_new_ads(url, newest_known_ad):
        break