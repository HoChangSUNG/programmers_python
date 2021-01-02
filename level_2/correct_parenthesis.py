from collections import deque

def is_correct_parenthesis(string): #올바른 괄호 문자열인지 확인해주는 함수
    stack = []
    for s in string :
        if s == '(' :
            stack.append(s)
        elif stack :
            stack.pop()
    return len(stack)==0
def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string
def separate_to_u_v(string):#2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리
    queue = deque(string)
    left,right = 0, 0
    u, v = "", ""
    while queue :
        char = queue.popleft()
        u += char
        if char == '(':
            left+=1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u,v
def change_to_correct_parenthesis(string):
    if string == "" :
        return ""
    u,v = separate_to_u_v(string)
    if is_correct_parenthesis(u) :
        return u + change_to_correct_parenthesis(v)
    else:
        return"(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])
def solution(p):
    if is_correct_parenthesis(p) :
        return p
    else :
        return change_to_correct_parenthesis(p)
p ="(()())()"
print(solution(p))