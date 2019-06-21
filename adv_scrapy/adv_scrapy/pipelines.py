# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AdvScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class AdvScrapyPipeline1(object):
    def process_item(self, item, spider):
        return item

import mysql.connector

    class PhonesPipeline(object):
        def __init__(self):
            self.create_connection()
            self.create_table()