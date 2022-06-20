n = int(input())
people = dict()
for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        people[a] = True
    else:
        people[a] = False
for name in sorted([i for i in people if people[i]], reverse=True):
    print(name)


