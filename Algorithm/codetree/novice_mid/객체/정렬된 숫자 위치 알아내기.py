import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls1 = [(ls[i], i + 1) for i in range(n)]
ls2 = sorted(ls1, key=lambda x:x[0])
ans = []
for i in ls1:
    ans.append(ls2.index(i) + 1)
print(*ans)

## 풀이 1

# 클래스 선언
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index


# 변수 선언 및 입력
n = int(input())
given_inputs = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(given_inputs)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key = lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')



## 풀이 2
# 변수 선언 및 입력
n = int(input())
given_inputs = list(map(int, input().split()))
numbers = [
    (num, i)
    for i, num in enumerate(given_inputs)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key = lambda x: (x[0], x[1]))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, (_, index) in enumerate(numbers):
    answer[index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')
