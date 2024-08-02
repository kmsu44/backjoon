from collections import deque
def find_pos(building,l,r,c):
    s = (-1,-1,-1)
    e = (-1,-1,-1)
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    s = (i,j,k)
                if building[i][j][k] == 'E':
                    e = (i,j,k)
    return s,e


def in_range(x,y,z,l,r,c):
    return 0 <= x < l and 0 <= y < r and 0 <= z < c

moves = [
    [0,0,1],
    [0,0,-1],
    [0,1,0],
    [0,-1,0],
    [1,0,0],
    [-1,0,0]
]

def BFS(sx,sy,sz,ex,ey,ez,l,r,c):
    q = deque()
    visited = set()
    visited.add((sx,sy,sz))
    q.append((sx,sy,sz,0))
    while q:
        x,y,z,cnt = q.popleft()
        if x== ex and y == ey and z == ez:
            return cnt
        for xx,yy,zz in moves:
            dx = x + xx
            dy = y + yy
            dz = z + zz 
            if in_range(dx,dy,dz,l,r,c) and (dx,dy,dz) not in visited and (graph[dx][dy][dz] == '.' or graph[dx][dy][dz] == 'E'):
                q.append((dx,dy,dz,cnt + 1))
                visited.add((dx,dy,dz))
    return -1
    
    
    

while True:
    l, r, c = map(int,input().split())
    if l == r == c == 0:
        break
    graph = []

    for _ in range(l):
        floor = [list(input()) for _ in range(r)]
        tmp = input()
        graph.append(floor)
    
    s,e = find_pos(graph,l,r,c)
    
    time = BFS(s[0],s[1],s[2],e[0],e[1],e[2],l,r,c)
    if time == -1:
        print('Trapped!')
    else:
        print('Escaped in',time,'minute(s).')
    



