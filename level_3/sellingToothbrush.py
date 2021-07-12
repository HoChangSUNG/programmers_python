def dfs(person,graph,result,amount):
    referralMoney = amount//10
    myMoney = amount-referralMoney
    result[person] += myMoney
    if referralMoney == 0 or graph[person] == "-":
        return
    dfs(graph[person], graph, result, referralMoney)

def solution(enroll, referral, seller, amount): # 다단계 칫솔 판매
    graph = dict()
    result = dict()
    for person in enroll:
        result[person]=0
    for i in range(len(enroll)):
        graph[enroll[i]]=referral[i]
    for i in range(len(amount)):
        amount[i]*=100

    for i in range(len(seller)):
        dfs(seller[i],graph,result,amount[i])

    res = [0]*(len(enroll))
    for i in range(len(res)):
        res[i]=result[enroll[i]]
    # print(res)
    return res
# enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller=["sam", "emily", "jaimie", "edward"]
# amount=[2, 3, 5, 4]
# solution(enroll, referral, seller, amount)

