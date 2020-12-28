def solution(clothes):#위장
    # (a+1)(b+1)(c+1) -1 = a+b+c +(ab+bc+ca) +abc
    answer = 1
    clothes_dict={}
    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_dict:
            clothes_dict[clothes[i][1]]=[clothes[i][0]]
        else :
            clothes_dict[clothes[i][1]].append(clothes[i][0])
    # print(clothes_dict)
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key]))+1
    answer += -1
    # print(answer)
    return answer
clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))