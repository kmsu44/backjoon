n, k = map(int,input().split())

students = list(map(int,input().split()))

costs = []
for idx in range(1,n):
    costs.append([students[idx] - students[idx-1],idx])

costs.sort()
groups = []
for _ in range(k-1):
    groups.append(costs.pop())

groups.sort()
ans = 0
s = 0
for start,end in groups:
    ans += students[end-1] - students[s]
    s = end

ans += students[n-1] - students[s]
print(ans)