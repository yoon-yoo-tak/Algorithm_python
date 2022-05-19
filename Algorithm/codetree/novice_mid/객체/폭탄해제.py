"""


"""

import sys

input = sys.stdin.readline

class Info:
    def __init__(self, code = "", color = "", sec = 0):
        self.code = code
        self.color = color
        self.sec = sec


a_code, a_color, a_sec = input().split()

bomb = Info()
bomb.code = a_code
bomb.color = a_color
bomb.sec = a_sec

print(f'code : {bomb.code}')
print(f'color : {bomb.color}')
print(f'second : {bomb.sec}')