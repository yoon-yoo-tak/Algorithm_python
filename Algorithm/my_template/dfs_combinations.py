"""
재귀(dfs)로 조합(combinations)구하기
"""
m = 1234 # m 개 뽑기
list_i_have_to_pick = []
selected = []
def dfs(depth, idx):
    if depth == m:
        print("m개뽑고 해야할 일들")
        return
    for i in range(idx, len(list_i_have_to_pick)):
        selected.append(list_i_have_to_pick[i])
        dfs(depth + 1, i + 1)
        selected.pop()

dfs(0, 0)