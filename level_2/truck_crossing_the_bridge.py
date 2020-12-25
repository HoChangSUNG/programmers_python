from collections import deque
#     weight 10  weight3  weight3+7  weight  6
# 1초     7      2초 7       3초 4        4초 4,5   ->다리를 건너는 트럭
#     weight 3   weight3   weight6     weight1
#     weight 1+4 weight 5+5 weight 5 weight 10
# 5초    5        6초  6     7초  6    8초  x        ->다리를 건너는 트럭, 다리를 건너는 트럭이 없을때 시간 반환
#     weight 5   weight 4   weight 4  weight 10

def solution(bridge_length, weight, truck_weights):# 다리를 지나는 트럭
    truck_count = len(truck_weights)
    wait = deque(truck_weights) #대기 트럭
    walk = deque() # 다리를 건너는 트럭(weight와 해당 트럭이 다리를 진입한 시간)
    success = deque()#다리를 지난 트럭
    time = 1
    while True :
        if time !=1 and walk[0][1] + bridge_length == time :# 다리를 다 건넌 트럭
            success_truck = walk.popleft()
            success.append(success_truck)
            weight += success_truck[0]
            if len(success) == truck_count: #모든 트럭이 다리를 다 건넜을 때
                return time
        if len(wait)!=0 and wait[0] <= weight: # 대기 트럭이 다리로 들어갈 수 있을 때,대기트럭이 0개보다 많을 때
            truck = wait.popleft()
            walk.append([truck,time])#트럭 weight와 진입 시간.
            weight-=truck
        time+=1
bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length,weight,truck_weights))