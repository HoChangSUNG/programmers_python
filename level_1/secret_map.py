def solution(n, arr1, arr2):  # 비밀지도
    answer = []
    for i  in range(n):
        convert = ""
        temp_one = bin(arr1[i])[2:]
        temp_two = bin(arr2[i])[2:]
        one = "0"*(n-len(temp_one)) + temp_one
        two = "0" * (n - len(temp_two)) + temp_two
        for j in range(n):
            if one[j]=="0" and two[j]=="0":
                convert += " "
            else:
                convert += "#"
        answer.append(convert)
    return answer

n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))
