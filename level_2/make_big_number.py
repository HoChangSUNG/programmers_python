def solution(number, k):#큰 수 만들기
        # 1924 2자리로 이루어진 최고값 반환
        # ---  ->최고값:9(index범위 : -4~-2까지)
        #   -- ->최고값:4(index범위 : -2~-1까지)
        # 1231234 4자리로 이루어진 최고값 반환
        # ----    ->최고값:3(index범위 : -7~-4까지)
        #    --   ->최고값:2(index범위 : -4~-3까지)
        #      -  ->최고값:3(index범위 : -2~-2까지)
        #       - ->최고값:4(index범위 : -1~-1까지)
    answer = ''
    n = len(number) - k
    start_index = -len(number)#초기 설정
    end_index = -n + 1#초기 설정
    for i in range(1,n+1):
        max = number[start_index]
        max_index = start_index
        for j  in range(start_index,end_index):#탐색할index 범위 내에서 최대값 찾기
            if max =='9':#9가 최고 큰 수이므로 더이상 비교하지 않아도 됨.
                break
            elif max < number[j] :
                max=number[j]
                max_index = j
        start_index=max_index+1#탐색할index 범위 변경
        end_index +=1
        answer += max
    return answer
k=2
number = "1924"
print(solution(number,k))