"""
2817 부분 수열의 합
"""
def solve(idx, sum):
    global cnt
    if idx >= n:
        return
    temp = sum + ls[idx]
    if temp == k:
        cnt += 1
    solve(idx + 1, sum)
    solve(idx + 1, temp)


for tt in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    cnt = 0
    solve(0, 0)
    print(f'#{tt} {cnt}')


