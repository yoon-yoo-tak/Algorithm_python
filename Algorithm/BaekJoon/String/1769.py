"""

1769 3의 배수

"""

import sys
input = sys.stdin.readline

n = input().strip()
cnt = 0
while True:
    sum = 0
    if len(n) == 1:
        break
    for i in n:
        sum += int(i)
    n = str(sum)
    cnt += 1

print(cnt)
print('YES' if int(n) % 3 == 0 else 'NO')
