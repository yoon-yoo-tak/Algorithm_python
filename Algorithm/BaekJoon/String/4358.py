"""
4358 생태학

"""

import sys

input = sys.stdin.readline
trees = {}

n = 0
while True:
    tree = input().strip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    n += 1
tree_lst = sorted(trees.keys())
for tree in tree_lst:
    print('%s %.4f' %(tree, trees[tree]/n * 100))