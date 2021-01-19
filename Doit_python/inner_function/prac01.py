# Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)


# print(cal.value)

# Q2

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# Q4

list(filter(lambda a: a > 0, [1, -2, 3, -5, 8, -3]))

# Q5

int(0xea)

# Q6

show_list = list(map(lambda a: a * 3, [1, 2, 3, 4]))
# print(show_list)

# Q7

int_list = [-8, 2, 7, 5, -3, 5, 0, 1]
# a = max(int_list)
# b = min(int_list)
# print(a + b)

# Q8

round((17 / 3), ndigits=4)
# print(a)

# Q12

import time

time.strftime('%c', time.localtime(time.time()))

# Q13

import random

result = []

while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
