"""
리트코드 819 가장 흔한 단어
"""

import sys, re
from collections import Counter
input = sys.stdin.readline
s = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def mostCommonWord(paragraph: str, banned: list) -> str:
    print(re.sub(r'[^\w]', ' ', paragraph).lower().split())
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]



print(mostCommonWord(s, banned))