from collections import deque
dr = [-1, 0, 1, 0]  # 위,오른,아래,왼쪽
dc = [0, 1, 0, -1]
def solution(maps):  # 게임 맵 최단거리
    visited = set()  # 방문여부
    queue = deque()
    queue.append((0, 0, 1))  # 시작위치 row, col, 지나온 칸 수

    while queue:
        row, col, cnt = queue.popleft()
        if row == len(maps) - 1 and col == len(maps[0]) - 1 :  # 마지막에 도달시
            return cnt

        for i in range(4):  # 상하좌우 이동가능한지 탐색
            temp_row, temp_col = row+dr[i], col+dc[i]
            if 0 <= temp_row < len(maps) and 0 <= temp_col < len(maps[0]) :
                if maps[temp_row][temp_col] == 1 and (temp_row,temp_col) not in visited:
                    visited.add((temp_row, temp_col))
                    queue.append((temp_row, temp_col, cnt+1))
    return -1  # 도달하지 못했을 경우
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))