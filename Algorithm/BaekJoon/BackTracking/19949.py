"""
19949 영쟈의 시험

"""
ans = list(map(int, input().split()))
li, cnt = [], 0
def rec(k):
    global cnt
    if k == 10:
        s = 0
        for j in range(10):
            if li[j] == ans[j]:
                s += 1
        if s >= 5:
            cnt += 1
        return;
    for i in range(1, 6):
        if k > 1 and li[k - 2] == li[k - 1] == i:
            continue
        li.append(i)
        rec(k + 1)
        li.pop()
rec(0)
print(cnt)