"""

"""
n, m = 4, 3 # 7명 중 4명을 고르자 !
selected = [0 for _ in range(n)]
def choose(person_idx, cnt):
    # 0번 부터 (person_index - 1) 까지는 0 또는 1을 잘 선택했고,
    # 그 중에서 1을 cnt번 골랐다.
    # 이제 person_idx 부터 마지막 사람(n - 1 번 사람) 까지 모든 조합을 확인해주는 함수
    if person_idx == n:
        if cnt == m:
            for i in range(n):
                if selected[i] == 1:
                    print(i + 1, end=' ')
            print()
        return
    selected[person_idx] = 1
    choose(person_idx + 1, cnt + 1)

    selected[person_idx] = 0
    choose(person_idx + 1, cnt)


choose(0, 0)


