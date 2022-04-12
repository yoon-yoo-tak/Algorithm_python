"""
리트코드 937 로그파일 재정렬

"""
# 람다와 + 연산자 이용
def reorderLogFiles(self, logs: list) -> list:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    return letters + digits