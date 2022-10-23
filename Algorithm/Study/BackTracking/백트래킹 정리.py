"""
중복순열
문제를 n자리 m진수
 == 길이가 m인 배열에서 중복을 허용해서 n개의 값을 모두 골라보는 경우를 탐색 = > m개중에 n개 뽑기

코드는 크게 3가지 템플릿이 있다. 응용해서 알아서 쓰자.

"""
# 3자리 7진수
for i in range(7):
    for j in range(7):
        for k in range(7):
            print(i, j, k)
#
# 3자리 m진수
m = int(input())
for i in range(m):
    for j in range(m):
        for k in range(m):
            print(i, j, k)

# n자리 m진수 (중복순열) > n중 반복문을 구현해야하기 위해 재귀함수를 쓴다.
n, m = map(int, input().split())
selected = []

def rec(cur):  # 중복순열
    if cur == n:  # n개 뽑았다 !
        print(*selected)
        return
    for i in range(m):
        selected.append(i)
        rec(cur + 1)
        selected.pop()
rec(0)

"""
순열

n자리 m진수 중 한 케이스 내에 같은 수가 없는 것들만 출력
 == 길이가 m인 배열에서 중복을 허용하지 않고 
"""

selected = []
visited = [False] * m
print('#######################################')

def rec2(cur):  # 순열
    if cur == n:
        print(*selected)
    for i in range(m):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            rec2(cur + 1)
            visited[i] = False
            selected.pop()
rec2(0)

"""
n자리 m진수 중 중복케이스 제외하고 출력(조합)

"""
selected = []
def rec3(cur, start):
    if cur == n:
        print(*selected)
        return
    for i in range(start, m):
        selected.append(i)
        rec3(cur + 1, i + 1)
        selected.pop()

rec3(0)

