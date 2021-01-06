def solution(n): # 점프와 순간이동
    # 6 -> 3 -> 2 -> 1 -> 0
    # 순간이동 점프 순간이동 점프
    answer = 0
    while n != 0 :
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
    return answer
n = 6
print(solution(n))
