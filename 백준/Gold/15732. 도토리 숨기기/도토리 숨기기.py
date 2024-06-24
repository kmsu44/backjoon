def find_minimum_boxes(n, k, d, arr):
    left, right = 1, n
    ans = -1  # Initialize the answer variable

    while left <= right:
        mid = (left + right) // 2
        cnt = 0  # Counter for the number of valid boxes

        # Calculate the number of valid boxes up to 'mid'
        for a, b, c in arr:
            last = min(mid, b)
            if last >= a:
                cnt += (last - a) // c + 1

        # Adjust the binary search range based on the count
        if cnt >= d:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

# Reading input values
n, k, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Find and print the minimum number of boxes
result = find_minimum_boxes(n, k, d, arr)
print(result)