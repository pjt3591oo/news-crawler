import requests as rq
from bs4 import BeautifulSoup

import json
import math

BASE_URL = 'https://reco.kbs.co.kr/v2/search?'
QUERY_URL = 'target=%s&keyword=%s&prev=%s&page=%d&page_size=%d&sort_option=%s&searchfield=%s&sdate=%s&edate=%s&categoryfield=%s&_=%s'

TARGET="newstotal"
KEYWORD="블록체인"
PREV=''
PAGE=1
PAGE_SIZE=10
SORT_OPTION="date"
SEARCHFIELD="all"
SDATE="1987.01.01"
EDATE="2019.08.27"
CATEGORYFIELD=''
_=1566887156844

while True:
  URL = BASE_URL + QUERY_URL%(TARGET, KEYWORD, PREV, PAGE, PAGE_SIZE, SORT_OPTION, SEARCHFIELD, SDATE, EDATE, CATEGORYFIELD, _)

  res = rq.get(URL)
  items = res.json()

  total_count = items["total_count"]

  for item in items['data']:
    
    contents_id = item.get('contents_id')
    title = item.get('title')
    image_h = item.get('image_h')
    image_s = item.get('image_s')
    image_o = item.get('image_o')
    target_url = item.get('target_url')
    source_code = item.get('source_code')
    section_code_name = item.get('section_code_name')
    section_code = item.get('section_code')
    root_contents_code = item.get('root_contents_code')
    root_contents_code_name = item.get('root_contents_code_name')
    service_time = item.get('service_time')
    vod_yn = item.get('vod_yn')
    broad_yn = item.get('broad_yn')
    view_count = item.get('view_count')
    rdatetime = item.get('rdatetime')
    source = item.get('source')
    score = item.get('score')

    print('contents_id : ', contents_id)
    print('title : ', title)
    print('image_h : ', image_h)
    print('image_s : ', image_s)
    print('image_o : ', image_o)
    print('target_url : ', target_url)
    print('source_code : ', source_code)
    print('section_code_name : ', section_code_name)
    print('section_code : ', section_code)
    print('root_contents_code : ', root_contents_code)
    print('root_contents_code_name : ', root_contents_code_name)
    print('service_time : ', service_time)
    print('vod_yn : ', vod_yn)
    print('broad_yn : ', broad_yn)
    print('view_count : ', view_count)
    print('rdatetime : ', rdatetime)
    print('source : ', source)
    print('score : ', score)

  print('========================= %d / %d ========================='%(PAGE, math.ceil(total_count / 10)))
  
  if PAGE * PAGE_SIZE > total_count : break
  PAGE += 1

  print(total_count)