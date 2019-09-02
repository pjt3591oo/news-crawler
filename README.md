# News Crawler

뉴스기사 크롤러

1. [사이트 분석](./docs/site_analysis.md)
2. [시스템 구조](./docs/system_architecture.md)
3. usage
4. pipeline 구축

## usage

```bash
$ git clone https://github.com/pjt3591oo/news-crawler.git
$ cd news-crawler
```

* 로컬 크롤러 실행

```bash
$ pip install -r requirements.txt
$ python crawler.py
```

logs 디렉터리로 수집 데이터 로그가 쌓임

* pipeline 전체실행

```bash
$ ./start.sh
```

## step by step

* crawler(filebeat), logstash 실행

```
$ ./createImg.sh
$ ./createContainer.sh
```

* elsasticsearch

```
$ docker-compose up
```

## pipeline 구축

* logstash 실행

```bash
$ logstash -r -f ./pipeline/logstash/pipeline.conf
```

* filebeat 실행

```bash
$ filebeat -e -c filebeat.yml -d "publish"
```

설정파일 위치 

MAC: **`/usr/local/etc/filebeat/`**

ubuntu: **`/etc/filebeat/`**