import sys
sys.setrecursionlimit(100000)
def solution(cards1, cards2, goal):
    answer = 'No'
    result = []
    def combine(cards1,cards2,R):
        if len(cards1) == 0:
            R += cards2
            result.append(R)
            return
        if len(cards2) == 0:
            R += cards1
            result.append(R)
            return
        combine(cards1[1:],cards2,R + cards1[:1])
        combine(cards1,cards2[1:],R + cards2[:1])
        return
    combine(cards1,cards2,[])
    size = len(goal)
    for i in result:
        if size <= len(i):
            if goal == i[:size]:
                answer= 'Yes'
    return answer