from packages.news.jtbc import JTBC
from packages.news.kbs import KBS
from packages.news.mbc import MBC
from packages.news.sbs import SBS

from packages.ml.word import word_extraction

from models.save import save_file

import pprint
import random

class Crawler():

  def __init__(self):
    self.keyword = "미국"
    self.crawlers = {
      "jtbc": JTBC(self.keyword),
      "kbs": KBS(self.keyword),
      "mbc": MBC(self.keyword),
      "sbs": SBS(self.keyword)
    }

    self.data_head = ['link', 'title', 'img', 'info', 'text']
    self.target = ''
    self.contents = []

    self.words = []

  def __call__(self):
    self.target = self.__random_select(self.crawlers.keys())
    self.show_info()
    self.contents = self.crawlers[self.target]()
    is_change = self.is_percentage_set_keyword()

    if is_change and len(self.contents):
      self.change_keyword()

  def change_keyword(self):
    content = self.__random_select(self.contents)
    new_keyswords = word_extraction(content['text'])
    new_keywords = list(set(new_keyswords.get('NNP', [])))
    
    if len(new_keywords):
      new_keyword = self.__random_select(new_keywords)
      self.crawlers[self.target].init(new_keyword)

  def __random_select(self, data):
    return random.choice(list(data))

  def is_percentage_set_keyword(self):
    return random.randint(1, 100) < 30

  def get_info(self):
    return {
      'contents': self.contents,
      'data_head': self.data_head,
      'target': self.target,
      'page': self.crawlers[self.target].page - 1,
      'keyword': self.crawlers[self.target].keyword
    }

  def get_info_by_target(self, news):
    return self.crawlers[self.target].get_info()

  def show_info(self):
    print('page: %s, new: %s, keyword: %s'%(self.crawlers[self.target].page, self.target, self.crawlers[self.target].keyword))

if __name__ == "__main__":
  c1 = Crawler()
  while True:
    c1()
    info = c1.get_info()
    # print(len(info['contents']), info['target'], info['keyword'], info['data_head'])
    save_file(info['target'], info['data_head'], info['contents'])