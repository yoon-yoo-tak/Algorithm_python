"""
22988 재활용 캠페인
"""
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
ls = sorted(map(int, input().split()))  # 정렬
ans = ls.count(x)  # 완품만큼 더하기
for i in range(ans):
    ls.pop()
l, r = 0, len(ls) - 1 # 시작, 끝
rest = len(ls) # 남은거

while l < r:
    if ls[l] + ls[r] >= x // 2:  # 두개의 합이 반보다 크다 == 가능
        rest -= 2  # 남은거에서 2개 빼줌
        l += 1  # 왼쪽 ++
        r -= 1  # 오른쪽 ++
        ans += 1 # 정답 ++
    else:
        l += 1  # 왼쪽 ++

ans += rest // 3
print(ans)


