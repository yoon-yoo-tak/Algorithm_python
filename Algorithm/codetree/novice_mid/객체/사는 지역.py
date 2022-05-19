import sys

input = sys.stdin.readline

class Info:
    def __init__(self, name = "", code = "", region = ""):
        self.name = name
        self.code = code
        self.region = region


info = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    info.append(Info(a, b, c))

min_idx = 0

for i, person in enumerate(info):
    if person.name > info[min_idx].name:
        min_idx = i

print(f'name {info[min_idx].name}')
print(f'addr {info[min_idx].code}')
print(f'city {info[min_idx].region}')

