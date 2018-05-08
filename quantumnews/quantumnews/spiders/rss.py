# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider

"""
Scrapes from RSS feeds with news regarding quantum computing

URL:
https://news.mit.edu/rss/topic/quantum-computing
"""


class MitRssSpider(XMLFeedSpider):
    name = 'rss'
    allowed_domains = [
        'https://news.mit.edu/rss/topic/quantum-computing',
    ]
    start_urls = [
        'https://news.mit.edu/rss/topic/quantum-computing',
    ]
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        self.logger.info('<{}> node: {}'.format(self.itertag, ''.join(selector.extract())))
        i = {}
        i['title'] = selector.select('title').extract()
        i['link'] = selector.select('link').extract()
        i['description'] = selector.select('description').extract()
        i['pubDate'] = selector.select('pubDate').extract()

        return i
