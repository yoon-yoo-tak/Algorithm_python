"""
1244 스우치 켜고 끄기
"""
import sys
input = sys.stdin.readline

n = int(input())
switch = [0] + list(map(int, input().split()))
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(1, n + 1):
            if i % b == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
    elif a == 2:
        temp = [b]
        val = min(b - 1, n - b)
        for i in range(1, val + 1):
            if switch[b - i] == switch[b + i]:
                temp.append(b - i)
                temp.append(b + i)
            else:
                break
        for i in temp:
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1

for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()
