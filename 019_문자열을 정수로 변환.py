#year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
#year = "2020"

year = "2020"
int1 = int(year)
print(int1-1, int1, int1+1) #2019 2020 2021

#아래의 세 줄도 동일한 결과를 출력한다.
print(int(year)-1) #2019
print(int(year)) #2020
print(int(year)+1) #2021