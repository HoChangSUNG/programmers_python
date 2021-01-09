def solution(n): # 2xn 타일링
    first_num = 0
    second_num = 1
    for i in range(n): # 피보나치 수열
        first_num, second_num = second_num, first_num + second_num
    print(second_num)
    return second_num%1000000007

print(solution(25))