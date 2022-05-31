"""
테스트 케이스 t가 주어진다.
각 테케마다 배열의 길이 n이 주어진다
배열 a가 주어진다.
0 <= i , j < n 을 만족하는 i, j에 대해
연산 (i, j)는 ai 를 aj 로 나눈 나머지이다.
서로다른 (i, j) 순서쌍을 골랐을 때 모든 (i, j)의 합은?
(변수 int 범위 였던걸로 기억)
[1, 2,3 ,4]
"""
for tt in range(1, int(input()) + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
           ans += ls[i] % ls[j]
    print(f'#{tt} {ans}')