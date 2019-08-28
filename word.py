from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()


def parse(text):
  temp = {}
  for result in kkma.pos(text) :
    temp.setdefault(result[1], [])
    temp[result[1]].append(result[0])
  return temp


if __name__ == '__main__':
  texts = [
    '일본 정부는 오늘 새벽 0시를 기해 한국을 수출심사 우대국인 화이트리스트에서 제외하는 수출무역관리령 개정안을 시행했습니다. ',
    '한국 대법원의 강제징용 배상판결에 반발해 지난 7월 반도체 핵심소재 3개 품목에 대한 수출 규제를 강화한 이후 사실상 2차 보복 조치입니다. ' 
  ]
  
  for text in texts:
    words = parse(text)
    pprint(text)
    pprint(words)