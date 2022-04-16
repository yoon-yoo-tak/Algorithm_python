for T in range(int(input())):
    D, L, N = map(int, input().split())
    
    result = 0
    for i in range(N):
        result += D * (1 + L*i/100)
    
    print(f'#{T+1} {int(result)}')