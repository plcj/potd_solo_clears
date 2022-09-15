import datetime
import scrapy

import support
from data_model import jobs_by_uid


class PotdSoloLeaderboardSpider(scrapy.Spider):
    name = "leaderboard"
    allowed_domains = ['na.finalfantasyxiv.com']
    start_urls = support.build_urls()

    ## Testing
    # start_urls = ["https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b&solo_party=solo&dcgroup=Aether"]
    # start_urls = ["https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=1c29ab32bcd60f4ac37827066709fa17c872edca&solo_party=solo&dcgroup=Primal"]
    # start_urls = [
    #     "https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=eb7fb1a2664ede39d2d921e0171a20fa7e57eb2b&solo_party=solo&dcgroup=Aether",
    #     "https://na.finalfantasyxiv.com/lodestone/ranking/deepdungeon/?subtype=1c29ab32bcd60f4ac37827066709fa17c872edca&solo_party=solo&dcgroup=Primal"
    # ]

    @staticmethod
    def parse(response, **kwargs):
        leaders = response.css('.deepdungeon__ranking__list__item')
        job_name = jobs_by_uid[support.extract_job_uid_from_url(response.url)].name
        datacenter = support.extract_datacenter_from_url(response.url)
        for leader in leaders:
            yield {
                "job": job_name,
                "datacenter": datacenter,
                "url": response.url,
                "rank": leader.css('.deepdungeon__ranking__result__order::text').get(),
                "name": leader.css('.deepdungeon__ranking__result__name h3::text').get(),
                "world": leader.css('.deepdungeon__ranking__result__world::text').get(),
                "score": leader.css('.deepdungeon__ranking__data--score::text').get(),
                "floor": leader.css('.deepdungeon__ranking__data--reaching::text').get(),
                "utc-time": datetime.datetime.fromtimestamp(
                    support.extract_epoch_from_time_script(
                        leader.css('.deepdungeon__ranking__data--time script').get())),
            }
