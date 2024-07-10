from itertools import permutations

n, m = map(int,input().split())
arr = list(map(int,input().split()))

L = list(permutations(arr,m))
L.sort(key=lambda x: [x[i] for i in range(m)])

for a in L:
    print(*a)