for tt in range(1,int(input())+1):
    n, m = map(int,input().split())
    print(f'#{tt} {len(set(input().split())&set(input().split()))}')

