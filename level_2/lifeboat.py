from collections import deque
# 1.오름차순 정렬
# 2.0번째와 마지막번째 인덱스의 값(몸무게)을 비교하여 limit 과 같거나 작으면 보트에 넣는다
# 3.큐가 빌때까지 시도한다.
def solution(people, limit):
    n=limit
    people.sort(reverse=True)
    queue = deque(sorted(people, reverse=True))
    answer = 0

    while queue : # 한 구명보트에 최대 2명씩 넣는다(제일 무거운 몸무게,가장 가벼운 몸무게의 합이 구명보트가 버틸 수 있는 무게보다 작다면)
        answer +=1
        limit -= queue.popleft()
        if len(queue) != 0 and limit >=queue[-1]:
            queue.pop()
        limit=n
    return answer
people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))