# News Crawler

뉴스기사 크롤러

1. [사이트 분석](./docs/site_analysis.md)
2. [시스템 구조](./docs/system_architecture.md)

## usage

```bash
$ git clone https://github.com/pjt3591oo/news-crawler.git
$ cd news-crawler
```

* 로컬실행 

```bash
$ pip install -r requirements.txt
```

```bash
$ python crawler.py
```

* 도커실행

```bash
$ ./craeteImg.sh
```

```bash
$ ./createContainer.sh
```

logs 디렉터리로 수집 데이터 로그가 쌓임