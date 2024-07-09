import sys
n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort()
arr.append([sys.maxsize,sys.maxsize])

start = arr[0][0]
last = arr[0][1]

ans = 0
for x,y in arr[1:]:
    if x <= last:
        last = max(last,y)
    else:
        ans += last - start
        start = x 
        last = y
print(ans)