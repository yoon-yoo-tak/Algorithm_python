"""

2805 나무 자르기

필요한 나무를 얻을 수 있는 최대 길이

Parametric Search로 접근

적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값 을 구하라

뒤집어서 생각 >> 어떤 높이(H)로 잘랐을 때 원하는 길이 M만큼 얻을 수 있는가?

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

def ok(H):
    sum = 0
    for x in a:
        if x > H:
            sum += x - H
    return sum >= m

l = 0
r = 2000000000
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)