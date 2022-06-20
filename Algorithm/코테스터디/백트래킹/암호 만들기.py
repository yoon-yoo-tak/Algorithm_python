"""
암호 만들기
모음 1개 자음 2개
오름차순
c 개 중에 l개 고르는 조합
"""
import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = sorted(input().split())
vowel = 'aeiou'
selected = []
def count_alpha():  # 모음의 갯수 세기
    cnt = 0
    for i in selected:
        if i in vowel:
            cnt += 1
    return cnt

def rec(k, cnt): # 조합(combinations)
    if k == c:
        if cnt == l:
            vowel_cnt = count_alpha()
            if vowel_cnt >= 1 and len(selected) - vowel_cnt >= 2:
                print(''.join(selected))
    else:
        selected.append(alpha[k])
        rec(k + 1, cnt + 1)
        selected.pop()
        rec(k + 1, cnt)


rec(0, 0)

