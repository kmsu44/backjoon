import sys
    

def main():
    n, m = map(int,input().split())
    rides = list(map(int,input().split()))
    left = 0
    right = sys.maxsize
    
    def get_num_by_time(time):
        cnt = m
        for data in rides:
            cnt += time // data
        return cnt
    
    if n <= m:
        return n
    while left <= right:
        mid = (left+right) // 2
        cnt = get_num_by_time(mid)
        if cnt < n:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    s = m
    for idx,ride in enumerate(rides):
        s += (ans-1) // ride

    for idx,ride in enumerate(rides):
        if ans % ride == 0:
            s += 1
        if s == n:
            return idx+1
print(main())


