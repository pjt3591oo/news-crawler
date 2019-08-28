import requests as rq
from bs4 import BeautifulSoup

BASE_URL = "http://search.imnews.imbc.com:8180/news/search.jsp?"
QUERY_URL = "kwd=%s&date=all&category=TOTAL&subCategory=ALL&pageNum=%d&sort=d&detailSearch=false"

PAGENUM = 1
KWD = "블록체인"

while True:
  URL = BASE_URL + QUERY_URL%(KWD, PAGENUM)

  res = rq.get(URL)

  soup = BeautifulSoup(res.content, 'lxml')
  contents = soup.select('.searchresult_list li')

  if not len(contents): break

  for content in contents:
    link = content.select('a')[0].get('href')
    title = content.select('.title')[0].text
    img = content.select('img.thum_img')
    img =  len(img) and img[0].get('src') or ''
    text = content.select('.description')[0].text
    info = content.select('.date')[0].text.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    print('link :', link)
    print('title :', title)
    print('img :', img)
    print('text :', text)
    print('info :', info)
    print('')

  print('====================== %d ======================'%(PAGENUM))
  PAGENUM += 1