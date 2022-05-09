
from collections import defaultdict
def solution(survey, choices):
    score = [0, 3 , 2 , 1 , 0 , 1 , 2 , 3]
    mbti = ['RT', 'CF', 'JM', 'AN']
    result = ''
    temp = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] < 4:
            temp[survey[i][0]] += score[choices[i]]
        elif choices[i] > 4:
            temp[survey[i][1]] += score[choices[i]]
    for m in mbti:
        if temp[m[0]] > temp[m[1]]:
            result += m[0]
        elif temp[m[0]] < temp[m[1]]:
            result += m[1]
        else:
            result += m[0]
    return result

print(solution(['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5]))
print(solution(['TR', 'RT', 'TR'], [7, 1, 3]))