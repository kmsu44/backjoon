def finddigit(number):
    cnt = 0
    while number > 0:
        number //= 10
        cnt+=1
    return cnt
    
def solution(storey):
    answer = 0
    while finddigit(storey)>=2:
        t = storey % 10
        storey //= 10
        if t > 5:
            t = 10 - t
            storey += 1
        elif t == 5:
            if storey % 10 >= 5:
                t = 10 - t
                storey +=1
        answer+=t
    if storey > 5:
        t = 10 - storey + 1
    else:
        t = storey
    answer += t
    return answer

# 155 -> 11
# 154 -> 10