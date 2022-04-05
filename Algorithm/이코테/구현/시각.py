"""
이코테 구현파트 연습문제 - 시각

정수 N이 입력되면 00시00분00초부터 N시 59분 59초까지 모든 시각중에서 3이 포함되는 경우가 몇가지인지 구하기
1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

h = int(input())
count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
