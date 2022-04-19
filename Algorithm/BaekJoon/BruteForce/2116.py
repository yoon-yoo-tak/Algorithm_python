"""
2116 주사위 쌓기

"""

import sys

input = sys.stdin.readline
n = int(input())
stack = [list(map(int, input().split())) for _ in range(n)]

def check(stack , ds):
  for i in range(0,6):
    if ds == stack[i]:
      idx = i
      break
  #1 6 / 2 4 / 3 5
  if idx == 0:
    return (max(stack[1],stack[2],stack[3],stack[4]) , stack[5])
  elif idx == 5:
    return (max(stack[1],stack[2],stack[3],stack[4]) , stack[0])
  elif idx == 1:
    return (max(stack[0],stack[2],stack[5],stack[4]) , stack[3])
  elif idx == 3:
    return (max(stack[0],stack[2],stack[5],stack[4]) , stack[1])
  elif idx == 2:
    return (max(stack[0],stack[1],stack[5],stack[3]), stack[4])
  elif idx == 4:
    return (max(stack[0],stack[1],stack[5],stack[3]), stack[2])

maxx = 0
for i in range(1,7):
  next_ds = i
  ans = 0
  for t in range(0,n):
    summ , next_ds = check(stack[t],next_ds)
    ans += summ
  if maxx < ans:
    maxx = ans
print(maxx)