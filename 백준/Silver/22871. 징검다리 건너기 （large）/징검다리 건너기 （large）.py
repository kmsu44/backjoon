
n = int(input())
L = [0] + list(map(int, input().split()))
left = 0
right = (n-1) * (1 + abs(L[n] - L[1]))
while left <= right:
    mid = (left+right)//2
    flag = 0
    stack = [1]
    visit = [True] * (n+1)
    visit[1] = False

    while stack:
        i = stack.pop()
        if i == n:
            flag = 1
            break
        for j in range(i+1, n+1):
            t = (j-i) * (1 + abs(L[i] - L[j]))
            if t <= mid and visit[j]:
                stack.append(j)
                visit[j] = False
    if flag == 1:
        right = mid-1
    else:
        left = mid + 1
print(left)
