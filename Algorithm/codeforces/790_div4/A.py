import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    a = sum([int(i) for i in s[:3]])
    b = sum([int(i) for i in s[3:]])
    print('YES' if a == b else 'NO')


"""
일단 제 풀이들은
D: 빡구현 (또는 누적합)
E: 누적합 + 파라매트릭 서치
F: 트리맵 + 스위핑
G: 트리DP
H: 세그트리
"""
