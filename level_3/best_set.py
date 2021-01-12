def solution(n, s): # 최고의 집합
    answer = []
    if n > s: # 최고의 집합이 없는 경우
        return [-1]

    while n>0:# 최고의 집합이 있는 경우
        num = s//n
        s -= num
        n -= 1
        answer.append(num)
    return answer

n = 2
s = 8
print(solution(n,s))