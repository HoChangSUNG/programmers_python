from collections import deque
def solution(progresses, speeds):#기능개발
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    answer = []
    date = 0
    while progresses_queue :
        date +=1
        for i in range(len(progresses_queue)) : #작업
            if progresses_queue[i]<100 :
                progresses_queue[i]+=speeds_queue[i]
        count = 0
        while progresses_queue :#배포가능여부 확인
            if progresses_queue[0]>=100 :
                count+=1
                progresses_queue.popleft()
                speeds_queue.popleft()
            else :
                break
        if count :
            answer.append(count)
    return answer
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))