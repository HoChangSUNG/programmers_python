def solution(operations): # 이중우선순위큐
    heap = []
    for op in operations:
        operation = op.split()[0]
        operand = op.split()[1]
        if operation == 'I':
            heap.append(int(operand))
            heap.sort(reverse=True)
        else:
            if operand == '1' and heap :
                heap.pop(0)
            elif operand == '-1'and heap:
                heap.pop()
    if heap:
        return heap
    else :
        return [0,0]
operations = ['I 16','D 1']
print(solution(operations))