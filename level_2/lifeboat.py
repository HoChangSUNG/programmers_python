from collections import deque
def solution(people, limit):
    n=limit
    people.sort(reverse=True)
    queue = deque(sorted(people, reverse=True))
    answer = 0

    while queue :
        answer +=1
        limit -= queue.popleft()
        if len(queue) != 0 and limit >=queue[-1]:
            queue.pop()
        limit=n
    return answer
people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))