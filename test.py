def solution(m,n,puddles): #등굣길, 정확성/효율성테스트 통과

    d= [[0]*(m+1) for _ in range(n+1)]
    d[1][0]=1
    for j in range(1,m+1):
        for i in range(1,n+1):
            if [j,i] in puddles: # 웅덩이일 경우
                d[i][j] =0
            else: #웅덩이가 아닐 경우
                d[i][j] = d[i-1][j]+d[i][j-1]
    print(d)
    return d[m][j]
m=4
n=3
puddles=[[1,3],[2,2]]

print(solution(m,n,puddles))