#url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#>> url = "http://sharebook.kr"
#실행 예:
#kr

url = "http://sharebook.kr"
print(url[-2:])

#아래의 세 줄 짜리 코드는 모범 답안이다.
#문자열로 표현된 url에서 split 메서드를 통해 .을 기준으로 url을 분리한다.
#분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있다.
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])