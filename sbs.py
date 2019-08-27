import requests as rq
from bs4 import BeautifulSoup

BASE_URL = 'https://news.sbs.co.kr/news/search/main.do?'
QUERY_URL = 'pageIdx=%d&searchTermStartDate=%s&searchTermEndDate=%s&query=%s&collection=%s&searchOption=%d&searchSection=%s'

headers = {
  # "Referer": "https://news.sbs.co.kr/news/search/main.do?pageIdx=1&searchTermStartDate=&searchTermEndDate=&searchSection=&searchCategory=&searchMode=&query=1&collection=&searchOption=1",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
} 

PAGEIDX = 1
QUERY = '블록체인'
COLLECTION = 'nnews'
SORT=  'date'
SEARCHTERMSTARTDATE = ''
SEARCHTERMENDDATE =  ''
SEARCHOPTION = 1
SEARCHSECTION=["01", "02", "03", "07", "08", "14", "09"]


while True:
  URL = BASE_URL + QUERY_URL%(PAGEIDX, SEARCHTERMSTARTDATE, SEARCHTERMENDDATE, QUERY, COLLECTION, SEARCHOPTION, "|".join(SEARCHSECTION) )

  res = rq.get(URL, headers=headers)

  soup = BeautifulSoup(res.content, 'lxml')
  contents = soup.select('.psearch_result_list li')

  for content in contents:
    title = content.select('.psil_tit')[0].text.strip()
    img = content.select('.lazy')
    img = len(img) and img[0].get('data-src') or ''
    text = content.select('.psil_txt')[0].text.strip()
    info = content.select('.psil_info')[0].text.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    link = content.select('.psil_link')[0].get('href')

    print('title  : ', title)
    print('img    : ', img)
    print('text   : ', text)
    print('info   : ', info)
    print('link   : ', link)

    print('===============')

  print(URL, PAGEIDX, len(contents))
  if not len(contents): break
  PAGEIDX += 1

print('end')