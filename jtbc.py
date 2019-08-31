import requests as rq
from bs4 import BeautifulSoup
import pprint

class JTBC:

  def __init__(self, keyword):
    self.BASE_URL = 'http://jtbc.joins.com/search/news?'
    self.QUERY_URL = 'page=%d&term=%s&filed=%s&section=%s&source=%s&sort=%s'
    self.page = 1
    self.term = keyword
    self.filed = 'any'
    self.section = 'any'
    self.source = 'any'
    self.sort = 'latest'

  def __call__(self, **kwargs):
    self.page = self.__is_key(kwargs, 'page') and kwargs['page'] or self.page
    URL = self.BASE_URL + self.QUERY_URL % (self.page, self.term, self.filed, self.section, self.source, self.sort)

    res = rq.get(URL)
    soup = BeautifulSoup(res.content, 'lxml')

    contents = soup.select('.news_list li')

    temp = []

    for content in contents:
      temp.append(self.__format(content))

    self.page += 1

    return temp

  def __format(self, content):
    title = content.select('h3.prg_ttl')[0].text.replace('\n', '')
    link = content.select('h3.prg_ttl a')[0].get('href')
    img = content.select('.img img')
    img = len(img) and img[0].get('src') or ''
    text = content.select('.vod_exp')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
    who = content.select('.origin')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
    date = content.select('.date')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()

    return {
      "link": link,
      "title": title,
      "img": img,
      "text": text,
      "info": who + date,
    }

  def init(self, keyword):
    self.page = 1
    self.term = keyword

  def __is_key(self, dictionary, key):
    return key in dictionary.keys()

  def get_info(self):
    return {
        "page": self.page,
        "keyword": self.term
    }


if __name__ == "__main__":
  crawler_jtbc = JTBC("야구")
  data = crawler_jtbc(page = 3)
  pprint.pprint(data)

  pprint.pprint(crawler_jtbc.get_info())