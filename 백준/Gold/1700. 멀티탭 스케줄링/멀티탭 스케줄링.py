import sys

n,k = map(int,input().split())
arr = list(map(int,input().split()))
tabs = set()
for i in arr:
    tabs.add(i)
    if len(tabs) == n:
        break    

def find_pull_tab(index):
    d = {}
    for tab in tabs:
        d[tab] = sys.maxsize
    priority = 0
    for i in range(index,k):
        if arr[i] in tabs and d[arr[i]] == sys.maxsize:            
            d[arr[i]] = priority
            priority +=1
    res = []
    for key in d:
        res.append([key,d[key]])
    res.sort(key=lambda x:x[1])
    return res[-1][0]

cnt = 0
for i in range(n,k):
    if arr[i] in tabs:
        continue
    r = find_pull_tab(i)
    tabs.remove(r)
    tabs.add(arr[i])
    cnt += 1
print(cnt)



