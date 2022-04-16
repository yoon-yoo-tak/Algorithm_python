"""
2877 4와 7
"""
import sys
input = sys.stdin.readline
n = int(input())
print(format(n+1, 'b')[1:].replace('0', '4').replace('1', '7'))