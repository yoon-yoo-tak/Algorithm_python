"""
3699 주차 빌딩
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    h, l = map(int, input().split())
    tower = [list(map(int, input().split())) for _ in range(h)]
    car_pos = []
    for i in range(h):
        for j in range(l):
            if tower[i][j] != -1:
                car_pos.append([i, j, tower[i][j]])
    # car_pos = [[i, j, tower[i][j]] for j in range(l) for i in range(h) if tower[i][j] != -1]
    car_pos.sort(key=lambda x: x[2])  # 1, 2, 3...번 순서로 정렬
    ans = 0  # 총 걸린 시간 담을 정수
    curr_pos = [0] * h  # 1 ~ h층의 엘베 위치 저장
    for height, width, _ in car_pos:  # height : 차가 있는 층, width : 첫번째 위치부터 차까지의 거리
        ans += 20 * height  # 층 이동 10초, 올라갔다 내려와야해서 곱하기 2
        dist = abs(curr_pos[height] - width)  # 현재 엘베 위치에서 차의 위치까지 거리 절대값
        ans += 5 * min(dist, l - dist)  # 시계방향으로 이동하는게 짧은지, 반시계로 이동하는지 짧은지 판별
        curr_pos[height] = width  # 현재 층의 엘베 위치 변경 (차가 있던 위치로)

    print(ans)
