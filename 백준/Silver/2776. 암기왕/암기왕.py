def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        note1 = list(map(int,input().split()))
        note1.sort()
        m = int(input())
        note2 = list(map(int,input().split()))
        for num in note2:
            ans = -1
            left = 0
            right = n-1
            while left <= right:
                mid = (left + right) // 2
                if note1[mid] <= num:
                    left = mid + 1
                    ans = mid
                else:
                    right = mid - 1
            if note1[ans] == num:
                print(1)
            else:
                print(0)

main()

