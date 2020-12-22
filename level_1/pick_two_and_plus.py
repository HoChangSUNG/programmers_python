def solution(numbers):#두개 뽑아서 더하기
    answer = []
    for i in range(len(numbers)) :#첫번째 인덱스 i
        for j in range(len(numbers)):#두번째 인덱스 j
            if i != j and numbers[i] + numbers[j] not in answer: #인덱스가 같지 않고 더한 값이 이미 존재하지 않을 경우 더하기
                answer.append(numbers[i] + numbers[j])

    return sorted(answer)