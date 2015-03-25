__author__ = 'wrp'

import urllib.request
import re

from dbManager import dbManager


class Crawl:
    def __init__(self):
        pass

    dbm = dbManager.getInstance()

    @staticmethod
    def parse_url(content):
        ss = content.replace("[\S\s]+", "")
        urls = re.findall(r"<a(\s+)href=\"(.*?)\"(.*?)>", ss, re.I)

        for ur in urls:
            Crawl.dbm.execute('replace into url_uncrawl VALUES (%s)', ur[1])

    @staticmethod
    def fetch(url):
        response = urllib.request.urlopen(url)
        context = response.read().decode('utf-8')
        response.close()

        sql = "insert into page_content(url, content) VALUES (%s, %s)"

        Crawl.parse_url(context)

        Crawl.dbm.execute(sql, (url, context))

        # for i in Crawl.dbm.execute('select * from page_content'):
        #     print(i[1])



if __name__ == '__main__':
    Crawl.fetch('http://www.douban.com')
