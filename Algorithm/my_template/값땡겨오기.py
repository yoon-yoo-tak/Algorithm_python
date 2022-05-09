"""
사이사이 빈칸 없애버리는 코드 //  값 땡겨오기 // 빈칸이 있으면 압축
"""
a = [0,1,1,0,2,3,1,0,0,0,3,3,4,2,0,2]

last = 0
for i in range(1, len(a)):
    if a[i] == 0:
        continue
    last += 1  # 이번에 값을 넣을 위치를 알려줌
    a[last] = a[i]  # 그 위치에 값을 넣어줌
for i in range(last + 1, len(a)):
    a[i] = 0

print(a)


