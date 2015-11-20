# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class okfnPipeline(object):
    def process_item(self, item, spider):
        with open(spider.export_file, 'ab') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if spider.writer_header :
                spider.writer_header = False;
                csvwriter.writerow(spider.csv_header)
            csvwriter.writerow([ item[ x.replace('/', '').replace(' ', '')].encode('utf-8') for x in spider.csv_header])
        return item
