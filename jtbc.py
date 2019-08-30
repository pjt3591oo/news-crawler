import requests as rq
from bs4 import BeautifulSoup

BASE_URL = 'http://jtbc.joins.com/search/news?'
QUERY_URL = 'page=%d&term=%s'

PAGE = 1
TERM = "야구"

while True:
  URL = BASE_URL + QUERY_URL%(PAGE, TERM)

  res = rq.get(URL)
  soup = BeautifulSoup(res.content, 'lxml')

  news = soup.select('.news_list li')

  for new in news:
    title = new.select('h3.prg_ttl')[0].text.replace('\n', '')
    link = new.select('h3.prg_ttl a')[0].get('href')
    img = new.select('.img img')
    img = len(img) and img[0].get('src') or ''
    text = new.select('.vod_exp')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
    who = new.select('.origin')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
    date = new.select('.date')[0].text.replace('\n', '').replace('\t', '').replace('\r', '').strip()

    print('title: ', title)
    print('link: ', link)
    print('img: ', img)
    print('text: ', text)
    print('who: ', who)
    print('date: ', date)

  print('============== %d page =============='%(PAGE))
  PAGE += 1