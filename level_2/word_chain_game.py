def solution(n, words):#영어 끝말잇기
    pre_repeated = [words[0]]
    answer = [0,0]
    for idx in range(1,len(words)) :
        if words[idx][0] == pre_repeated[-1][-1] and words[idx] not in pre_repeated :
            pre_repeated.append(words[idx])
        else :
            num = idx%n + 1
            turn_num = idx//n +1
            answer = [num,turn_num]
            return answer
    return answer

n=5
words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
print(solution(n,words))
