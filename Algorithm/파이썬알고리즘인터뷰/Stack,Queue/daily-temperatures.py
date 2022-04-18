"""
리트코드 739 일일 온도
"""

def dailyTemperature(temperatures: list) -> list:
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer