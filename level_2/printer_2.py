from collections import deque
def solution(priorities, location): # 프린터
    queue_priorities = deque(priorities)
    answer = 0
    while len(queue_priorities)>1:
        delete_priorities = queue_priorities.popleft()
        location -= 1 # 내가 인쇄 요청한 문서 위치

        if delete_priorities >= max(queue_priorities): # 문서가 인쇄될때
            answer+=1
            if location == -1: # 내가 인쇄 요청한 문서 인쇄될 때
                return answer
        elif delete_priorities < max(queue_priorities):
            if location == -1: # 내가 인쇄 요청한 문서 위치
                location += len(queue_priorities) + 1
            queue_priorities.append(delete_priorities)

    return answer+1 # 인쇄 요청한 문서가 제일 마지막에 인쇄될때

priorities=[2, 1, 3, 2]
location = 2
print(solution(priorities,location))
