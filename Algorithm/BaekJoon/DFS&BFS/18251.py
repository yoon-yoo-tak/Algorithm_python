"""
18251 내 생각에 A번인 단순 dfs 문제가 이 대회에서 E번이 되어버린 건에 관하여 (Easy)
높이 = logN
"""
import sys, math

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
nums = []
height = int(math.log2(n)) + 1

def dfs(h, x, y):
    if h * 2 <= n:
        x = dfs(h * 2, x, y + 1)
    nums.append([x, y, ls[h - 1]])  # 중위순회로 x, y, 값 넣어줌
    if h * 2 + 1 <= n:
        x = dfs(h * 2 + 1, x + 1, y + 1)
    return x + 1

dfs(1, 0, 0)
ans = nums[0][2]  # 가장 아래 가장 왼쪽 노드
# print(nums)
for i in range(height):
    for j in range(i, height):
        temp = 0
        for k in nums:
            if i < k[1] < j:  # y값 체크
                if temp + k[2] >= 0:  # 양수 일때
                    temp += k[2]
                    ans = max(ans, temp)
                else:  # 음수 일때
                    ans = max(ans, k[2])
                    temp = 0
print(ans)