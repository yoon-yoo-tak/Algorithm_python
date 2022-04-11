"""
10866 덱

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    a = input().split()
    if a[0] == 'push_front':
        q.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        q.append(int(a[1]))
    elif a[0] == 'pop_front':
        print(q.popleft() if len(q) > 0 else -1)
    elif a[0] == 'pop_back':
        print(q.pop() if len(q) > 0 else -1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) > 0: print(0)
        else: print(1)
    elif a[0] == 'front':
        print(q[0] if len(q) > 0 else -1)
    else:
        print(q[len(q) - 1] if len(q) > 0 else -1)

