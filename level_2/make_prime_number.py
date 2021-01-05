import itertools
def solution(nums): #소수 만들기
    answer = 0
    total_combination = list(map(sum, list(itertools.combinations(nums, 3)))) #3개 뽑아서 더한 수 리스트로 만듦
    for combination in total_combination: # 소수 판별
        for i  in range(2,int(combination**0.5)+1):
            if combination%i == 0:
                break
        else:
            answer += 1
    return answer
nums = [1, 2, 7, 6,4]
print(solution(nums))