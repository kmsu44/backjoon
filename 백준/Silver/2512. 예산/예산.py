def main():
    n = int(input())
    requests = list(map(int,input().split()))
    budget = int(input())
    requests.sort()
    left = 0
    right = requests[-1]
    

    while left <= right:
        mid = (left+right) // 2
        s = 0
        for request in requests:
            if request <= mid:
                s += request
            else:
                s += mid
        if s <= budget:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans

print(main())

