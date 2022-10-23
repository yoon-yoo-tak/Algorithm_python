"""
today := yyyy.mm.dd
terms := A 6, B 3, C 12 == A 약관 6개월
privacies := "2021.05.12 A", ...
"""
def translate(s: str) -> int:
    yy, mm, dd = s.split('.')
    return 28 * 12 * int(yy) + 28 * int(mm) + int(dd)

def solution(today, terms, privacies):
    answer = []
    term = dict()
    tod = translate(today)
    for i in terms:
        a, b = i.split()
        term[a] = int(b)

    for i in range(len(privacies)):
        date, x = privacies[i].split()
        trans_date = translate(date)
        trans_date += term[x] * 28
        if trans_date <= tod:
            answer.append(i + 1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

"""
"2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

> [1, 3]
"""