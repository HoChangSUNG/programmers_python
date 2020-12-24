from collections import deque
def solution(priorities, location): # 프린터
    queue_priorities = deque(priorities) # 우선순위 queue에 저장
    queue_document=deque()
    answer = 0

    for i in range(len(priorities)) : # True/False가 저장된 queue 생성
        if i == location: # 인덱스와 위치가 같을 경우 True입력(True가 이제부터 location 역할)
            queue_document.append(True)
        else : # False입력
            queue_document.append(False)

    while len(queue_priorities)>1:
        delete_priorities = queue_priorities.popleft()
        delete_document = queue_document.popleft()
        if delete_priorities >= max(queue_priorities) : # 우선순위가 제일 높은 경우 인쇄
            answer += 1
            if delete_document : # 내가 인쇄 요청한 문서가 인쇄될때 몇번째로 인쇄되었는지 반환
                return answer
        else:#우선순위가 낮을 때
            queue_priorities.append(delete_priorities)
            queue_document.append(delete_document)
    return answer+1 # 인쇄 요청한 문서가 제일 마지막에 인쇄될때

priorities=[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))
