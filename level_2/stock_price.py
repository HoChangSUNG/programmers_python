def solution(prices):#주식가격, 효율성 성공 못함
    n = len(prices)
    answer = [n-1-i for i in range(n)]
    while prices :
        compare = prices.pop()
        for i in range(len(prices)) :
            if compare<prices[i] :
                answer[i] = len(prices) - i
    return answer
prices = [1, 2, 3, 3,3 ]
print(solution(prices))