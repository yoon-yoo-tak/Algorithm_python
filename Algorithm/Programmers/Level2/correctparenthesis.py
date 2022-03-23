"""

레벨 2 올바른 괄호

"""

def solution(s):
    ls = []
    for i in range(len(s)):
        if s[i] == '(':
            ls.append('(')
        else:
            if len(ls) > 0:
                ls.pop()
            else:
                return False
    return True if len(ls) == 0 else False  # len(ls) == 0 으로 간단하게 쓸 수 있다.

print(solution('(())()'))
