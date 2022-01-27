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


# [is] 연산자 = 주소값 비교(값 비교가 아님!)
a = [ 1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]
print('a is b = ', a is b) # True
print('a is c = ', a is c) # False
print('b is c = ', b is c) # False

# [==] 연산자 = 데이터 값 비교
a = [ 1, 2, 3, 4, 5]
b = a
c = [1, 2, 3, 4, 5]
print('a == b = ', a == b) # True
print('a == c = ', a == c) # True
print('b == c = ', b == c) # True

# is, == 연산자 문제 연습
a = 101
b = 100 + 1
print('a is b = ', a is b, ' > id(a) ', id(a), ' > id(b) ', id(b)) # T 101 이라는 공간이 이미 있기 때문에 같은 곳을 가리키게 됨
print('a == b = ', a == b) # T

c = 'korea'
d = 'korea'
print('c is d = ', c is d) # T
print('c == d = ', c == d) # T

e = [1,2,3,4,5]
f = [1,2,3,4,5]
print('e is f = ', e is f) # F 리스트는 각 객체가 만들어져 가리키게 됨
print('e == f = ', e == f) # T


# is 연산자  추가
print('-' * 10)
a = 'korea'
b = 'korea'
print('a is b = ', a is b)

b += '!' # b 끝에 ! 추가
print('b += ! = ', b, id(b)) # korea! 라는 새로운 메모리 공간
print('a is b = ', a is b) # False -> a = korea , b = korea! 이므로 서로 다른 메모리 공간

c = b[:-1] # b에서 끝에서 1자를 slice 잘라내기 => korea / !
print('c = b[:-1] ', c, id(c)) # korea
print('a is c = ', a is b) # False -> 다른 주소값인 b에서 잘라왔으므로 기존에 korea가 있음에도 새로 할당


# 문자열의 slice 결과와 id(), is() 연산자
print('-' * 10)
t = 'korea'
print(t, id(t), '-', t[:1], id(t[:1]), '-', t[:2], id(t[:2]), '-', t[:3], id(t[:3]),
      '-', t[:4], id(t[:4]), t[:5], id(t[:5]),  '-', t[:-1], id(t[:-1])) # t = t[:5]
# k[:4] = kore, k[:-1] = kore 지만 서로 다른 주소값
print(t, id(t[:])) # 전부를 슬라이스. 변화 없이 슬라이스 했으므로 별도 메모리 공간 할당하지 않음
print('t[:] is t[:5] ', t[:] is t[:5]) # True


# 두 변수 값 교환
print('-' * 10)
a = 100
b = 200
print('교환 전 a, b = ', a, b)

temp = a
a = b
b = temp
print('교환 후 a, b = ', a, b) # swqp 방식

c, d = 300, 400
print('교환 전 c, d = ', c, d)
c, d = d, c
print('교환 후 c, d = ', c, d) # 문법적인 특징을 사용한 교환
