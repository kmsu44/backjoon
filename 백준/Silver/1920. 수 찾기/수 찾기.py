n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()
for num in arr2:
    left = 0
    right= n-1
    ans = -1
    while left <= right:
        mid = (left+right) // 2
        if arr1[mid] <= num:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    if arr1[ans] == num:
        print(1)
    else:
        print(0)