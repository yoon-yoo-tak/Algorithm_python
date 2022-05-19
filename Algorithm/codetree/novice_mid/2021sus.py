import sys

input = sys.stdin.readline

def day_limit(month):
    if month == 2:
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

m, d = map(int, input().split())
def check(m, d):
    if m <= 12 and d <= day_limit(m):
        return True
    return False

print('Yes' if check(m, d) else 'No')