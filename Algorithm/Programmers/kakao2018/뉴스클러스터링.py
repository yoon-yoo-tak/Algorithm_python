"""

뉴스클러스터링

"""
import re


def solution(str1, str2):
    # 예외처리 추가
    if len(str1) <= 1 and len(str2) <= 1:
        return 65536
    str1 = str1.lower()
    str2 = str2.lower()

    str1List = []
    str2List = []

    pattern = re.compile(r'[a-z]{2}')

    for i in range(len(str1) - 1):
        strr = str1[i] + str1[i + 1]
        if pattern.findall(strr):
            str1List.append(strr)

    for i in range(len(str2) - 1):
        strr = str2[i] + str2[i + 1]
        if pattern.findall(strr):
            str2List.append(strr)

    gyo = set(str1List) & set(str2List)
    hap = set(str1List) | set(str2List)

    gyoplus = 0

    for i in gyo:
        if str1List.count(i) > 1 and str2List.count(i) > 1:
            if str1List.count(i) > str2List.count(i):
                gyoplus += str2List.count(i) - 1
            else:
                gyoplus += str1List.count(i) - 1

    happlus = 0

    for i in hap:
        if str1List.count(i) > 1 or str2List.count(i) > 1:
            if str1List.count(i) > str2List.count(i):
                happlus += str1List.count(i) - 1
            else:
                happlus += str2List.count(i) - 1

                # 마지막에 추가
    if (len(hap) + happlus) == 0:
        return 65536
    if (len(gyo) + gyoplus) == 0:
        return 0

    return int((len(gyo) + gyoplus) / (len(hap) + happlus) * 65536)