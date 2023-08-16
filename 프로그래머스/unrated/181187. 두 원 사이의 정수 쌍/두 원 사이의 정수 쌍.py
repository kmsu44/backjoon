

import math
def solution(r1, r2):
    
    answer = 0 
    for x in range(1,r1+1):
        h2 = int(math.sqrt(r2*r2-x*x))
        h1 = math.sqrt(r1*r1-x*x)
        answer += int(h2-h1+1)
    for x in range(r1+1,r2+1):
        h2 = int(math.sqrt(r2*r2 - x*x))
        if h2 == 0:
            answer +=1
        else:
            answer += int(h2) +1
            
    # print(answer)
    answer *= 4
    
    
    
    return answer






