from itertools import chain
dir_r = [1,0,-1]  # 순서대로 왼쪽 아래로, 오른쪽으로, 왼쪽 위로 갈때의 row값
dir_c = [0,1,-1]  # 순서대로 왼쪽 아래로, 오른쪽으로, 왼쪽 위로 갈때의 col값
def solution(n): # 삼각 달팽이
    cnt = 0 #숫자
    triangle = [[0]*i for i in range(1,n+1)]
    target = n*(n+1)/2  # 마지막 숫자
    dir = 0  # 왼쪽 아래로, 오른쪽으로, 왼쪽 위를 결정
    row, col = 0, 0
    while cnt <target :
        # print(row,col)
        cnt +=1
        triangle[row][col]=cnt
        next_row, next_col = row +dir_r[dir], col + dir_c[dir]
        if next_row<0 or next_row>n-1 or next_col<0 or next_col>next_row or triangle[next_row][next_col]!=0:  # 다음 이동할 곳이 왼쪽 아래로, 오른쪽으로, 왼쪽 위를 결정
            dir = (dir+1)%3
            row += dir_r[dir]
            col += dir_c[dir]
            continue
        row=next_row
        col=next_col
    # print(triangle)
    return list(chain(*triangle)) #2차원 배열 ->1차원 배열
solution(6)