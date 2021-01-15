from collections import deque
move={ # 명령어
    'U':[0,1],
    'D':[0,-1],
    'R':[1,0],
    'L':[-1,0]
}
def solution(dirs): # 방문 길이
    queue = deque(dirs) # 명령어 저장
    cur_x, cur_y = 0,0
    visited = [] # 이동전, 이동후 좌표 저장,처음 가는 경로일 경우 저장 ex) 0,0 에서 1,1로 이동 ->[(0,0),(1,1)]
    while queue:
        dir = queue.popleft()
        temp_x, temp_y = cur_x + move[dir][0], cur_y + move[dir][1] # 이동한 좌표
        if temp_x>5 or temp_x<-5 or temp_y>5 or temp_y<-5: # 정해진 좌표평면의 범위를 벗어날 경우
            print("명령어:", dir, "이동전:", (cur_x,cur_y), "이동후:", (temp_x,temp_y),"좌표 범위를 벗어남")
            continue
        else :
            path = [(cur_x,cur_y),(temp_x,temp_y)]
            print("명령어:", dir, "이동전:", path[0], "이동후:", path[1])
            path.sort()
            cur_x, cur_y = temp_x, temp_y
            if path not in visited: # 처음 지나가는 경로일 경우
                visited.append(path)
    # print(visited)
    return len(visited)

print(solution("LULLLLLLU"))