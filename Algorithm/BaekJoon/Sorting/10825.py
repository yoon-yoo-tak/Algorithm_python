"""

10825 국영수

1. 국어점수가 감소하는 순서대로
2. 국어점수가 같으면 영어 점수가 증가하는 순서로
3. 국어, 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모두 같으면 이름이 증가하는 순서로.

"""
import sys
input = sys.stdin.readline

ls = []

for i in range(int(input())):
    a = input().split()
    a[1:] = map(int, a[1:])
    ls.append(a)

ls.sort(key = lambda x:(-x[1], x[2],-x[3], x[0]))

for i in ls:
    print(i[0])

