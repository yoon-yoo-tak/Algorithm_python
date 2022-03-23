def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(i, res):
        if i == n:
            if res == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(i+1, res+numbers[i])
            dfs(i+1, res-numbers[i])
    dfs(0,0)
    return answer

print(solution([4,1,2,1], 4))