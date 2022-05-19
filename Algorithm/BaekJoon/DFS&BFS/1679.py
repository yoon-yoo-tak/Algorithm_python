from itertools import product
def sol1(nums, max_num):
    length = len(nums)
    pool = range(max_num+1)
    pool = list(filter(lambda x: 0<sum(x)<=max_num, list(product(pool, repeat=length))))

    memo = [False for _ in range((nums[-1]*max_num) + 1)]
    for pair in pool:
        cum = 0
        for i in range(len(pair)):
            cum += pair[i] * nums[i]
        memo[cum] = True

    for num in range(1, len(memo)):
        if not memo[num]: break

    who = 'holsoon' if num % 2 == 0 else 'jjaksoon'
    return '{} win at {}'.format(who, num)

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
print(sol1(nums, k))


