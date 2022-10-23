"""
완탐 딱대 ^^
"""

def solution(users, emoticons):
    rate = [0.9, 0.8, 0.7, 0.6]
    selected = []
    def rec(k): # 중복순열
        if k == len(emoticons):  # k개 뽑았다!
            """
            만약에 i번째 이모티콘의 할인율이 user가 원하는것보다 높으면 ? 산다 >> 다 사본다.
            그게 user의 예산을 넘으면? 이모티콘 플러스 구독한다.
            """
            total_register = 0
            total_money = 0
            for user_rate, user_amount in users:
                temp_money = 0
                for i in range(len(selected)):
                    if 100 - int(selected[i] * 100) >= user_rate:  # 유저가 원하는 할인율보다 높으면?
                        temp_money += emoticons[i] * selected[i]
                    if temp_money >= user_amount:
                        total_register += 1
                        break
                else:  # 다 살때까지 예산 안넘엇으면? 가입안한다.
                    total_money += temp_money
            answer.append([total_register, int(total_money)])
        else:
            for i in range(len(rate)):
                selected.append(rate[i])
                rec(k + 1)
                selected.pop()
    answer = []
    rec(0)  # 완탐 '헤줘'
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]

print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]


