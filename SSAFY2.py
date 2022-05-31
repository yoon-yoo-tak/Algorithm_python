"""
테케 t 가 주어진다
배열의 크기 n이 주어진다
배열 a가 주어진다.

조건 : 배열의 모든 원소에 대해 홀수는 홀수끼리 인접하면 안되며, 짝수는 짝수끼리 인접하면 안된다.

배열의 원소에 대해 인접한 원소끼리 교환이 가능하다.

배열의 모든 원소가 조건에 만족하게 되는 최소 교환 횟수는?

(어떻게 교환해도 조건에 만족하지 않으면 -1 출력)

배열 크기 범위(200까지)
배열 원소 범위(80 까지 였나..아무튼 int범위)
"""


def possible(arr):  # 교환을 통해 정렬이 가능한지 판단
    if len(arr) % 2 == 0:  # 길이가 짝수일 때
        if arr.count(1) != arr.count(0):  # 0과 1의 갯수가 같아야 의미가 있다.
            return False
    else:
        if abs(arr.count(1) - arr.count(0)) != 1:  # 길이가 홀수일땐 0과 1의 갯수 차이가 1일때만 의미가 있다.
            return False
    return True


def check(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False
    return True


def my_sort(arr):  # 인덱스 차이가 최단일것이다 라는 추측
    global ans
    if len(arr) % 2 == 0:
        if arr[0] == 1:
            temp = [i for i in range(len(arr)) if arr[i] == 1]
            idx = [i for i in range(len(arr)) if i % 2 == 0]
            for i in range(len(temp)):
                ans += abs(temp[i] - idx[i])
        else:
            temp = [i for i in range(len(arr)) if arr[i] == 0]
            idx = [i for i in range(len(arr)) if i % 2 == 0]
            for i in range(len(temp)):
                ans += abs(temp[i] - idx[i])
    elif len(arr) % 2 != 0:
        if arr.count(1) < arr.count(0):
            temp = [i for i in range(len(arr)) if arr[i] == 0]
            idx = [i for i in range(len(arr)) if i % 2 == 0]
            for i in range(len(temp)):
                ans += abs(temp[i] - idx[i])
        else:
            temp = [i for i in range(len(arr)) if arr[i] == 1]
            idx = [i for i in range(len(arr)) if i % 2 == 0]
            for i in range(len(temp)):
                ans += abs(temp[i] - idx[i])


for tt in range(1, int(input()) + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    ls1 = [i % 2 for i in ls]
    ans = 0
    if possible(ls1):
        my_sort(ls1)
    else:
        ans = -1
    print(f'#{tt} {ans}')
