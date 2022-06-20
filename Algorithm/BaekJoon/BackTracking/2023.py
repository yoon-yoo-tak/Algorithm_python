"""
신기한 소수
"""
import sys, math

input = sys.stdin.readline


def is_prime(num):  # num이 소수이면 True 리턴 아니라면 False 리턴
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
selected = []
def rec(k):
    if len(str(k)) == n:
        print(k)
    else:
        for i in range(10):
            prime = k * 10 + i
            if is_prime(prime):
                rec(prime)
rec(2)
rec(3)
rec(5)
rec(7)
