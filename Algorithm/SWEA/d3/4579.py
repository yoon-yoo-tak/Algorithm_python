"""
4579 세상의 모든 팰린드롬 2
"""
for tc in range(int(input())):
    answer = 'Not exist'
    word = input()
    reversed_word = word[::-1]
    for i in range(len(word)):
        if word[i] == reversed_word[i]:
            continue

        if word[i] == '*' or reversed_word[i] == '*':
            answer = 'Exist'
            break
        else:
            break
    else:
        answer = 'Exist'

    print(f'#{tc + 1} {answer}')