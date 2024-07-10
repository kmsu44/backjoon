

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = []
visited = set()
def make_permutation(arr,tmp):
    if len(tmp) == m:
        ans.append(tmp[::])
    for i in arr:
        if i not in visited:
            tmp.append(i)
            visited.add(i)
            make_permutation(arr,tmp)
            tmp.pop()
            visited.remove(i)

for i in arr:
    visited.add(i)
    make_permutation(arr,[i])
    visited.remove(i)

for i in ans:
    print(*i)