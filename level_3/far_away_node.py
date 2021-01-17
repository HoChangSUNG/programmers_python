from collections import deque
def dijkstra(road, N): # 가장 먼 노드
    dist = [0 for i in range(N + 1)] #거리를 저장할 리스트
    adjacent_nodes = {i : []for i in range(1,N+1)} # 인접한 노드 저장할 dict
    for u, v in road: # 인접 리스트로 표현
        adjacent_nodes[u].append(v)
        adjacent_nodes[v].append(u)
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for adj in adjacent_nodes[node]: #인접 노드들 방문
            if dist[adj] == 0 and adj != 1:# 1번 노드는 항상 0이여야 하기 때문.
                dist[adj] = dist[node] + 1# 방문하지 않은 노드들의 거리를 저장
                queue.append(adj) # 방문한 노드를 queue에 저장.
    return dist
def solution(n, edge):
    result=dijkstra(edge, n)
    a = max(result) #가장 멀리 떨어진 노드의 거리
    return result.count(a)#가장 멀리 떨어진 노드의 개수 리턴

n=6
vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,vertex))