"""

셔틀 버스

"""
def solution(n, t, m, timetable):
    timetable = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable])

    corn = 540
    shuttle = 540

    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= shuttle:
                corn = timetable.pop(0) - 1
            else:
                corn = shuttle
        shuttle += t
    return f'{str(corn//60).zfill(2)}:{str(corn%60).zfill(2)}'