#print() 함수를 사용하여 다음과 같이 출력하세요.
#naver;kakao;sk;samsung

print("naver", "kakao", "sk", "samsung", sep=";")
#print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력된다.
#아래의 코드도 동일한 결과가 나온다. 그러나 sep을 이용하면 좀 더 깔끔해보이고, 문자열 사이에 어떤 문자가 들어가있는지 알아보기 쉽다.
#print("naver;kakao;sk;samsung")