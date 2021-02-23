def solution(board):  # 가장 큰 정사각형 찾기
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==1:
                board[i][j] = min(board[i-1][j-1],board[i][j-1],board[i-1][j]) + 1
    answer = []
    for i in range(len(board)):
        answer.append(max(board[i]))
    return max(answer)**2

board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))