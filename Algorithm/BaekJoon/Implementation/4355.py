"""
4355 숫자 맞추기
"""

import sys

input = sys.stdin.readline

mini = 0
maxi = 100
while True:
    num = int(input())
    if num == 0:
        break

    talk = input().rstrip()
    if talk == 'too high':
        maxi = min(num, maxi)

    elif talk == 'too low':
        mini = max(num, mini)

    else:

        if mini < num < maxi:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        mini = 0
        maxi = 100
