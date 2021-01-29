from collections import deque
def solution(n, computers):
    answer = 0 #네트워크 개수
    visited = []
    queue=deque()
    adjacent_nodes = {i : [] for i in range(n)} # 인접리스트 방식으로 그래프 표현, 문제에서는 노드가 1부터 시작하지만 편의상 0부터 시작
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 :
                if i != j:
                    adjacent_nodes[i].append(j)
    # print(adjacent_nodes)
    while len(visited)!= n: # 모든 노드를 방문할 때까지
        if len(queue)==0: # 인접한 모드 노드를 모두 방문하고, 다음 네트워크의 노드를 찾아야 할 때
            for i in range(n):
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    answer += 1
                    break
        cur_node = queue.popleft()
        for adjacent_node in adjacent_nodes[cur_node]: # 인접 노드 탐색
            if adjacent_node not in visited:
                queue.append(adjacent_node)
                visited.append(adjacent_node)
    # print(visited,answer)
    return answer