from collections import deque
def solution(n):  # 올바른 괄호의 갯수
    queue = deque()
    queue.append((0,0))  # 열린 괄호, 닫힌 괄호 개수
    answer = 0
    while queue :
        open_p, close_p = queue.popleft() # 여는 괄호, 닫는 괄호
        temp_open_p, temp_close_p = open_p + 1, close_p + 1
        if open_p >= close_p and temp_open_p <= n:  # 여는 괄호를 추가할 수 있는 경우
            queue.append((temp_open_p, close_p))
            if temp_open_p == n and close_p == n:  # 올바른 괄호가 완성되면 개수 +1
                answer += 1

        if open_p > close_p and close_p <= n:  # 닫는 괄호를 추가할 수 있는 경우
            queue.append((open_p, temp_close_p))
            if open_p == n and temp_close_p == n:  # 올바른 괄호가 완성되면 개수 +1
                answer += 1
    return answer

solution(3)