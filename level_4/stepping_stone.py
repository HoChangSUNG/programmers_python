

def solution(distance, rocks, n): # 징검다리
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    diff=[]
    for i in range(1,len(rocks)):
        diff.append(rocks[i]-rocks[i-1])

    low,high = 1,distance
    while low<=high:
        mid = (low+high)//2
        tmp, cnt=0, 0
        for i in range(len(diff)):
            tmp+=diff[i]
            if tmp>=mid:
                tmp=0
                continue
            else:
                cnt+=1

        if cnt>n: # 현재 제거한 돌 개수 > 제거하기로 한 돌 개수
            high = mid-1
        else:# 현재 제거한 돌 개수 <= 제거하기로 한 돌 개수
            low=mid+1
    return high

distance = 23
rocks=[3, 6, 9, 10, 14, 17]
n=2
print(solution(distance,rocks,n))