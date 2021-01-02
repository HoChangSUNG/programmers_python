from collections import deque
def solution(brown, yellow):# 카펫
    carpet_size = brown + yellow # 카펫의 가로*세로 크기
    queue = deque()
    for i in range(1, yellow // 2 + 2): #노란색 격자의 형태
        yellow_row = yellow//i
        yellow_col = i
        if yellow % i == 0 and yellow_row >= yellow_col: #카펫 가로 길이가 세로 길이보다 커야 하기 때문
            queue.append((yellow_row, yellow_col))
    print(queue)
    while queue:
        yellow_row, yellow_col = queue.popleft()
        if carpet_size == (yellow_row + 2) * (yellow_col + 2) : #카펫의 크기와 같을 때
            answer = [yellow_row + 2, yellow_col + 2]
            return answer


print(solution(24,24))