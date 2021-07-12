# 가장 긴 펠린드롬
import sys
sys.setrecursionlimit(10**9)
def isPalindrome(s) :
    if len(s)<=1:
        return True
    if s[0]==s[-1]:
        return  isPalindrome(s[1:-1])
    else:
        return False
def solution(s):
    for length in range(len(s),0,-1):
        for i in range(len(s)):
            if i+length>len(s):
                break
            if isPalindrome(s[i:i+length]):
                return length


