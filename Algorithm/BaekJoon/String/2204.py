"""

2204 도비의 난독증 테스트

"""
import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break

    words = []

    for i in range(n):
        words.append(input().strip())
    words.sort(key = lambda x: x.lower())
    print(words[0])



