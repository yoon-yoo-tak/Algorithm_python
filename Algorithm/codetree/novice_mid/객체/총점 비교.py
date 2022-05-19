import sys

input = sys.stdin.readline

class Info:
    def __init__(self, name = "", a = 0, b = 0, c = 0):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

n = int(input())
ls = [list(input().split()) for _ in range(n)]
for i in sorted([Info(name, int(a), int(b), int(c)) for name, a, b, c in ls], key = lambda x: (x.a + x.b + x.c)):
    print(i.name, i.a,i.b,i.c)
