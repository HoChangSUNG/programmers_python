from collections import deque
def solution(n, computers): # 네트워크
    answer = 0 #네트워크 개수
    visited = []
    queue=deque()
    while len(visited)!= n: # 모든 노드를 방문할 때까지
        if len(queue)==0: # 인접한 모드 노드를 모두 방문하고, 다음 네트워크의 노드를 찾아야 할 때
            for i in range(n):
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    answer += 1
                    break
        cur_node = queue.popleft()
        for adjacent in range(len(computers[cur_node])): # 인접 노드 탐색
            if adjacent not in visited and computers[cur_node][adjacent]==1:
                queue.append(adjacent)
                visited.append(adjacent)
    # print(visited,answer)
    return answer

solution()