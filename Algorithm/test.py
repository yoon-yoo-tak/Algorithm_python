a, b = list(input().split())
c = []
result = ""
if len(a) == len(b):
    for i in range(1, len(a) + 1):
        c.append(int(a[-i]) + int(b[-i]))
    c.reverse()
    for i in c:
        result += str(i)
    print(int(result))
elif len(a) != len(b):  # 길이가 다르면
    for i in range(1, min(len(a), len(b)) + 1):  # 짧은것의 길이까지
        c.append(int(a[-i]) + int(b[-i]))  # 맨 뒤에서부터 더해서 넣는다.
        # print('a[-i]', a[-i], 'b[-i]', b[-i], ', -i :', -i)
        # print(c)
    if len(a) < len(b):  # b가 a보다 길면
        # for j in range((max(len(a), len(b)) + 1) - (min(len(a), len(b)) + 1)):
        for j in range((max(len(a), len(b)) + 1) - (min(len(a), len(b)) + 1) - 1, -1, -1): # 처음으로 b가 a보다 길어지는 인덱스부터 0까지.
            #   c.append(int(b[-j]))  >> j 의 범위가 [0 ~ 길이차이] 인데 - 를 붙이면 맨앞자리 > 맨뒤 > 맨뒤에서 2번째 > ...  이렇게 불러옴.
            #                            예제는 길이차이가 1인거까지밖에 없어서 맨앞자리만 갖고오면 맞기때문에 맞게 됨. 자릿수 차이 두자리 이상이면 틀림.
            c.append(int(b[j]))
            # print(c)
    elif len(b) < len(a):
        for j in range((max(len(a), len(b)) + 1) - (min(len(a), len(b)) + 1) - 1, - 1, -1):
            # print('a[-j]', a[-j], ', -j  =', -j)
            c.append(int(a[j]))
            # print(c)
    c.reverse()
    for i in c:
        result += str(i)
    print(int(result))
