"""
2688 숫자고르기
사이클찾기
"""
import sys
input = sys.stdin.readline


def dfs(a, b, c):
    a.add(c)
    b.add(ls[c])
    if ls[c] in a:
        if a == b:
            ans.update(a)
            return True
        return False
    return dfs(a, b, ls[c])


n = int(input())
ans = set()
ls = [0] + [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    if i not in ans:
        dfs(set(), set(), i)
print(len(ans))
for i in sorted(ans):
    print(i)