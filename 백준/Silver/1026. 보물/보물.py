n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

b_index_arr = []
for idx, data in enumerate(b):
    b_index_arr.append([data,idx])

b_index_arr.sort()

a.sort(reverse=True)

s = 0
for idx,data in enumerate(b_index_arr):
    b_data, b_idx = data
    s += a[idx] * b[b_idx]
print(s)