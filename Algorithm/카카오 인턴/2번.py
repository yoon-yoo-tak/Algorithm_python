from collections import deque

def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)
    result = 0
    total = sum(q1) + sum(q2)
    target = total // 2

    while True:
        if sum(q1) == sum(q2):
            break
        if sum(q1) < sum(q2):
            q1.append(q2.popleft())
            result += 1
        else:
            q2.append(q1.popleft())
            result += 1
    return result


print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1, 1], [1, 5]))