from collections import deque
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

jewel_cnt = 0
impurities = dict()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            jewel_cnt += 1
        if graph[i][j] == 1:
            impurities[(i,j)] = 0
    

def count_jewel_impurities(x1,x2,y1,y2):
    j_cnt = 0
    i_cnt = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            if graph[i][j] == 2:
                j_cnt += 1
            if graph[i][j] == 1:
                i_cnt += 1
    return j_cnt,i_cnt



def in_range(x,y,x1,x2,y1,y2):
    return x1 <= x < x2 and y1 <= y < y2

def is_jewel(i,j,x1,x2,y1,y2,direction):
    if direction == 'row':
        for y in range(y1,y2):
            if graph[i][y] == 2:
                return False
    else:
        for x in range(x1,x2):
                if graph[x][j] == 2:
                    return False
    return True


def divide(x1,x2,y1,y2,direction):
    j_cnt,i_cnt = count_jewel_impurities(x1,x2,y1,y2)
    ans = 0
    # 판으로 결정이 난 경우
    if j_cnt == 0 or j_cnt >=2 and i_cnt ==0 or j_cnt==1 and i_cnt >= 1:
        return 0
    if j_cnt == 1 and i_cnt == 0:
        return 1
    tmp = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            if graph[i][j] == 1 and is_jewel(i,j,x1,x2,y1,y2,direction):
                if direction == 'row':
                    # 가로로 분할
                    if (i == x2 - 1 or i == x1):
                        continue
                    tmp = divide(x1,i,y1,y2,'col') * divide(i+1,x2,y1,y2,'col')
                else:
                    # 세로 분할
                    if (j == y2-1 or j == y1):
                        continue
                    tmp = divide(x1,x2,y1,j,'row') * divide(x1,x2,j+1,y2,'row')
                ans += tmp
    return ans
    
    
row = divide(0,n,0,n,'row')
col = divide(0,n,0,n,'col')
ans = row+col
if ans == 0:
    print(-1)
else:
    print(ans)
