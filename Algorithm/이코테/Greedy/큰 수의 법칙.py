"""
이코테 그리디 파트 연습문제 - 큰 수의 법칙

1. 아이디어
2. 시간복잡도
3. 자료구조
"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰수
second = data[n - 2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # k번 동안 가장 큰 수 더해준다
        if m == 0: # 모두 m 번 더했다면 종료
            break
        result += first # 큰수를 k 번 더해줌
        m -= 1 # 남은 횟수 -1
    if m == 0: # 위의 루프 끝났는데  m 이 0이라면 종료
        break
    result += second # 두번째로 큰 수 한번 더해줌
    m -= 1 # 횟수 -1

print(result)
