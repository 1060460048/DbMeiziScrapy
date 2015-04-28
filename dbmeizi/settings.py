# -*- coding: utf-8 -*-

# Scrapy settings for stack project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dbmeizi'

SPIDER_MODULES = ['dbmeizi.spiders']
NEWSPIDER_MODULE = 'dbmeizi.spiders'

ITEM_PIPELINES = ['dbmeizi.pipelines.MongoDBPipeline',] 

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "dbmeizi"
MONGODB_COLLECTION = "meizi"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stack (+http://www.yourdomain.com)'
