# 함수

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result


# 매개변수에 초깃값 미리설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d입니다.." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# vartest_return.py
a = 1


def vartest(a):
    a = a + 1
    return a


a = vartest(a)

# lambda
add = lambda a, b: a + b
result = add(3, 4)
mul = lambda a, b: a * b
result1 = mul(3, 4)

# writedata.py
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다..\n" % i
    f.write(data)
f.close()

# readline.py
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# add_data.py

f = open("새파일.txt", 'a')
for i in range(11, 21):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
data_1 = f2.read()
print(data_1)
f2.close()

user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()

