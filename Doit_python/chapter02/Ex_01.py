# multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)

print("=============================")

# 문자열 길이 구하기

a = "Life is too short"
b = len(a)
print(b)

print("=============================")

# 문자열 슬라이싱

str1 = "Life is too short, You need Python"
print(str1[0:4])  # 0<= str1 <4 --> 범위안에 있는 문자열을 출력

print("=============================")

# 딕셔너리

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

print("==============================")

print(list(a.keys()))

print("==============================")

print(a.values())

for b in a.values():
    print(b)

print("=============================")

print(a.items())

print(a.get('name'))

print("============================")

b = {'name': '홍길동', 'birth': 1128, 'age': 30}
print(b.items())

# 집합자료형 (중복을 허용하지 않는다, 순서가 없다.)

print("==============================")

# Q1
score = (80 + 75 + 55) / 3
print(score)
print("=============================")

# Q2
a = 13
if (a / 2 == 0):
    print("짝수입니다.")
print("홀수입니다.")
print("=============================")

# Q3
pin = "881120-1068234"
yyyymmdd = pin.split("-")[0]
num = pin[7:]
print(yyyymmdd)
print(num)
print("=============================")

# Q4
pin = "881120-1068234"
print(pin[7])  # 성별을 알수있는 번호 출력하기
print("================================")

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
print("===============================")

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)
print("================================")

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
print("=================================")

# Q8
a = (1, 2, 3)
a = a + (4,)
print(a)
print("===================================")

# Q9
# 답은 3번 타입xxx

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)
print("=================================")

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
print("====================================")

# Q12
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)
