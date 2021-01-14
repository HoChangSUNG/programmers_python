def solution(land): #땅따먹기, 다른 사람 풀이 참고
    for i in range(1,len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i-1][0:j]+land[i-1][j+1:])
    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))