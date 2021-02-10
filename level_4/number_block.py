import math
def solution(begin, end):  # 숫자블록
    answer= []
    for num in range(begin,end+1):
        for prime in range(2, int(math.sqrt(num) + 1)):  # 소수판별
            if num % prime == 0 and num//prime <= 10000000:  # 블록의 번호의 최대 : 10000000
                answer.append(num // prime)
                break
        else:
            if num < 2:  # 블럭의 위치가 1일때
                answer.append(0)
            else:
                answer.append(1)
    return answer

begin = 3
end = 10
solution(begin, end)