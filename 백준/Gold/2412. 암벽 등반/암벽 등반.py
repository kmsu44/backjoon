from collections import deque
from bisect import bisect_left,bisect_right

N, T = map(int,input().split())

arr = [tuple(map(int,input().split())) for _ in range(N)]

x_arr = sorted(arr,key=lambda x: x[0])

def upper_bound(arr, target, index):
    left = 0
    right = len(arr)-1
    ans = - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid][index] <= target:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans
def lower_bound(arr,target,index):
    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid][index] < target:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    return ans



def BFS():
    visited = set()
    visited.add((0,0))

    q = deque()
    q.append((0,0,0))


    while q:
        x,y,cnt = q.popleft()
        if y == T:
            return cnt
        x_left = lower_bound(x_arr,x-2,0)
        x_right = upper_bound(x_arr,x+2,0)
        for idx in range(x_left,x_right+1):
            dx,dy = x_arr[idx]
            if abs(dy-y) > 2:
                continue
            if (dx,dy) not in visited:
                visited.add((dx,dy))
                q.append((dx,dy,cnt+1))
    return -1    
print(BFS())
