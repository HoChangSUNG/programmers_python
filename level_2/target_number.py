def factorial(n):
    answer = 1
    for i in range(2,n+1):
        answer*=i
    return answer
def solution(n, k):
    answer = []
    nums =[i for i in range(1,n+1)]
    while nums :

        # print(nums)
        c=factorial(n-1)
        # print(c)
        # print((k // c) * c)
        first_num = nums.pop(k // c)
        k -= ((k // c) * c)
        # print(first_num)
        answer.append(first_num)
    print(answer)
    return answer