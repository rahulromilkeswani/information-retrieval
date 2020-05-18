# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from bs4 import BeautifulSoup
import json

class UicSpideySpider(CrawlSpider):
    name = 'uic_spidey'
    allowed_domains = ['uic.edu']
    start_urls = ['https://cs.uic.edu/']
    #disallowed_domains = ['https://www.cs.uic.edu/bin/','login.uic.edu/','https://www2.cs.uic.edu/','https://acm.cs.uic.edu/wiki','http://lug.cs.uic.edu/wiki']
    counter = 1
    links_visited = []
    rules = [
        Rule(LinkExtractor(canonicalize=True, unique=True, allow = allowed_domains),
            follow=True,
            callback = 'parse_url',
        )
    ]
    custom_settings = {
        'DEPTH_LIMIT' : 4
    }

    def parse_url(self, response):
        self.links_visited.append(response.url)
        items = []
        soup = BeautifulSoup(response.text,'html.parser') 
        file_contents = {}
        file_contents["url"] = response.url
        file_contents["title"] = soup.title.string.strip()
        paragraphs = soup.findAll('p')
        text = []
        for paragraph in paragraphs[2:] : 
                for line in paragraph.getText().split("\n"):
                    text.append(line.strip())
        file_contents["text"] = text
        links = LinkExtractor(canonicalize=True, unique=True, allow_domains=("uic.edu")).extract_links(response)
        out_links = []
        for link in links : 
            if(not link.url == response.url) : 
                out_links.append(link.url)
        file_contents["out_links"] = out_links
        filename = "files\\"+str(self.counter) + ".json"
        f = open(filename, "w+")
        json.dump(file_contents,f, ensure_ascii=False, indent=4)
        f.close()
        self.counter += 1
        yield {"url" : response.url}
      