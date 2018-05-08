# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider

"""
Scrapes from RSS feeds with news regarding quantum computing

URL:
https://news.mit.edu/rss/topic/quantum-computing
"""


class RssSpider(XMLFeedSpider):
    name = 'rss'
    allowed_domains = [
        'https://news.mit.edu/rss/topic/quantum-computing',
        'https://phys.org/rss-feed/search/?search=quantum+computing'
    ]
    start_urls = [
        'https://news.mit.edu/rss/topic/quantum-computing',
        'https://phys.org/rss-feed/search/?search=quantum+computing'
    ]
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        self.logger.info('<{}> node: {}'.format(self.itertag, ''.join(selector.extract())))
        i = {}
        i['title'] = selector.xpath('//title/text()').extract()
        i['link'] = selector.xpath('//link/text()').extract()
        i['description'] = selector.xpath('//description/text()').extract()
        i['pubDate'] = selector.xpath('//pubDate/text()').extract()

        return i
