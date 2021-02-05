answer = []
def hanoi(n,start,mid,end):
    if n==1:
        answer.append([start,end])  # 원반이 1개일 경우 이동
        return
    hanoi(n-1,start,end,mid)  # 1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮김(3번 기둥 거쳐서)
    answer.append([start,end])  # 1번 기둥에 남아있는 가장 큰 원판 1개를 3번 기둥으로 옮김
    hanoi(n-1,mid,start,end)  # 2번 기둥에 있는 n-1개의 원판을 3번 기둥으로 옮김(1번 기둥 거쳐서)

def solution(n):  # 하노이의 탑
    hanoi(n,1,2,3)
    return answer


n = 3
print(solution(n))