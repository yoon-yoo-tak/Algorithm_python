ls = dict()
ls['A+'] = 4.5
ls['A0'] = 4.0
ls['B+'] = 3.5
ls['B0'] = 3.0
ls['C+'] = 2.5
ls['C0'] = 2.0
ls['D+'] = 1.5
ls['D0'] = 1.0
ls['F'] = 0.0

score_sum = 0
total_sum = 0
for _ in range(20):
    a, score, grade = input().split()
    if grade == 'P':
        continue
    score_sum += float(score)
    total_sum += (float(score) * ls[grade])

print(f'{total_sum / score_sum:.6f}')