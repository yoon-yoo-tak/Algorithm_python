"""
위에서 아래로

"""
import sys
input = sys.stdin.readline
n = int(input())
print(*sorted(list(int(input()) for _ in range(n)), reverse=True))



