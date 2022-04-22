"""
1680 쓰레기 수거

쓰레기의 양이 용량에 도달했을 때.
그 지점의 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 될 때.
더 이상 쓰레기를 실을 지점이 없을 때.
"""
if __name__ == '__main__':
    for _ in range(int(input())):
        w, n = map(int, input().split())
        testcase = []
        for __ in range(n):
            x_i, w_i = map(int, input().split())
            testcase.append([x_i, w_i])

        capacity = 0
        distance = 0
        previous_value = 0
        for i in testcase:
            # i[0]: 쓰레기장으로부터의 거리   i[1]: 쓰레기의 양
            if capacity + i[1] < w:
                distance += i[0] - previous_value
                capacity += i[1]
            elif capacity + i[1] == w:
                distance += (i[0] - previous_value) + i[0] * 2
                capacity = 0
                if testcase.index(i) == n - 1:
                    distance -= i[0] * 2
            elif capacity + i[1] > w:
                capacity = i[1]
                distance += (i[0] - previous_value) + i[0] * 2
            previous_value = i[0]

        # 모든 쓰레기를 수거하여 다시 쓰레기장으로 돌아갈 때
        if testcase.index(i) == n - 1:
            distance += i[0]

        print(distance)
