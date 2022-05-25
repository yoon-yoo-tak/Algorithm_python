"""
1225 [S/W 문제해결 기본] 7일차 - 암호생성기
"""
from collections import deque
while True:
    try:
        t = int(input())
        ls = deque()
        temp = list(map(int, input().split()))
        for i in temp:
            ls.append(i)
        while ls[-1] != 0:
            for i in range(1, 6):
                val = ls.popleft() - i
                if val <= 0:
                    val = 0
                    ls.append(val)
                    break
                ls.append(val)
        print(f'#{t}', end = ' ')
        print(*list(ls))
    except:
        break