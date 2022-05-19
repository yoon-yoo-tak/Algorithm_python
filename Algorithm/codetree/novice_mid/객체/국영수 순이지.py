import sys

input = sys.stdin.readline

class Info:
    def __init__(self, name = "", kor = 0, eng = 0, math = 0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
ls = [list(input().split()) for _ in range(n)]
student = sorted([Info(name, int(kor), int(eng), int(math)) for name, kor, eng, math in ls], key=lambda x:(-x.kor, -x.eng, -x.math))
for i in student:
    print(i.name, i.kor, i.eng,i.math)