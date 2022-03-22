"""

입국심사

모든사람이 심사를 받는데 걸리는 시간의 최솟값을 구하라

> 시간이 t일때 모든사람이 심사를 받을 수 있는가?

"""
def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n

    while l <= r:
        mid = (l + r) // 2
        ans = 0
        for t in times:
            ans += mid // t
            if ans >= n:
                break
        if ans >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer
