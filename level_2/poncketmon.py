def solution(nums):
    set_nums = set(nums)
    if len(set_nums) >= len(nums)//2 : # 중복을 제거한 종류 개수가 선택할 수 있는 폰켓몬 개수와 같거나 클때
        return len(nums)//2
    else :
        return len(set_nums)
nums = [3,3,3,2,2,2]
print(solution(nums))