import sys

input = sys.stdin.readline


class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

s_code, m_point, time = input().split()

s = Spy(s_code, m_point, time)

print(f'secret code : {s.secret_code}')
print(f'meeting point : {s.meeting_point}')
print(f'time : {s.time}')