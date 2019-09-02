second10() {
    local w=80 p=$1;  shift
    # create a string of spaces, then change them to dots
    printf -v dots "%*s" "$(( $p*$w/10 ))" ""; dots=${dots// /.};
    # print those dots on a fixed-width space plus the percentage etc. 
    printf "\r\e[K|%-*s| %3d(s) / 10(s) %s" "$w" "$dots" "$p" "$*"; 
}
second40() {
    local w=80 p=$1;  shift
    # create a string of spaces, then change them to dots
    printf -v dots "%*s" "$(( $p*$w/40 ))" ""; dots=${dots// /.};
    # print those dots on a fixed-width space plus the percentage etc. 
    printf "\r\e[K|%-*s| %3d(s) / 40(s) %s" "$w" "$dots" "$p" "$*"; 
}

echo
echo " ____    _____      _      ____    _____ "
echo "/ ___|  |_   _|    / \    |  _ \  |_   _|"
echo "\___ \    | |     / _ \   | |_) |   | |  "
echo " ___) |   | |    / ___ \  |  _ <    | |  "
echo "|____/    |_|   /_/   \_\ |_| \_\   |_|  "
echo

echo "logstash, crawler(filebeat) 이미지 생성시작"
docker build -t news.crawler -f ./Docker/Dockerfile .
docker build -t news.logstash -f ./Docker/Dockerfile_logstash .

echo "logstash, crawler(filebeat) 이미지 생성완료"

echo "elasticsearch, kibana 컨테이너 생성시작"
docker-compose up -d
echo "elasticsearch, kibana 컨테이너 생성완료"

echo "elasticsearch, kibana 컨테이너 가동준비 10s"

for x in {1..10} ; do
    second10 "$x" still working...
    sleep 1   # do some work here
done ; echo

echo "logstash 컨테이너 생성시작"

docker run --name news.logstash.com -i -t -d -p 5044:5044 news.logstash

echo "logstash 컨테이너 생성완료"
echo "logstash 가동준비 40s 대기"

for x in {1..40} ; do
    second40 "$x" still working...
    sleep 1   # do some work here
done ; echo

echo "crawler(filebeat) 컨테이너 생성시작"
docker run --name news.crawler.com -i -t -d --link news.logstash.com -v $PWD/logs/:/news-crawler/logs/ news.crawler
echo "crawler(filebeat) 컨테이너 생성완료"

echo "========= All GOOD, execution completed =========== "
echo

echo
echo " _____   _   _   ____   "
echo "| ____| | \ | | |  _ \  "
echo "|  _|   |  \| | | | | | "
echo "| |___  | |\  | | |_| | "
echo "|_____| |_| \_| |____/  "
echo

exit 0