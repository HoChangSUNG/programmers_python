def solution(triangle):# 정수 삼각형
    d = [[0]*i for i in range(1,len(triangle)+1)]
    d[0][0]=triangle[0][0]

    for i in range(len(d)-1):
        for j in range(len(d[i])):
            # 현재 위치에서 내려갈 수 있는 위치가 최댓값이 되도록 값을 업데이트 해준다
            left_down = d[i][j] + triangle[i+1][j]
            right_down = d[i][j] + triangle[i+1][j+1]

            if left_down>d[i+1][j]:
                d[i+1][j] = left_down

            if right_down>d[i+1][j+1]:
                d[i+1][j+1] = right_down

    return max(d[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)