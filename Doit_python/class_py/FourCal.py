class FourCal:
    # 생성자 함수
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):
    # 메서드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# 클래스 변수
class Family:
    lastName = "김"



