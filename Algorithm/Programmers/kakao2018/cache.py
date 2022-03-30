"""

캐시

"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer