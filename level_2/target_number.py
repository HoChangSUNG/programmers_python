answer = 0
def target_number(numbers,index,value,target):
    if index == len(numbers):
        if value == target :
            global answer
            answer += 1
        return
    target_number(numbers,index+1,value + numbers[index],target)
    target_number(numbers, index + 1, value - numbers[index], target)
def solution(numbers, target): # 타겟넘버
    target_number(numbers,0,0,target)
    global answer
    return answer

