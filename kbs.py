import requests as rq
from bs4 import BeautifulSoup
import json
import math
import pprint

class KBS:

  def __init__(self, keyword):
    self.BASE_URL = 'https://reco.kbs.co.kr/v2/search?'
    self.QUERY_URL = 'target=%s&keyword=%s&prev=%s&page=%d&page_size=%d&sort_option=%s&searchfield=%s&sdate=%s&edate=%s&categoryfield=%s&_=%s'

    self.TARGET="newstotal"
    self.keyword=keyword
    self.PREV=''
    self.page=1
    self.PAGE_SIZE=10
    self.SORT_OPTION="date"
    self.SEARCHFIELD="all"
    self.SDATE=""
    self.EDATE=""
    self.CATEGORYFIELD=''
    self._=1566887156844

  def __call__(self, **kwargs):
    self.page = self.__is_key(kwargs, 'page') and kwargs['page'] or self.page
    URL = self.BASE_URL + self.QUERY_URL%(self.TARGET, self.keyword, self.PREV, self.page, self.PAGE_SIZE, self.SORT_OPTION, self.SEARCHFIELD, self.SDATE, self.EDATE, self.CATEGORYFIELD, self._)

    res = rq.get(URL)
    items = res.json()

    contents = items['data']
    temp = []

    for content in contents:
      temp.append(self.__format(content))
      
    self.page += 1

    return temp

  def __format(self, content):
    contents_id = content.get('contents_id')
    title = content.get('title')
    image_w = content.get('image_w')
    target_url = content.get('target_url')
    text = content.get('contents')
    date = content.get('service_time')
    pprint.pprint(content)
    
    return {
      "link": target_url,
      "img": image_w,
      "title": title,
      "text": text,
      "info": "[] "+ date
    }

  def init(self, keyword):
    self.page = 1
    self.keyword = keyword

  def get_info(self):
    return {
      "page": self.page,
      "keyword": self.keyword
    }

  def __is_key(self, dictionary, key):
    return key in dictionary.keys()

if __name__ == "__main__": 
  crawler_kbs = KBS("야구")
  data = crawler_kbs(page = 3)
  pprint.pprint(data)

  pprint.pprint(crawler_kbs.get_info())