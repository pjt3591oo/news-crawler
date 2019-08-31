import requests as rq
from bs4 import BeautifulSoup
import pprint

class MBC:

  def __init__(self, keyword):
    self.BASE_URL = "http://search.imnews.imbc.com:8180/news/search.jsp?"
    self.QUERY_URL = "kwd=%s&date=all&category=TOTAL&subCategory=ALL&pageNum=%d&sort=d&detailSearch=false"
    self.page = 1
    self.kwd = keyword

  def __call__(self, **kwargs):
    self.page = self.__is_key(kwargs, 'page') and kwargs['page'] or self.page
    URL = self.BASE_URL + self.QUERY_URL%(self.kwd, self.page)

    res = rq.get(URL)

    soup = BeautifulSoup(res.content, 'lxml')
    contents = soup.select('.searchresult_list li')

    temp = []

    for content in contents:
      temp.append(self.__format(content))

    self.page += 1
  
    return temp

  def __format(self, content):
    link = content.select('a')[0].get('href')
    title = content.select('.title')[0].text
    img = content.select('img.thum_img')
    img =  len(img) and img[0].get('src') or ''
    text = content.select('.description')[0].text
    info = content.select('.date')[0].text.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    return {
      "link"  : link,
      "title" : title,
      "img"   : img,
      "text"  : text,
      "info"  : info,
    }

  def init(self, keyword):
    self.page = 1
    self.kwd = keyword

  def get_info(self):
    return {
      "page": self.page,
      "keyword": self.kwd
    }

  def __is_key(self, dictionary, key):
    return key in dictionary.keys()

if __name__ == "__main__": 
  crawler_mbc = MBC("야구")
  data = crawler_mbc(page = 3)
  pprint.pprint(data)

  pprint.pprint(crawler_mbc.get_info())