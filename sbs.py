import requests as rq
from bs4 import BeautifulSoup
import pprint

class SBS:

  def __init__(self, keyword):
    self.BASE_URL = 'https://news.sbs.co.kr/news/search/main.do?'
    self.QUERY_URL = 'pageIdx=%d&searchTermStartDate=%s&searchTermEndDate=%s&query=%s&collection=%s&searchOption=%d&searchSection=%s'

    self.HEADERS = {
      # "Referer": "https://news.sbs.co.kr/news/search/main.do?pageIdx=1&searchTermStartDate=&searchTermEndDate=&searchSection=&searchCategory=&searchMode=&query=1&collection=&searchOption=1",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    } 

    self.page = 1
    self.query = keyword
    self.COLLECTION = 'nnews'
    self.SORT=  'date'
    self.SEARCHTERMSTARTDATE = ''
    self.SEARCHTERMENDDATE =  ''
    self.SEARCHOPTION = 1
    self.SEARCHSECTION=["01", "02", "03", "07", "08", "14", "09"]

  def __call__(self, **kwargs):
    self.page = self.__is_key(kwargs, 'page') and kwargs['page'] or self.page
    URL = self.BASE_URL + self.QUERY_URL%(self.page, self.SEARCHTERMSTARTDATE, self.SEARCHTERMENDDATE, self.query, self.COLLECTION, self.SEARCHOPTION, "|".join(self.SEARCHSECTION) )

    res = rq.get(URL, headers=self.HEADERS)

    soup = BeautifulSoup(res.content, 'lxml')
    contents = soup.select('.psearch_result_list li')

    temp = []

    for content in contents:
      temp.append(self.__format(content))

    self.page += 1

    return temp

  def __format(self, content):
    title = content.select('.psil_tit')[0].text.strip()
    img = content.select('.lazy')
    img = len(img) and img[0].get('data-src') or ''
    text = content.select('.psil_txt')[0].text.strip()
    info = content.select('.psil_info')[0].text.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    link = content.select('.psil_link')[0].get('href')

    return {
      "link"  : link,
      "title" : title,
      "img"   : img,
      "text"  : text,
      "info"  : info,
    }

  def init(self, keyword):
    self.page = 1
    self.query = keyword

  def get_info(self):
    return {
      "page": self.page,
      "keyword": self.query
    }

  def __is_key(self, dictionary, key):
    return key in dictionary.keys()


if __name__ == "__main__": 
  crawler_sbs = SBS("야구")
  data = crawler_sbs(page = 3)
  pprint.pprint(data)

  pprint.pprint(crawler_sbs.get_info())