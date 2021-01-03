
def solution(n,a,b): # 예상 대진표
    round = 0
    while a != b:
        if  a%2 == 1:
            a = (a+1)//2
        else:
            a//=2
        if  b%2 == 1:
            b = (b+1)//2
        else:
            b//=2
        round += 1
    return round

print(solution(8,4,7))