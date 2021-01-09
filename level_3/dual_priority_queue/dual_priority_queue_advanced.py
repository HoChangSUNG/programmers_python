import heapq
def solution(operations): # 이중우선순위큐
    heap = []

    for op in operations:
        operation, operand = op.split()[0], op.split()[1]
        if operation == "I":
            heapq.heappush(heap,int(operand))
        else :
            if heap :
                if operand == "1" :
                    heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
                else:
                    heapq.heappop(heap)

    if heap :
        answer = [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
        return answer
    else :
        return [0, 0]
    # print(heap)
operations = ['I 7','I 5','I -5','D -1']
print(solution(operations))