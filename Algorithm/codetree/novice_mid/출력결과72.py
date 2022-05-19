def operation(a, b, c):
    if b not in ('+', '-', '/', '*'):
        print('False')
        return
    a = int(a)
    c = int(c)
    if b == '+':
        ans = a + c
    elif b == '-':
        ans = a - c
    elif b == '*':
        ans = a * c
    else:
        ans = a // c
    print(f'{a} {b} {c} = {ans}')

num1, oper, num2 = input().split()

operation(num1, oper, num2)
