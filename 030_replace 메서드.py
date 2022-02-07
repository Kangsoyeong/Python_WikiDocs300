#아래 코드의 실행 결과를 예상해보세요.
#>> string = 'abcd'
#>> string.replace('b', 'B')
#>> print(string)

정답 : abcd가 그대로 출력된다.

#문자열은 변경할 수 없는 자료형이기 때문이다.
#replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
#먄약 str = string.replace('b', 'B')와 같이 코드를 작성했다면 aBcd가 출력될 것이다.