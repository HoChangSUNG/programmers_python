import heapq

def solution(n, works):  # 야근지수
    work = [-i for i in works]
    heap = work
    heapq.heapify(heap)  # max heap 사용
    while n > 0:

        cur = -heapq.heappop(heap)  # max값
        if cur == 0:  # max값이 0인 경우는 야근 피로도가 0이란 뜻
            return 0
        heapq.heappush(heap, -(cur - 1))  # 현재 작업량에서 -1
        n -= 1  # 남은 시간 최신화
    for i in range(len(heap)):  # 남은 각각의 일의 작업량의 야근지수 구하기
        heap[i] **= 2
    return sum(heap)  # 남은 야근 피로도 리턴


works = [4, 3, 3]
n = 4
solution(n, works)