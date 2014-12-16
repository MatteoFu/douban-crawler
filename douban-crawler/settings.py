# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douban-crawler'

SPIDER_MODULES = ['douban-crawler.spiders']
NEWSPIDER_MODULE = 'douban-crawler.spiders'

ITEM_PIPELINES = ['douban-crawler.pipelines.MongoDBPipeline'，]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "douban-crawler"
MONGODB_COLLECTION = "doubangroups"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'
