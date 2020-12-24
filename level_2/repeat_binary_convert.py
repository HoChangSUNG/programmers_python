def solution(s):#이진 변환 반복하기
    count = 0 # 이진 변환의 횟수
    sum_delete_zero = 0 # 이진 변환 과정에서 제거된 모든 0의 개수
    while s != '1':
        delete_zero_count=s.count('0') # 제거할 0의 개수
        sum_delete_zero+=delete_zero_count
        after_zero_length = len(s)-delete_zero_count # 0제거 후 길이
        s = bin(after_zero_length)[2:] # 이진 변환 결과(0b는 제외하고 s에 저장)
        count += 1
    return [count,sum_delete_zero]

print(solution("1111111"))

