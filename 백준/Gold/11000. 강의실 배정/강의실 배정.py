import heapq

n = int(input())
classes = [list(map(int,input().split())) for _ in range(n)]
classes.sort()


q = []
ans = 0
for start,end in classes:
    while q and q[0] <= start:
        heapq.heappop(q)
    heapq.heappush(q,end)
    ans = max(ans,len(q))
print(ans)