def solution(n):#다음 큰 숫자
    bynary = format(n,'b')
    bynary_count = 0
    next_bynary_count = 0
    for char in bynary: #현재 숫자(2진법)의 1의 개수 구하기
        if char == '1':
            bynary_count+=1
    while True :#다음 큰수 구하기
        n+=1
        next_bynary = format(n,'b')
        for char in next_bynary:
            if char == '1':
                next_bynary_count += 1
        if bynary_count == next_bynary_count:
            return n
        next_bynary_count = 0
print(solution(15))
