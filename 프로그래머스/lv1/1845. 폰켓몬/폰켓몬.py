def solution(nums):
    answer = 0
    T = len(nums)//2
    D = {}
    for i in nums:
        if i in D:
            D[i] +=1
        else:
            D[i] = 1
    if T <= len(D):
        answer = T
    else:
        answer =len(D)
    return answer