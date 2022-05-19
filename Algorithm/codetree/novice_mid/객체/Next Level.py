
import sys

input = sys.stdin.readline

class Character:
    def __init__(self, id = "", level = 0):
        self.id = id
        self.level = level

user = Character()

user.id = 'codetree'
user.level = 10

user2_id, level2 = input().split()

user2 = Character()

user2.id = user2_id
user2.level = level2

print(f'user {user.id} lv {user.level}')
print(f'user {user2.id} lv {user2.level}')
