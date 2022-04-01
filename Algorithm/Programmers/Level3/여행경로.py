"""
여행경로
"""
from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for i in tickets:
        graph[i[0]] = i[1]
    for key in graph.keys():
        graph[key].sort(reverse=True)
    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not graph[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(graph[tmp].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))

