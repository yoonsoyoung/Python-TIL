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