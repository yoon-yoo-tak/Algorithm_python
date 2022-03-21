"""
H-Index 논문 n편중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 H-Index이다.
"""

def solution(citations):
    citations.sort()
    for idx , citation in enumerate(citations):
        if citation >= len(citations) - idx :
            return len(citations) - idx
    return 0

print(solution([3,0,6,1,5]))