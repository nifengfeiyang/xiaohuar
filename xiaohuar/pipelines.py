# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib2


class XiaohuarPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        req = urllib2.Request(url=item['addr'],headers=headers)
        res = urllib2.urlopen(req)
        file_name = os.path.join(r'D:\my\down_pic',item['name']+'.jpg')
        with open(file_name,'wb') as fp:
            fp.write(res.read())
