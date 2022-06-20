"""
2529 부등호
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(input().split())
visited = [False] * 10
selected = []
minimum = int(1e10)
maximum = int(-1e10)
ans_mini = ''
ans_maxi = ''
def rec(k):
    global minimum, maximum, ans_mini, ans_maxi
    if k == n + 1:
        if int(''.join(map(str, selected))) < minimum:
            ans_mini = (''.join(map(str, selected)))
            minimum = int(''.join(map(str, selected)))
        elif int(''.join(map(str, selected))) > maximum:
            ans_maxi = (''.join(map(str, selected)))
            maximum = int(''.join(map(str, selected)))
    else:
        for i in range(10):
            if k >= 1:
                if ls[k - 1] == '>':
                    if selected[k - 1] > i and not visited[i]:
                        selected.append(i)
                        visited[i] = True
                        rec(k + 1)
                        selected.pop()
                        visited[i] = False
                    else:
                        continue
                else:
                    if selected[k - 1] < i and not visited[i]:
                        selected.append(i)
                        visited[i] = True
                        rec(k + 1)
                        selected.pop()
                        visited[i] = False
                    else:
                        continue
            else:
                selected.append(i)
                visited[i] = True
                rec(k + 1)
                selected.pop()
                visited[i] = False

rec(0)
print(ans_maxi)
print(ans_mini)


