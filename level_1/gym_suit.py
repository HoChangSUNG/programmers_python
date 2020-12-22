n = 3
reserve = [3]
lost = [1]
def solution(n, lost, reserve):#체육복
    gym_suit = [1]*n#모든 학생이 체육복이 있다고 가정
    reserve_index =[]
    for suit_lost in lost :#체육복을 잃어버린 학생의 경우
        gym_suit[suit_lost - 1] -= 1
    for suit_reserve in reserve :#체육복 여분이 있는 경우
        gym_suit[suit_reserve - 1] += 1
    for i in range(len(gym_suit)) :#체육복 여분이 있는 학생만 선택하여 리스트 구성(여분 있는 학생의 인덱스(번호) 추출)
        if gym_suit[i] ==2 :
            reserve_index.append(i)
    # print(gym_suit)
    for idx in reserve_index :#여분이 있는 학생들의 인덱스(번호)들

        if idx == 0 : #여분 있는 학생이 1번 학생인 경우
            if gym_suit[idx + 1] == 0:
                gym_suit[idx + 1] =1

                continue
        elif idx == len(gym_suit) - 1 :#여분 있는 학생이 마지막 번호의 학생인 경우
            if gym_suit[idx - 1] == 0 :
                gym_suit[idx - 1] = 1
                continue
        else :#여분 있는 학생이 2번 ~ 마지막 번호 전까지의 학생일 경우
            if gym_suit[idx - 1] == 0:
                gym_suit[idx - 1] = 1
                continue
            else :
                if gym_suit[idx + 1] == 0 :
                    gym_suit[idx + 1] = 1
                    continue
    student_belong_gym_suit = n
    for check in gym_suit :
        if check == 0:
            student_belong_gym_suit -= 1
    # print(gym_suit)
    # print(student_belong_gym_suit)
    return student_belong_gym_suit

solution(n,lost,reserve)
