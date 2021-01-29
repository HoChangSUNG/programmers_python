def solution(routes): #단속 카메라
            #    비교할 진입,진출   ->      겹치는 구간
    # -20 ~ -15 와 -18 ~ -13 비교 -> -18 ~ -15
    # -18 ~ -15 와 -14 ~ -5 비교  -> 진입,진출 지점에 겹치는 부분이 없음, -18~-15 사이에 단속카메라 설치
    # -14 ~ -5 와 -5 ~ -3비교     ->  -5 ~ -5 사이에 단속카메라 1대 설치

    routes.sort()
    start_route = -30001
    end_route = 30001
    answer = 1
    for start, end in routes:
        if start < end_route:
            start_route = start
            if end < end_route:
                end_route=end
        elif start == end_route:
            start_route = start
            end_route= start
        else:
            print(start)
            answer += 1
            start_route = start
            end_route = end
    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)