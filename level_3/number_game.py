import heapq
def solution(A, B): # 숫자 게임
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while B: # A팀이 가장 작은 숫자 가진 사람과 B팀 가장 작은 숫자 가진 사람 비교.
        if B[0]>A[0]:  #B팀의 숫자가 크다면 승점 1점 추가.
            heapq.heappop(B)
            heapq.heappop(A)
            answer += 1
        else :#B팀의 숫자가 작다면 B팀의 그 다음으로 숫자 작은 사람과 비교할 준비.
            heapq.heappop(B)
    return answer

a= [2,2,2,2]
b = [1,1,1,1]
solution(a,b)