import math
def solution(n, k): # 줄 서는 방법
    k -= 1 # 인덱스가 0부터 시작해서 1을 우선 뻬줌
    list_n = [i for i in range(1,n+1)]
    answer = []
    while list_n :
        number = list_n.pop(k//math.factorial(n-1))
        answer.append(number)
        next_k = k % math.factorial(n - 1)
        k = next_k
        n -= 1
    return answer
n = 3
k = 5
print(solution(n, k))