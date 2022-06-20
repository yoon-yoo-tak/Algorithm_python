"""
2n개 중에 n개의 숫자를 적절하게 고르기
2n 개 중에 n개를 뽑은 두 그룹 생성
각그룹의 총 합의 차이가 최소가 되도록
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))  # 길이 2n의 리스트
total = sum(ls)
ans = int(1e10)
selected = []
# 2n개 중에 n개 뽑기
def rec(k, cnt):
    global total, ans
    if k == 2 * n:
        if cnt == n:
            ans = min(ans, abs(total - (2 * sum(selected))))
    else:
        selected.append(ls[k])
        rec(k + 1, cnt + 1)
        selected.pop()
        rec(k + 1, cnt)
rec(0, 0)
print(ans)
