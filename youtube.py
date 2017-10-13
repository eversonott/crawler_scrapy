import scrapy
from scrapy.contrib.loader import ItemLoader


class YoutubeVideo(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()


class YoutubeChannelLister(scrapy.Spider):
    name = 'youtube-channel-lister'
    youtube_channel = 'LongboardUK'
    start_urls = ['https://www.youtube.com/user/%s/videos' % youtube_channel]

    def parse(self, response):
        for sel in response.css("ul#channels-browse-content-grid > li"):
            loader = ItemLoader(YoutubeVideo(), selector=sel)

            loader.add_xpath('link', './/h3/a/@href')
            loader.add_xpath('title', './/h3/a/text()')
            loader.add_xpath('views', ".//ul/li[1]/text()")

            yield loader.load_item()