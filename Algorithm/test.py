import math
from itertools import permutations

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    ls = []
    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers, i)
        for i in perm:
            num = int(''.join(i))
            ls.append(num)
    ls = list(set(ls))
    for i in ls:
        if is_prime_number(i):
            answer += 1
    return answer
print(solution('17'))