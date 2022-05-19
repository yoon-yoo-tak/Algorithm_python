"""
4466 최대 성적표 만들기
"""
for tt in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    ls = sorted(map(int, input().split()), reverse=True)
    ans = 0
    for i in range(k):
        ans += ls[i]
    print(f'#{tt} {ans}')

