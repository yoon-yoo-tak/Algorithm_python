"""

"""
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, s = map(int, input().split())
    ls = deque(list(map(int, input().split())))
    cnt = 0
    if sum(ls) < s:  # 총 합이 s 보다 작다 > 무슨 짓을 해도 못 만든다.
        print(-1)
        continue
    while sum(ls) != s:  # 총 합이 s가 될 때까지 반복
        front_one_idx = list(ls).index(1)  # 앞쪽 1 위치
        back_one_idx = list(ls)[::-1].index(1)  # 뒤쪽 1 위치
        if front_one_idx >= back_one_idx:  # 뒤에가 더 가깝거나 같으면
            for _ in range(back_one_idx + 1): # 1 위치 나올때 까지
                ls.pop()  # 뒤에서 빼겠다.
                cnt += 1  # 횟수 증가
        else:
            for _ in range(front_one_idx + 1):  # 앞에가 더 가까우면
                ls.popleft()  # 앞에서 빼겠다.
                cnt += 1  # 횟수 증가
    print(cnt)