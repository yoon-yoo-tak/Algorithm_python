#  네이버 공채 4번
import sys
input = sys.stdin.readline
n, Money = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
items.sort(key=lambda x: -x[2])  # 이율 순서로 내림차순 정렬
ans = 0
selected = []


def solve():
    global ans
    money = Money
    interest = 0
    for idx in selected:
        money -= items[idx][0]  # 최소치만큼 투자
        interest += items[idx][0] // 100 * items[idx][2]  # 최소치만큼 투자함으로서 얻는 수익 누적
    if money < 0:  # 돈이 부족하다. >> 이번 선택지는 불가능
        return

    for idx in selected:
        invest = min(money, items[idx][1] - items[idx][0])
        money -= invest
        interest += invest // 100 * items[idx][2]

    ans = max(ans, interest)


def backtracking(idx):
    if idx == n:
        solve()
        return
    selected.append(idx)
    backtracking(idx + 1)
    selected.pop()
    backtracking(idx + 1)

backtracking(0)
print(ans)
