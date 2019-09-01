FROM rackspacedot/python37:latest


RUN apt-get update
RUN apt-get install -y git

RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y openjdk-8-jre

RUN cd /
WORKDIR /

RUN git clone https://github.com/pjt3591oo/news-crawler.git

RUN cd news-crawler
WORKDIR /news-crawler

RUN pip install -r requirements.txt
CMD ["python", "crawler.py"]