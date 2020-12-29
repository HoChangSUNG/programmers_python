def solution(s) : # 짝지어 제거하기
    stack = [s[0]]
    for i  in range(1,len(s)) :
        if len(stack) != 0 and stack[-1] == s[i] :
            stack.pop()
        elif len(stack) == 0 or stack[-1] != s[i]:
            stack.append(s[i])
    # print(stack) -> 짝지어지지 않은 알파벳들 출력
    if stack :
        return 0 #-> 짝지어지지 않은 알파벳들 있을 경우
    return 1 #-> 짝지어지지 않은 알파벳들 없을 경우
s = 'baabaa'
print(solution(s))