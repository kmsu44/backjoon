import heapq
        
n = int(input())
q = []

for _ in range(n):
    lope = int(input())
    heapq.heappush(q,lope)
ans = 0
while q:
    size = len(q)
    min_weight = heapq.heappop(q)
    ans = max(ans,min_weight * size)
print(ans)