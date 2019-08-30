# News Crawler

뉴스기사 크롤러

1. SBS
2. KBS
3. MBC
3. JTBC

## SBS

(SBS 뉴스)[https://news.sbs.co.kr/news/search/main.do]

* 헤더

```
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
```

`user-agent`가 비어있으면 http response code 404 반환

* URL 구조분석

https://news.sbs.co.kr/news/search/main.do?pageIdx=1&searchTermStartDate=&searchTermEndDate=&searchSection=01%7C02%7C03%7C07%7C08%7C14%7C09&searchCategory=&searchMode=&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&collection=nnews&searchOption=1

```
pageIdx: 페이지 인덱스(1apge: 1, 2page: 2)
query: 검색어
collection: nnews
sort: 정렬기준 (최신순: DATE, 인기순: POP, 인기도순: RANK)
searchTermStartDate: yyyy.mm.dd
searchTermEndDate: yyyy.mm.dd
searchOption: 1~4(전체 검색: 1, 일주일 검색: 2, 한달 검색: 3, 날짜 검색: 4)
searchSection: 검색범위(정치 01, 경제: 02, 사회03, 국제: 07, 생활문화: 08, 연예: 14, 스포츠: 09) 해당 데이터를 비우면 전체검색
```

searchSection의 경우 검색범위를 하나만 넣을경우 `01`의 형태로 전달. 

다수의 범위를 선택하면 `01|02|14`의 형태로 전달

`01|02|14`는 정치, 경제, 연애 선택


## KBS

(KBS 뉴스)[http://news.kbs.co.kr/search/search.do]

* URL 구조분석

https://reco.kbs.co.kr/v2/search?target=newstotal&keyword=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&prev=&page=1&page_size=10&sort_option=date&searchfield=all&sdate=1987.01.01&edate=2019.08.27&categoryfield=&callback=search&_=1566887156844

별개의 URL을 통해 json 형태로 데이터를 응답

순수한 JSON 형태가 아니기 떄문에 필요없는 데이터를 지운 후 json 처리

```
target
keyword: 검색단어
prev
page: 페이지 인덱스
page_size: 페이지당 표시갯수
sort_option: 정렬기중 (최신순: data, 정확도순: score)
searchfield: 검색영역 (전체: all, 제목 + 내용: tcontent, 제목: title, 내용: content, 기자명: writer)
sdate: 시작날짜   (yyyy.mm.dd)
edate: 마지막 날짜 (yyyy.mm.dd)
categoryfield: 검색범위 (정치: 0003, 경제: 0004, 사회: 0005, IT/과학: 0007, 문화: 0008, 스포츠: 0002, 연예: 0039, 국제: 0006) 해당 데이터를 비우면 전체검색
_
```

searchSection의 경우 검색범위를 하나만 넣을경우 `0003`의 형태로 전달. 

다수의 범위를 선택하면 `0031,0004,0005`의 형태로 전달

`0031,0004,0005`는 정치, 경제, 사회 선택

* 응답결과 분석

```json
{
    "status": 200,
    "reason": "OK",
    "data": [
        {
            "contents_id": 2013058,
            "title": "현대중공업 서해 조선기지 시대 열었다",
            "contents": "",
            "parsed_title": "현대중공업 서해 조선기지 시대 열었다",
            "parsed_contents": "",
            "image_w": null,
            "image_h": "",
            "image_s": "",
            "image_o": "",
            "target_url": "http://news.kbs.co.kr/news/view.do?ncd=2013058",
            "source_code": "300",
            "section_code_name": "뉴스",
            "section_code": "01",
            "root_contents_code": "0004",
            "root_contents_code_name": "경제",
            "service_time": "20091218 135822",
            "vod_yn": "N",
            "broad_yn": "N",
            "rdatetime": "20171129",
            "source": "news",
            "score": "180"
        }
    ],
    "total_count": 388
}
```

응답결과는 json 형태로 받음

## MBC 

(MBC 뉴스)[http://search.imnews.imbc.com:8180/news/search.jsp]


* URL 구조분석

http://search.imnews.imbc.com:8180/news/search.jsp?kwd=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&date=all&category=TOTAL&subCategory=ALL&pageNum=2&sort=d&detailSearch=false

```
cate_top: 분류별 (정치: politics, 국제: world, 사회: society, 경제/과학: economy, 문화/연예: culture, 스포츠: sport)
newsprog_top: 프로그램별 (뉴스: newsproc, 다시보기: program, 위클리: weekly, 엠빅뉴스: mspecial, 더보기: etc)
startDate: yyyymmdd
endDate: yyyymmdd
kwd: 검색어
sort: 정렬 (최신순: d, 정확도순: r)
detailSearch: true
category: TOTAL
subCategory: ALL
pageNum: 1
date: detail
period: 7
```


## JTBC

(JTBC 뉴스)[http://jtbc.joins.com/search/news]

* URL 구조분석

http://jtbc.joins.com/search/news?source=any&term=%EC%95%BC%EA%B5%AC

```
field: 검색영역 (전체: any, 제목: title, 내용: contents, 기자명: reporter, 키워드: keyword)
section: 검색분야 (전체: any, 정치: politics, 경제: economy, 사회: social, 국제: international, 문화: culture, 연예: enter, 스포츠: sport, 날씨: weather)
source: 검색범위 (전체: any, JTBC 뉴스만: jtbc, JTBC 제외한 뉴스만: other)
sort: 정렬기준 (최신순: latest, 정확도순: accuracy)
```