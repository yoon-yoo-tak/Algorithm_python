N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
def divide(x, y, n):
    global white, blue
    color = paper[x][y]
    check = True
    for i in range(x, x+n):
        if not check:
            break
        for j in range(y, y+n):
            if color != paper[i][j]:
                check = False
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                break
    if check:
        if color:
            blue += 1 
        else:
            white += 1 
divide(0, 0, N)
print(white)
print(blue)