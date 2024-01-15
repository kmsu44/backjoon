from collections import defaultdict
def solution(participant, completion):
    answer = ''
    L = defaultdict(int)
    for i in participant:
        L[i] +=1
    for j in completion:
        L[j] -=1
    for i in L:
        if(L[i] != 0):
            answer = i
            
    return answer