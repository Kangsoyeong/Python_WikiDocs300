#다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
#ticker = "btc_krw"

ticker = "btc_krw"
print(ticker.upper())

#upper 메서드를 호출하면 문자열을 대문자로 만들 수 있다.
#다만 이 경우에도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환되는 것이다.
#반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로 출력하면 된다.
#따라서 아래의 코드도 동일한 결과를 출력한다.

ticker = "btc_krw"
UP = ticker.upper()
print(UP)