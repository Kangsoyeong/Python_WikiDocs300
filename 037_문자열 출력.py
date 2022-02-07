#파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.

#35번 문제
"""변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
이름: 김민수 나이: 10
이름: 이철희 나이: 13"""

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#f-string은 문자열 앞에 f가 붙은 형태이다.
#f-string을 사용하면 {변수}와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력할 수 있다.