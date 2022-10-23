"""
16637 괄호 추가하기
"""

# def pascal(height, m):
#     if m == 0 or m == height:
#         return 1
#     elif m < 0 or height < m :
#         return 0
#     else:
#         return pascal(height -1 , m - 1) + pascal(height - 1, m)
# n = 4
# for i in range(4):
#     print(pascal(n, i), end=' ')
#     print()

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

def C(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def pascal(n):
    if n == 1:
        print(1)

    else:
        pascal(n - 1)
        m = []
        for i in range(n):
            if i == 0 or i == n - 1:
                m.append(1)
            else:
                s = C(n - 1, i)
                m.append(s)

        m = map(str, m)
        print(" ".join(m))


a = int(input())
pascal(a)