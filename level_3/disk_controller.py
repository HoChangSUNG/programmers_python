import heapq
def solution(jobs): # 디스크 컨트롤러
    time_start, time_end, count = -1, 0, 0
    answer = 0
    heap = []
    while count < len(jobs):
        for job in jobs:
            if time_start<job[0] <= time_end: # 작업이 일어나는 시간.
                answer += time_end - job[0] # 요청 ~ 다음 작업 시작까지의 소요 시간
                heapq.heappush(heap,job[1]) # 힙에 넣어준다.
        if len(heap) > 0: # 작업이 있을 때
            answer += heap[0] * len(heap)
            time_start = time_end
            time_end = time_start + heapq.heappop(heap)
            count += 1
        else: # 작업이 없을 때
            time_start = time_end
            time_end = time_start + 1

    return answer//len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

