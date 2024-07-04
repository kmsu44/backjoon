from bisect import bisect_left,bisect_right

def make_sub_array(arr):
    size = len(arr)
    dp = []
    for i in range(size):
        s = 0
        for j in range(i,size):
            s += arr[j]
            dp.append(s)
    dp.sort()
    return dp

T = int(input())
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2= list(map(int,input().split()))
sub_arr1 = make_sub_array(arr1)
sub_arr2 = make_sub_array(arr2)


cnt = 0
for k in sub_arr1:
    target = T - k
    cnt += bisect_right(sub_arr2,target) - bisect_left(sub_arr2,target)
print(cnt)