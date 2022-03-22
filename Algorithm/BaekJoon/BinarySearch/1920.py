"""

1920 수 찾기

A배열 안에 X라는 정수가 존재하는지 알아내기
존자하면 1, 아니면 0 출력

"""
import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def lower_bound(A, L, R, X):
    while L <= R:
        mid = (L + R) // 2
        if A[mid] < X:
            L = mid + 1
        else:
            R = mid -1
        if A[mid] == X:
            return True
    return False


for i in B:
    if lower_bound(A, 0, N-1, i): print(1)
    else: print(0)
