n, r, c = map(int,input().split())
SIZE = 2**n
ans = -1
cnt = 0
def find_depth(size,x,y):
    global cnt
    global ans
    if ans != -1:
        return
    if size == 2:
        for i in range(x,x+2):
            for j in range(y,y+2):
                if i == r and j == c:
                    ans = cnt
                cnt += 1
        return
    size = size // 2
    if x <= r < x+size and y <= c < y+size:
        find_depth(size,x,y)
    else:
        cnt += size * size
    if x <= r < SIZE and y+size <= c < SIZE:
        find_depth(size,x,y+size)
    else:
        cnt += size * size
    if x+size <= r < SIZE and y<= c < y+size:
        find_depth(size,x+size,y)
    else:
        cnt += size * size
    if x+size <= r < SIZE and y + size <= c < SIZE:
        find_depth(size,x+size,y+size)
    else:
        cnt += size * size
find_depth(2**n,0,0)
print(ans)
