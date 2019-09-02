docker run --name news.logstash.com -i -t -d -p 5044:5044 news.logstash

echo "======== logstash 컨테이너 생성완료 ========\n"
echo "======== logstash 가동준비 40s 대기 ========\n"

second40() {
    local w=80 p=$1;  shift
    printf -v dots "%*s" "$(( $p*$w/40 ))" ""; dots=${dots// /.};
    printf "\r\e[K|%-*s| %3d(s) / 40(s) %s" "$w" "$dots" "$p" "$*"; 
}

# test loop
for x in {1..40} ; do
    second40 "$x" still working...
    sleep 1   # do some work here
done ; echo

docker run --name news.crawler.com -i -t -d --link news.logstash.com -v $PWD/logs/:/news-crawler/logs/ news.crawler