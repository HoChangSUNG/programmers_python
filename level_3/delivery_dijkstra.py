from queue import PriorityQueue
def dijkstra(road, N):
    INF = 987654321
    dist = [float('inf') for i in range(N + 1)]
    road.sort()
    pq = PriorityQueue()
    pq.put([0, 1]) # 시작점에서부터의 거리, 현재 노드
    dist[1] = 0 # 시작 노드 초기화
    while not pq.empty(): # while pq로 하면 안됨.
        cost, here = pq.get() #현재 노드까지의 비용, 현재 노드
        print("cost, here", cost, here)
        if cost > dist[here]: #현재 노드의 비용이 dist값보다 클 때
            continue
        for i in range(len(road)):
            if road[i][0] == here:
                there, nextCost = road[i][1], road[i][2] + cost
                if nextCost < dist[there]: # 현재 노드까지의 비용이 dist값보다 작을때
                    dist[there] = nextCost
                    pq.put([nextCost, there])
            elif road[i][1] == here:
                there, nextCost = road[i][0], road[i][2] + cost
                if nextCost < dist[there]: # 현재 노드까지의 비용이 dist값보다 작을때
                    dist[there] = nextCost
                    pq.put([nextCost, there])
    print(dist)
    return dist
input_N = 5
input_road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
input_K = 3
def solution(N, road, K): # 배달, 다른 사람의 코드 참고함.
    answer = 0
    dist = dijkstra(road, N)
    print("dist is", dist)
    for d in dist:
        if d <= K:
            answer += 1
    return answer
print(solution(input_N, input_road, input_K))  # 4 가 나와야 합니다