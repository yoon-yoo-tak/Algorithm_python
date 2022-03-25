# from itertools import permutations
# from collections import Counter
#
# def solution(numbers, k):
#     answer = 0
#     new_num = numbers
#     perm = permutations(new_num, len(new_num))
#     ls = []
#     for i in perm:
#         count = 0
#         if isInK(i, k):
#             for j in range(len(numbers)):
#                 if numbers[j] != i[j]:
#                     count += 1
#             ls.append(count/2)
#     if len(ls) == 0:
#         answer = -1
#     else:
#         answer = min(ls)
#     return round(answer)
#
# def isInK(perm , k):
#     ls = []
#     for i in range(len(perm)-1):
#         ls.append(abs(perm[i]-perm[i+1]))
#     for i in ls:
#         if i > k:
#             return False
#     return True
#
# print(solution([1,5,4,7,8], 2))

