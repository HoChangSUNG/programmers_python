def solution(sticker):  # 스티커 모으기(2)
    dp = [[0 for _ in range(100000)]for _ in range(2)] # row 0 -> 첫번째 스티커 뗀 경우
                                                       # row 1 -> 첫번째 스티커 떼지 않은 경우
    n = len(sticker)
    if n==1:
        return sticker[0]
    # 첫번째 스티커 뗀 경우
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    for i in range(2,n-1):
        dp[0][i] = max(sticker[i]+dp[0][i-2],dp[0][i-1])
    dp[0][n-1] = dp[0][n-2]

    # 첫번째 스티커 떼지 않은 경우
    dp[1][0] = 0
    dp[1][1] = sticker[1]
    for i in range(2,n):
        dp[1][i] = max(sticker[i]+dp[1][i-2],dp[1][i-1])

    return max(dp[0][n-1],dp[1][n-1])

sticker =  [1, 2, 3]
print(solution(sticker))