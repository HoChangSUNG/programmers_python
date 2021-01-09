import sys
dp = [[0,2,5,1,sys.maxsize,sys.maxsize],[2,0,3,2,sys.maxsize,sys.maxsize],[5,3,0,3,1,5],[1,2,3,0,1,sys.maxsize],[sys.maxsize,sys.maxsize,5,1,0,2],[sys.maxsize,sys.maxsize,5,sys.maxsize,2,0]]

visited= []

while len(visited) <len(dp):
    min = dp[0].index(max(dp[0]))

    for i in range(len(dp[0])):
        if i not in visited :
            if dp[0][i] < dp[0][min]:
                min = i
    print('index :',min)
    visited.append(min)
    for i in range(len(dp[0])):
        if dp[0][i]>dp[min][i]+dp[0][min]:
            dp[0][i] = dp[min][i]+dp[0][min]
    print(dp[0])



