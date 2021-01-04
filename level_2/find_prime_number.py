import itertools, math
def prime_number_cnt(number_list): # 소수의 개수 반환
    answer = 0
    for number in number_list:
        if number>1 : # 값이 1과 같거나 작으면 처음부터 소수가 아니기 때문
            for i  in range(2, int(math.sqrt(number))+1): # 소수 판별
                if number%i == 0:
                    break
            else :
                answer +=1
    return answer

def solution(numbers):
    number_list = list(numbers)
    int_list = []
    for i in range(1,len(number_list)+1): #숫자를 순열로 바꾸어 나올 수 있는 경우의 수 나열
        str_list = list(map(''.join, itertools.permutations(number_list, i))) #숫자의 형태로 변경
        int_list +=list(map(int, str_list))
    set_numbers = set(int_list) # 경우의 수에서 중복되는 숫자 제거
    return prime_number_cnt(set_numbers) # 소수 개수 판별 후 반환

numbers = "17"
print(solution(numbers))