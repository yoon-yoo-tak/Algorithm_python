"""
짝지어제거하기

"""
def solution(s):
    answer = -1
    ls = []
    for i in s:
        if len(ls) == 0:
            ls.append(i)
        elif ls[-1] == i:
            ls.pop()
        else:
            ls.append(i)
    if len(ls) == 0:
        return 1
    return 0

print(solution('cdcd'))