"""

7795 먹을 것인가 먹힐 것인가

B배열 정렬 > O(MlogM)
A의 원소마다 B배열에 대해 이분탐색 > O(NlogM)

O((N+M)logM)

"""
import sys
input = sys.stdin.readline

def lower_bound(A, L, R, X):
    result = L - 1
    while L <= R:
        mid = (L + R) // 2
        if A[mid] < X:
            result = mid
            L = mid + 1
        else:
            R = mid - 1
    return result

for i in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()))
    ans = 0
    for x in A:
        ans += lower_bound(B, 0, m - 1, x) + 1
    print(ans)
