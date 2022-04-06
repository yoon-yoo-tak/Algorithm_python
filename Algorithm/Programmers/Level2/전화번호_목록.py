"""
프로그래머스 레벨 2 - 전화번호 목록

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

def solution(phone_book):
    phone_book = sorted(phone_book)
    print(list(zip(phone_book, phone_book[1:])))
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True

print(solution(["12","123","1235","567","88"]))