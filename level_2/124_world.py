def solution(n): #124나라의 숫자
    answer = ''
    while True :
        quotient = n //3
        div = n % 3
        if div == 0 :
            answer = '4'+answer
            quotient -=1
        else :
            answer = str(div) +answer
        if quotient == 0 :
            return answer
        n= quotient

print(solution(10))