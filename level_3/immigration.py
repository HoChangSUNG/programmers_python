def solution(n, times):  # 입국심사, 문제푸는 방법도 생각못함, 다른 사람 코드 참고
    min_time = 1
    max_time = max(times) * n
    answer = 0
    while min_time<=max_time:
        mid_time = (min_time + max_time) // 2
        count = 0
        for time in times:
            count+=mid_time // time
            if count>=n:
                answer = mid_time
                break
        if count>=n:
            max_time = mid_time-1
        else:
            min_time=mid_time+1
    return answer
n=6
times=[7,10]
print(solution(n,times))