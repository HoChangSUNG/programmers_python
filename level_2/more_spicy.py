import heapq
def solution(scoville, K):# 더 맵게
    mix_count = 0
    heap =[]
    for i in range(len(scoville)) :
        heapq.heappush(heap,scoville[i])

    while True:
        cur_scoville = heapq.heappop(heap)
        if cur_scoville >=K : # 모든 음식의 스코빌 지수 K이상일때
            return mix_count
        elif len(heap) == 0 : # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        elif cur_scoville <K: # 모든 음식의 스코빌 지수 K미만일때
            new_scoville = cur_scoville + heapq.heappop(heap)*2
            heapq.heappush(heap,new_scoville)
            mix_count+=1

li=[1, 2, 3, 9, 10, 12]
k =7
print(solution(li,k))
