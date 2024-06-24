import sys
def main():
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    left = 0
    right = sys.maxsize
    def check(k):
        cnt = 1
        remain = k
        for money in arr:
            if k < money:
                return False
            if remain < money:
                remain = k
                cnt += 1
            remain -= money
        if cnt <= m:
            return True
        return False
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return ans
print(main())