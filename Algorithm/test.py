num_selection, num_people = map(int, input().split())  # 변수 선언
selected = [0 for _ in range(num_people)] # 뽑힌 사람의 번호를 저장할 배열을 뽑을 명수만큼 선언


def choose_num(curr_num: int):  # curr_num부터 마지막 사람까지 고르는 선택지를 구해줌
    if curr_num == num_people: # 모든 사람이 각자 선택을 했으면
        print(*selected)       # 출력
        return

    else:  # 아직 선택해야하는 사람이 남아있다면
        for num in range(1, num_selection + 1): # 1 ~ num_selection 까지 반복하겠다.
            selected[curr_num] = num  # selected배열의 curr_num 번지에 현재 뽑은 num을 넣겠다.
            choose_num(curr_num + 1)  # 다음 번지를


choose_num(0)
