"""
2로 나누어 떨어지는 경우
일의 자리가 5인 경우
3으로 나누어 떨어지면서 9로는 나누어 떨어지지 않는 수
위 조건을 모두 만족하지 않는 수
"""
def is_perfect(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True


a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if is_perfect(i):
        cnt += 1
print(cnt)
