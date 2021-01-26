def solution(tickets): # 여행경로, 다른 사람 코드 참고
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]
    for k in t.keys():
        t[k].sort(reverse=True)
    st = ["ICN"]
    answer = []
    while st :
        top = st[-1]
        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(t[top].pop())
    answer.reverse()
    return answer
tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(tickets))