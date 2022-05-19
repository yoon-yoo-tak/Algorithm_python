import sys

input = sys.stdin.readline

print(bin(int('0b' + input().strip(), 2) * 17)[2:])