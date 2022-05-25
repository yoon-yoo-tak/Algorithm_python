"""
4371 항구에 들어오는 배
"""
for tc in range(int(input())):
    N = int(input())
    happy = list(int(input()) for _ in range(N))

    ships = set()
    answer = 0
    for i in range(1, len(happy)):
        if happy[i] in ships:
            continue
        gap = happy[i] - 1
        for j in range(1 + gap, happy[-1] + 1, gap):
            ships.add(j)
        answer += 1

    print(f'#{tc + 1} {answer}')


