from collections import deque
def solution(m, n, puddles): # 등굣길, 효율성테스트 실패, 테스트케이스 8번 시간초과
    queue = deque()
    queue.append((1,1,0))# x좌표, y좌표, 거리
    min_dist = float('INF')
    answer = 0
    puddle = set()
    for x,y in puddles:
        puddle.add((x,y))
    while queue :
        cur_x,cur_y,cur_dist = queue.popleft()
        if cur_dist>min_dist:
            return answer
        if cur_x == m and cur_y == n:
            if min_dist>=cur_dist:
                min_dist=cur_dist
                answer += 1

        temp_right_x, temp_bottom_y, temp_dist = cur_x+1, cur_y+1, cur_dist + 1
        if 1<=temp_right_x<=m and (temp_right_x,cur_y) not in puddle:
            queue.append((temp_right_x,cur_y,temp_dist))
        if 1<=temp_bottom_y <=n and (cur_x, temp_bottom_y) not in puddle:
            queue.append((cur_x, temp_bottom_y, temp_dist))
    return answer
m = 4
n=3
puddles = [[2, 2]]
print(solution(m,n,puddles))