"""
프로그래머스 레벨 2 구명보트
"""
def solution(people, limit):
    cnt = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        cnt += 1
        if people[end] + people[start] <= limit:
            start += 1
        end -= 1
    return cnt

print(solution([70, 50, 80, 50], 100))