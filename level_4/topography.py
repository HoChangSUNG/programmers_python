import sys
from collections import deque
sys.setrecursionlimit(10**6)
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def land_num_bfs(land,land_num_map,visited,i,j,land_num,height): # 지형 이동
    queue = deque()
    queue.append([i,j])
    visited[i][j]=True
    land_num_map[i][j]=land_num
    while queue:
        r,c = queue.pop()
        for i in range(4):
            t_r,t_c = r+dr[i],c+dc[i]
            if -1<t_r<len(land) and -1<t_c<len(land[0]):
                diff = abs(land[t_r][t_c]-land[r][c])
                if diff<=height and not visited[t_r][t_c]:
                    queue.append([t_r,t_c])
                    visited[t_r][t_c] = True
                    land_num_map[t_r][t_c] = land_num

def landLadder(land,land_num_map,dist):
    row_size,col_size = len(land),len(land[0])
    for r in range(row_size):
        for c in range(col_size):
            cur_num=land_num_map[r][c]
            for dr,dc in [(1,0),(0,1)]:
                t_r,t_c = r+dr,c+dc
                if t_r<row_size and t_c<col_size and land_num_map[r][c] != land_num_map[t_r][t_c]:
                    next_num = land_num_map[t_r][t_c]
                    if (min(cur_num,next_num),max(cur_num,next_num)) not in dist:
                        dist[(min(cur_num, next_num), max(cur_num, next_num))] = abs(land[r][c] - land[t_r][t_c])
                    else:
                        dist[(min(cur_num,next_num),max(cur_num,next_num))]=min(dist[(min(cur_num,next_num),max(cur_num,next_num))],abs(land[r][c]-land[t_r][t_c]))

def find(a,parent):
    if parent[a]==a:
        return a
    parent[a]=find(parent[a],parent)
    return parent[a]

def union(a,b,parent):
    a_parent,b_parent = find(a,parent),find(b,parent)
    parent[b_parent] = a_parent

def solution(land, height):
    answer = 0
    row_size,col_size = len(land),len(land[0])
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    land_num_map = [[0 for _ in range(col_size)] for _ in range(row_size)]
    land_num_cnt=0
    # 땅 구역 나누기
    for i in range(row_size):
        for j in range(col_size):
            if not visited[i][j]:
                land_num_bfs(land,land_num_map,visited,i,j,land_num_cnt,height)
                land_num_cnt+=1

    dist = dict()
    landLadder(land,land_num_map,dist)
    dist_ = sorted(dist.items(),key=lambda x:x[1])

    cnt = 0
    parent = [i for i in range(land_num_cnt)]
    for (a,b),w in dist_:

        if find(a,parent)!=find(b,parent):
            union(a,b,parent)
            cnt+=1
            answer += w

        if land_num_cnt - 1 == cnt:
            break
    return answer
# land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
# height =1
# print(solution(land,height))