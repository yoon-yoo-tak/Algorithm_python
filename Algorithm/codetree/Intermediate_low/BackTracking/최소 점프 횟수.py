"""
최소 점프 횟수
"""
import sys

input = sys.stdin.readline

n = int(input())  # 길이 값 n
ls = list(map(int, input().split())) #거리 정보 저장

ans = int(1e9) # 정답 변수

def find_min(idx, cnt):  # idx 위치까지 cnt 만에 갈 수 있다?
    global ans

    if idx >= n - 1:  # 만약에 마지막 위치까지 도달했다면
        ans = min(ans, cnt)   # 현재 정답 변수와 cnt 와 비교
        return
    for dist in range(1, ls[idx] + 1):
        find_min(idx + dist, cnt + 1)

find_min(0, 0)

print(ans if ans != int(1e9) else -1)
