citations=[3,0,6,1,5]
def solution(citations):#H-index
    # 피인용수 논문수
    # 6          1
    # 5          2
    # 3 <-h_index3
    # 1          4
    # 0          5
    #h_index = 피인용수가 논문수와 작아지기 시작하기 직전 논문수
    sorted_citations = sorted(citations,reverse=True)
    answer = len(sorted_citations) # 예외: for문 다 돌고 answer이 return되지 않으면 논문의 수 반환
    for idx  in range(len(sorted_citations)) :
        if sorted_citations[idx] <idx + 1 :
            answer = idx
            return answer
    return answer
print(solution(citations))
