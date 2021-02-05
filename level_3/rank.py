def solution(n, results): # 순위, 다른 사람 코드 이용
    answer = 0
    win = {}
    lose = {}
    for i in range(1,n+1):
        win[i]=set()
        lose[i]=set()
    for i in results:
        winner ,loser = i[0],i[1]
        win[winner].add(loser)
        lose[loser].add(winner)
    print(win,lose)
    for i in range(1,n+1):
        #lose[i] : i가 진 사람들
        # #win[i] : i가 이긴사람들
        # #i가 진 사람들은 모두 i가 이긴 사람들을 이긴다.
        for winner in lose[i]:
            win[winner].update(win[i])
        #i에게 진사람들은 i를 이긴사람들에게 모두 진다.
        for loser in win[i]:
            lose[loser].update(lose[i])
        print(win, lose)
    for i in range(1,n+1):
        if(len(lose[i])+len(win[i])==n-1):
            answer+=1
    return answer

n = 5
results= [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))