from collections import deque
def solution(board, moves): # 크레인 인형뽑기 게임
    answer = 0
    stack = []
    item = [ 0 for _ in range(len(board))]
    queue = deque(moves)
    for col in range(len(board)):
        for row in range(len(board)):
            if board[row][col] != 0:
                item[col] = row
                break
    while queue:
        cur_loc = queue.popleft()
        if item[cur_loc-1] == len(board):
            continue
        if stack:
            if board[item[cur_loc-1]][cur_loc-1] == stack[-1]:
                stack.pop()
                answer +=2
            else:
                stack.append(board[item[cur_loc-1]][cur_loc-1])
            item[cur_loc-1] +=1
        else:
            stack.append(board[item[cur_loc-1]][cur_loc-1])
            item[cur_loc-1] += 1

    return answer
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))