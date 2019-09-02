FROM rackspacedot/python37:latest


RUN apt-get update
RUN apt-get install -y git

RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y openjdk-8-jre

RUN cd /
WORKDIR /

RUN wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.4-amd64.deb
RUN dpkg -i filebeat-6.2.4-amd64.deb

COPY ./pipeline/filebeat/docker_filebeat.yml /etc/filebeat/filebeat.yml

RUN git clone https://github.com/pjt3591oo/news-crawler.git

RUN cd news-crawler
WORKDIR /news-crawler

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python crawler.py & filebeat -e -c filebeat.yml -d publish"]

# CMD ["sh", "-c", "filebeat -e -c filebeat.yml -d publish & python cralwer.py"]
# CMD ["python", "crawler.py"]