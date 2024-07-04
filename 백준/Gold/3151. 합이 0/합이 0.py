from bisect import bisect_left
n = int(input())

students = list(map(int,input().split()))

students.sort()

cnt = 0 

for mid in range(n-2):
    left = mid + 1
    right = n-1
    while left < right:
        s = students[left] + students[mid] + students[right]
        if s == 0:
            if students[left] == students[right]:
                cnt += right-left
            else:
                idx = bisect_left(students,students[right])
                cnt += right - idx + 1
            left += 1
        elif s > 0:
            right -= 1
        else:
            left += 1
print(cnt)