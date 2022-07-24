"""
14224 작은 정사각형 2
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]
l, r = 2, 2e9 + 2 # 경계에 걸치면 안되니까 + 2.

while l < r:  # 2 ~ 2e9 + 2 사이에서 적절한 변의 길이를 찾을거다.
    mid = (l + r) // 2  # 가운데 찍고
    flag = False
    for i in range(n):  # 임의의 점 두개를 고른다
        for j in range(n):
            x = min(dots[i][0], dots[j][0])  # 두개중에 x 좌표가 더 작은것 저장
            y = min(dots[i][1], dots[j][1])  # 두개중에 y 좌표가 더 작은것 저장
            cnt = 0  # 정사각형 안에 점이 몇개 있는지 세어줄 변수

            for k in range(n):  # 점들을 고르며 정사각형 안에 있는지 확인한다
                if dots[k][0] < x or x + mid - 2 < dots[k][0]:  # 지금 최소인 x보다 더 작다 >> 범위 밖 || 테두리에 혹은 밖에 있다.
                    continue  # 무시
                if dots[k][1] < y or y + mid - 2 < dots[k][1]:  # 지금 최소인 y보다 더 작다 >> 범위 밖 || 테두리에 혹은 밖에 있다.
                    continue  # 무시
                cnt += 1  # 임의의 두 점 사이에 있으며 테두리 안에 있으면 cnt += 1
            if cnt >= k:  # 그런 점이 k개 이상이면
                flag = True  # 멈쳐
                break
        if flag:  # 멈쳐
            break
    if flag:  # 범위를 더 줄여보면서 가장 작은 정사각형을 찾는다.
        r = mid
    else:
        l = mid + 1

print(int(l * l))
