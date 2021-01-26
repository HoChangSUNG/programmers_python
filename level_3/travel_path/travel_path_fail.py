def solution(tickets): # 여행경로, 테스트 케이스1,2 실패
    path = ['ICN']
    while True:
        find = path[-1]
        min_index = -1
        for i in range(len(tickets)):
            if tickets[i][0] == find:
                if min_index == -1:
                    min_index = i
                if tickets[min_index][1]>tickets[i][1]:
                    min_index = i
        if len(tickets) == 0:
            break
        path.append(tickets[min_index][1])

        tickets.pop(min_index)
    return path
tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(tickets))