# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class DoubanBookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    num = Field()
    info = Field()

class DoubanSubjectItem(Item):
    title = Field()
    link = Field()
    info = Field()
    rate = Field()
    votes = Field()
    author_intro = Field()
    tags = Field()

