# News Crawler

뉴스기사 크롤러

1. SBS
2. KBS
3. MBC

## SBS

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
searchSection: 검색범위(정치 01, 경제: 02, 사회03, 국제: 07, 생활문화: 08, 연예: 14, 스포츠: 09) 해당 데이터를 비우면 통합검색
```

searchSection의 경우 검색범위를 하나만 넣을경우 `01`의 형태로 전달. 

다수의 범위를 선택하면 `01|02|14`의 형태로 전달

`01|02|14`는 정치, 경제, 연애 선택
