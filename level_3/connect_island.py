def get_parent(a, parent): # 현재 노드의 부모 노드를 찾는 함수
    if a == parent[a]:
        return a
    else:
        return get_parent(parent[a], parent)

def solution(n, costs): # 섬 연결하기, 크루스칼 알고리즘 사용
    parent = [i for i in range(n)] #부모 노드 확인
    answer = 0
    costs.sort(key= lambda x:x[2])
    print(costs)
    for node_1, node_2, dist in costs:
        a= get_parent(node_1,parent)
        b= get_parent(node_2,parent)
        if a != b :
            answer += dist
            if a>b:
                parent[a] = b
            else:
                parent[b] = a
    return answer


n =4
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
print(solution(n,costs))