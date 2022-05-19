import sys

input = sys.stdin.readline

class Info:
    def __init__(self, name = "", h = 0, w = 0):
        self.name = name
        self.h = h
        self.w = w


ls = [list(input().split()) for _ in range(5)]
student = sorted([Info(name, h, w) for name, h, w in ls], key=lambda x:(x.name))
student1 = sorted([Info(name, int(h), w) for name, h, w in ls], key=lambda x: -x.h)

print('name')
for i in student:
    print(i.name, i.h, i.w)
print()
print('height')
for i in student1:
    print(i.name, i.h, i.w)