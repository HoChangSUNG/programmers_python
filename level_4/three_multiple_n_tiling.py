# D[n] = 3*D[n-2] + 2(D[n-4]+D[n-6] ... D[0])
def solution(n):  # 3 * n 타일링
    dp = [0 for _ in range(5001)]
    dp[0] = 1
    dp[2] = 3
    if n % 2 == 0:
        for i in range(4, n + 1, 2):
            dp[i] = (3 * dp[i - 2] + 2 * (sum(dp[:i - 2])))%1000000007
        return dp[n]
    else:
        return dp[n]