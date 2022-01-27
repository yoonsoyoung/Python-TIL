# 상수 선언 및 값 할당
# 파이썬에서는 다른 언어에서 const 상수 문법이 없음. 변경이 가능함
PI = 3.14
a = 100
str = "Hello world!"

print(PI)
print(a)
print(PI, a, str)

# 다중 할당 -> tuple type
a = b = c = d = e =100, 200
print(type(a))
print(a, b, c, d, e)

# 다중 할당 시 여러 개 값을 여러 개 변수에 각각 저장하는 코드를 한 줄로 구현
a,b,c,d = 100, 3.14, 'k', 'korea'
print(a,b,c,d)

# 문자열, 따옴표, 홑따옴표
print('나는 엄마에게 말했다. "더 이상 카레는 먹기 싫어요!" 라고')
print('나는 엄마에게 말했다. "더 이상 \'카레\'는 먹기 싫어요!" 라고')

# id() 함수는 무엇을 출력하는가? -> 변수나 객체가 참조하는 고유 메모리 주소를 알 수 있음
a = '붕어빵'
print(a, id(a))

b = a
print(b, id(b)) # a라는 값을 그대로 b에 넣어줬기 때문에 주소값도 동일

a = '잉어빵'
print(a, id(a)) # 새로운 값을 할당했기 때문에 주소값이 바뀜
print(b, id(b)) # 여전히 붕어빵을 가리키고 있기 때문에 그대로


# is 연산자 = 주소값 비교(값 비교가 아님!)
a = [ 1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]
print('a is b = ', a is b)
print('a is c = ', a is c)
print('b is c = ', b is c)