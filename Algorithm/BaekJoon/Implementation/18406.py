"""

18406 럭키 스트레이트

"""
n = input()

ls = sorted([x for x in n if x.isalpha()])
a = 0
for i in n:
    if i.isdigit():
        a += int(i)
print(''.join(ls)+str(a))
