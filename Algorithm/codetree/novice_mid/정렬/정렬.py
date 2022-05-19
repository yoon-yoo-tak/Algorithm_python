import sys

input = sys.stdin.readline

n, k, t = tuple(input().split())
n, k = int(n), int(k)



def starts_with(a, b):

    if len(a) < len(b):
        return False


    return a[:len(b)] == b


words = []
for _ in range(n):
    word = input()
    if starts_with(word, t):
        words.append(word)

words.sort()

print(words[k - 1])