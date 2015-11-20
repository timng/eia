# -*- coding: utf-8 -*-

# Scrapy settings for okfn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'okfn'

SPIDER_MODULES = ['okfn.spiders']
NEWSPIDER_MODULE = 'okfn.spiders'

ITEM_PIPELINES = {
    'okfn.pipelines.okfnPipeline': 1,
}

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 300,
# }
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'okfn (+http://www.yourdomain.com)'


# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
#     # Fix path to this module
#     'okfn.randomproxy.RandomProxy': 100,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
# }


# DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 600}
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = 'fc8d2065ba974b249d4b9a85dfc5eb76'
# CRAWLERA_PASS = ''

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = 'okfn/proxy_list.txt'