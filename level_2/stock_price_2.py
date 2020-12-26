from collections import deque
def solution(prices):#주식가격, 효율성 테스트 성공
    queue = deque(prices)
    answer = []
    while queue :#맨 앞의 원소부터 몇초 유지되었는지
        count = 0
        compare = queue.popleft()
        for q in queue :
            if compare > q:
                count +=1
                break
            count+=1
        answer.append(count)
    return answer
prices = [1, 2, 3, 2, 3]
print(solution(prices))