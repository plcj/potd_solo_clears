import scrapy

from support import build_urls


class PotdSoloLeaderboardSpider(scrapy.Spider):
    name = "leaderboard"
    allowed_domains = ['na.finalfantasyxiv.com']
    start_urls = build_urls()

    ## Testing
    # start_urls = ["https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b&solo_party=solo&dcgroup=Aether"]
    # start_urls = ["https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=1c29ab32bcd60f4ac37827066709fa17c872edca&solo_party=solo&dcgroup=Primal"]
    # start_urls = [
    #     "https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b&solo_party=solo&dcgroup=Aether",
    #     "https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=1c29ab32bcd60f4ac37827066709fa17c872edca&solo_party=solo&dcgroup=Primal"
    # ]

    def parse(self, response, **kwargs):
        yield {
            "url": response.url,
            "floorsReached": response.css('.deepdungeon__ranking__data--reaching::text').getall()
        }

        ## Testing
        # print("Clears (for testing): " + str(job_uid_xref[extract_job_uid_from_url(response.url)].value.clears)) # prints for each URL
