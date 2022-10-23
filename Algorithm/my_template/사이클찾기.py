# 사이클 찾기
def dfs(k, a):
    visited[k] = a
    if visited[arr[k]] == a:
        is_cycle[k] = True
        return arr[k]
    elif visited[arr[k]] != -1:
        return -1

    x = dfs(arr[k], a)

    if x == -1:
        return -1

    is_cycle[k] = True
    if k == x:
        return -1
    return x


visited = [-1] * 100000
is_cycle = [False] * 100000
