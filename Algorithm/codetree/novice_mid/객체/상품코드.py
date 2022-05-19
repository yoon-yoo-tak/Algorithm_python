import sys

input = sys.stdin.readline

class Item:
    def __init__(self, name = "", code = 0):
        self.name = name
        self.code = code


a_name, a_code = input().split()

tree = Item()
tree.name = 'codetree'
tree.code = 50

new_item = Item()
new_item.name = a_name
new_item.code = a_code

print(f'product {tree.code} is {tree.name}')
print(f'product {new_item.code} is {new_item.name}')