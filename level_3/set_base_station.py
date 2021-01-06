import math
def solution(n, stations, w): #기지국 설치
    answer = 0
    start = 1 # 시작 아파트
    for station in stations: # 첫번째 아파트와 기지국 사이,기지국들 사이
        end = station-w-1
        if start <= end :
            answer += math.ceil((end-start+1) / (2*w+1))
        start = station+w+1
    if start <= n: # 마지막 기지국과 마지막 아파트 사이
        answer += math.ceil((n-start+1) / (2*w+1))
    return answer

