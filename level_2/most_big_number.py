def solution(numbers): # 가장 큰 수
    numbers=list(map(str,numbers))
    sorted_numbers= sorted(numbers,key = lambda num : num*3,reverse=True)
    sum = 0
    for num in list(map(int,sorted_numbers)) :
        sum += num
    if sum ==0 :
        return '0'
    return ''.join(sorted_numbers)
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))