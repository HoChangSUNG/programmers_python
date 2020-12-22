
def to_ternary(n) :
    answer = ''
    while True :
        answer = str(n % 3) + answer
        n = n//3
        if n == 1 :
            answer =str(n) + answer
            return answer
        if n == 0 :
            return answer

    return answer

def reverse_ternary(n) :
    ternary_list = list(n)
    mid = len(n) //2
    for idx in range(mid):
        ternary_list[idx],ternary_list[- (idx + 1)] = ternary_list[- (idx + 1)], ternary_list[idx]
    return ternary_list
def to_decimal(n) :
    length = len(n)
    answer = 0
    for idx in range(length) :
        index = length - idx - 1
        answer += int(n[idx])*(3**index)
    return answer
def solution(n):#3진법 뒤집기
    ternary = to_ternary(n)
    reversed_ternary = reverse_ternary(ternary)
    return to_decimal(reversed_ternary)

