"""
특정 조건에 맞게 k개 중에 1개를 n번 뽑기 연속 3개 안됨 2개까지만
"""
import sys

input = sys.stdin.readline

k, n = map(int, input().split())  # 뽑을 범위 k, 뽑을 갯수 n
selected = [0] * n  # 뽑힌 수를 담을 리스트


def rec(x):     # 1 ~ k 까지의 수 중에 n개를 뽑는데, 같은 수는 연속하여 2개까지 가능하도록 선택해주는 함수
    if x == n:  # n개 뽑았다!
        print(*selected)  # 출력
        return  # 종료
    else:
        for i in range(1, k + 1):  # 1 ~ k 사이에서 뽑을것이므로 1 ~ k 까지 반복
            if x >= 2 and selected[x - 1] == selected[x - 2] and selected[x - 1] == i:  # 만약에 3개이상 뽑았고,
                                                                                        # 현재 뽑으려는 수가 전에 뽑은것과 그 전에 뽑은것과 같으면.
                continue  # 무시하고 다음 숫자를 뽑는다.
            else:  # 그게 아니라면
                selected[x] = i  # x번째 뽑을 숫자를 i로 결정
                rec(x + 1)       # (x + 1) 번째 뽑으러 출발
                selected[x] = 0  #

rec(0)
