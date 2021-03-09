def solution(money):  # 도둑질
    dp = [[0]for _ in range(2)]
    n = len(money)
    if n==1:
        return money[0]
    # 첫번째 집을 턴 경우
    dp[0][0] = money[0]
    dp[0].append(money[0])
    for i in range(2,n-1):
        dp[0].append(max(money[i] + dp[0][i - 2], dp[0][i - 1]))

    # 첫번째 집을 털지 않은 경우
    dp[1][0] = 0
    dp[1].append(money[1])
    for i in range(2,n):
        dp[1].append(max(money[i] + dp[1][i - 2], dp[1][i - 1]))

    return max(dp[0][-1],dp[1][-1])

money =  [1, 2, 3, 1]
print(solution(money))