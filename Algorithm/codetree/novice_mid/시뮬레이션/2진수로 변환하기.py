import sys

input = sys.stdin.readline

print(int('0b' + input().strip(), 2))



binary = list(map(int, list(input())))
length = len(binary)

# 십진수로 변환합니다.
num = 0
for i in range(length):
    num = num * 2 + binary[i]

# 출력
print(num)